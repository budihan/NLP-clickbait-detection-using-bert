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


# # https://towardsdatascience.com/text-classification-with-bert-in-pytorch-887965e5820f

# from transformers import BertModel, BertConfig, BertTokenizer

# tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')

# # Initializing a BERT bert-base-uncased style configuration
# configuration = BertConfig()

# # Initializing a model from the bert-base-uncased style configuration
# model = BertModel(configuration)

# # Accessing the model configuration
# configuration = model.config

# def train(model, train_data, val_data, learning_rate, epochs):
#     train, val = 