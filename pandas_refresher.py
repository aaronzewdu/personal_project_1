import pandas as pd

raw_data = pd.read_csv("data/rrf_foia.csv", encoding="latin-1")

print(raw_data.head())
