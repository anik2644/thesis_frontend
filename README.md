# NLP Model Evaluation and Dataset Processing

This repository contains scripts and resources for evaluating the **BuetT5 model**, dataset translation, dataset filtering, Named Entity Recognition (NER), and training/evaluating T5 models.

## Features
- **BuetT5 Model Evaluation**: Evaluates the performance of the BuetT5 model.
- **Dataset Translation**: Translates datasets from English to Bangla.
- **Dataset Filtering**: Filters datasets based on predefined criteria.
- **Named Entity Recognition (NER)**: Processes and trains NER models.
- **T5 Model Training & Evaluation**: Scripts for training and evaluating T5 models.

## Resources & Notebooks
### **1. BuetT5 Model Evaluation**
- Colab Notebook: [BuetT5 Evaluation](https://colab.research.google.com/drive/1yut0I29paxtLbFGyoW8PbpA7L5M9ELx6)

### **2. Dataset & Processing**
- Dataset: [ChatGPT Paraphrases](https://huggingface.co/datasets/humarin/chatgpt-paraphrases)
- Dataset Translation: [English to Bangla](https://colab.research.google.com/drive/1lQvIAdb4D-TA4TKET2YdXYE53sNbEZUf)
- Dataset Filtering:
  - [Thesis Filter Repository](https://github.com/anik2644/Thesis_FIlter/tree/final)
  - [Bangla Paraphrase Dataset](https://github.com/csebuetnlp/banglaparaphrase/blob/master/README.md)

### **3. Named Entity Recognition (NER)**
- Dataset Specification: [NER Dataset](https://colab.research.google.com/drive/1D6m8V-NAhiV8kucfhZvGCqr7cFGQEPPu)
- Training Notebook: [Train NER Model](https://colab.research.google.com/drive/1IjRTRh7RwgQZI10rVgCZb8ZS2DjwWLn6)

### **4. T5 Model Training & Evaluation**
- Train T5: [Colab Notebook](https://colab.research.google.com/drive/1SspmaXYJDDnAYcWZjmA9vzlUc4sM4m0x)
- Evaluate T5: [Colab Notebook](https://colab.research.google.com/drive/1bTkaX5-d9Xzc4whCmEhEhx3aLseFW2Ad#scrollTo=WLHxz_gb8ajK)

## Installation & Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/NLP_Model_Evaluation.git
   cd NLP_Model_Evaluation
   ```
2. Install dependencies (if required):
   ```sh
   pip install -r requirements.txt
   ```
3. Run dataset filtering:
   ```sh
   python dataset_filter.py
   ```

## Folder Structure
```
NLP_Model_Evaluation/
│-- buet_t5_eval.ipynb        # BuetT5 Evaluation Notebook
│-- dataset_translation.ipynb # Dataset Translation Notebook
│-- dataset_filter.py         # Script for filtering dataset
│-- ner_train.ipynb           # NER Training Notebook
│-- train_t5.ipynb            # T5 Training Notebook
│-- eval_t5.ipynb             # T5 Evaluation Notebook
│-- README.md                 # Project documentation
│-- data/                     # Folder containing datasets
```

## Contributing
Feel free to fork this repository and contribute improvements! Pull requests are welcome.

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Contact
For any issues or suggestions, please open an issue or reach out to [your email or GitHub profile].

