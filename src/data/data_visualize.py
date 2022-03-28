import pandas as pd


stock_code = "1925"

df = pd.read_csv(f".{stock_code}.csv")

print(df)