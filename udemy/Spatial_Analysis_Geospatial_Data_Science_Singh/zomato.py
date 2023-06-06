import pandas as pd
import numpy as np

df = pd.read_csv(r'D:\Downloads\zomato.csv')
print(df.isna().sum())