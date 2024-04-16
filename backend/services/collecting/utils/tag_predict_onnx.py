import numpy as np
from transformers import BertTokenizerFast
from onnxruntime import InferenceSession

class RuBERTONNX:
    def __init__(self, model_path, tokenizer_path, max_lenght):
        self.model_path = model_path
        self.tokenizer_path = tokenizer_path
        self.max_lenght = max_lenght
        self.session = InferenceSession(self.model_path)
        self.tokenizer = BertTokenizerFast.from_pretrained(self.tokenizer_path)

    def predict(self, text):
        # Преобразуйте текст в токены и получите входные данные для модели BERT
        inputs = self.tokenizer(text, return_tensors="pt",max_length=self.max_lenght, truncation=True)
        
        # Получите тензоры input_ids, token_type_ids и attention_mask
        input_ids = inputs['input_ids']
        token_type_ids = inputs['token_type_ids']
        attention_mask = inputs['attention_mask']

        # Преобразуйте тензоры к типу данных int64
        input_ids = input_ids.long()
        token_type_ids = token_type_ids.long()
        attention_mask = attention_mask.long()

        # Запустите модель
        outputs = self.session.run(output_names=["logits"], input_feed={
            'input_ids': input_ids.numpy(),
            'token_type_ids': token_type_ids.numpy(),
            'attention_mask': attention_mask.numpy()
        })[0]

        labels = {'Из жизни' : 0, 'Культура': 1, 'Наука и техника' : 2, 'Общество' :3, 'Политика' :4,
       'СВО/Украина': 5, 'Следствие и суд': 6, 'Среда обитания' : 7, 'Экономика': 8}
       
        prediction = list(labels.values())[outputs.argmax()]
        text_pred = list(labels.keys())[list(labels.values()).index(prediction)]
        return text_pred
    