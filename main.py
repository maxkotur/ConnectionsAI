import numpy as np
import pandas as pd
from transformers import pipeline, AutoTokenizer
import datachange as dc

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)

df = dc.text_to_df()

X = df[['word1', 'word2', 'word3', 'word4']]
y = df[['titles']]

print(X.head())
print(y.head())

max_seq_length = 4  # Adjust this based on the data
X_tokens = {
    col: [] for col in X.columns
}

for col in X.columns:
    X_tokens[col] = X[col].apply(lambda x: tokenizer.encode(x, add_special_tokens=False,
                                                            max_length=max_seq_length,
                                                            padding='max_length',
                                                            truncation=True))
X_tokens = pd.DataFrame(X_tokens)       
print(X_tokens)