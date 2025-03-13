import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
import re
import json


device = "cuda" if torch.cuda.is_available() else "cpu"

model_name = "csebuetnlp/banglat5_banglaparaphrase"  # "mhdank/t5-paraphrase_finetuned"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)
tokenizer = AutoTokenizer.from_pretrained(model_name)


def generate_paraphrase(text, max_length=128, num_return_sequences=3, num_beams=5):
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding="max_length",
        max_length=max_length,
    ).to(device)

    # print(inputs)
    # print("     dwdsdsd     ")
    outputs = model.generate(
        **inputs,
        max_length=max_length,
        num_return_sequences=num_return_sequences,
        num_beams=num_beams,
    )

    # print(outputs)
    paraphrased_texts = [
        tokenizer.decode(output, skip_special_tokens=True) for output in outputs
    ]
    return paraphrased_texts


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


def process_sentences(sentences, output_file="paraphrases.json"):
    results = []
    for sentence in sentences:
        replaced_sentence, replacements = replace_named_entities(sentence)
        paraphrases = generate_paraphrase(replaced_sentence, num_return_sequences=3)
        paraphrases = restore_named_entities(paraphrases, replacements)
        results.append({"original": sentence, "paraphrases": paraphrases})

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print(f"Paraphrases saved to {output_file}")


if __name__ == "__main__":
    sample_sentences = [
        "বিকাশ দিয়ে বিদ্যুৎ বিল পরিশোধ করা যাবে কি?",
        "নগদ এর মাধ্যমে বিদ্যুৎ বিল দিতে চাই ।",
        "বিপিডিবি বিল জমা দিয়েছি, কিন্তু সংযোগ চালু হয়নি ।",
    ]
    process_sentences(sample_sentences)


import torch
import transformers

print(torch.__version__)
print(transformers.__version__)
