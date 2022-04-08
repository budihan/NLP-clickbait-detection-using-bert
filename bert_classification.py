from sklearn.model_selection import train_test_split
from transformers import BertModel, BertConfig, BertTokenizer

model_name = 'bert-base-cased'

# Tokenizer
tokenizer = BertTokenizer.from_pretrained(model_name)
bert_input = tokenizer("example text", truncation=True, return_tensors="pt")

# Model
config = BertConfig()
model = BertModel(config))


def read_webisData(test_size=0.2):
    X = 'Some documents'
    Y = 'Some labels'

    return train_test_split(X, Y, test_size, shuffle=True)
