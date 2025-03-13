from fastapi import FastAPI
from pydantic import BaseModel
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import re
import json
from fastapi.middleware.cors import CORSMiddleware


# Initialize FastAPI
app = FastAPI()


# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to your frontend URL for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load the model
device = "cuda" if torch.cuda.is_available() else "cpu"

model_name = "csebuetnlp/banglat5_banglaparaphrase"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name)


# Named Entity Replacement
english_to_bangla = {
    "b": "বি",
    "c": "সি",
    "d": "ডি",
    "l": "এল",
    "m": "এম",
    "n": "এন",
    "p": "পি",
    "q": "কিউ",
    "x": "এক্স",
    "y": "ওয়াই",
}

named_entities = [
    "বিকাশ",
    "নগদ",
    "বিপিডিবি",
    "ডেসকো",
    "পল্লী বিদ্যুৎ",
    "রবি",
    "গ্রামীণফোন",
    "সোনালী ব্যাংক",
    "জনতা ব্যাংক",
    "দারাজ",
]


def replace_named_entities(sentence):
    replacements = []
    for idx, entity in enumerate(named_entities):
        if entity in sentence:
            placeholder = list(english_to_bangla.values())[idx % len(english_to_bangla)]
            sentence = sentence.replace(entity, placeholder)
            replacements.append(f"{placeholder} : {entity}")
    return sentence, replacements


def restore_named_entities(paraphrases, replacements):
    restored_paraphrases = []
    for para in paraphrases:
        restored_para = para
        for replacement in replacements:
            placeholder, original_entity = replacement.split(" : ")
            restored_para = re.sub(
                rf"(?<!\w){re.escape(placeholder)}(?!\w)",
                original_entity,
                restored_para,
            )
        restored_paraphrases.append(restored_para)
    return restored_paraphrases


def generate_paraphrase(text, max_length=128, num_return_sequences=3, num_beams=5):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding="max_length",
        max_length=max_length,
    ).to(device)

    outputs = model.generate(
        **inputs,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        num_beams=num_beams,
    )

    paraphrased_texts = [
        tokenizer.decode(output, skip_special_tokens=True) for output in outputs
    ]
    return paraphrased_texts


# API Request Model
class SentenceInput(BaseModel):
    sentence: str


@app.post("/paraphrase/")
async def paraphrase_text(data: SentenceInput):
    replaced_sentence, replacements = replace_named_entities(data.sentence)
    paraphrases = generate_paraphrase(replaced_sentence, num_return_sequences=3)
    paraphrases = restore_named_entities(paraphrases, replacements)

    return {"original": data.sentence, "paraphrases": paraphrases}
