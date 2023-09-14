import numpy as np
import pandas as pd
from transformers import pipeline
import datachange as dc

classifier = pipeline("sentiment-analysis")

# results = classifier(["I hate nev", "I really love teena"])

# for res in results:
#     print(res)

df = dc.text_to_df()
print(df)