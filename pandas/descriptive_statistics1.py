import pandas as pd

names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
df = pd.read_csv(r'..\data\pima-indians-diabetes.csv',names=names)
print(df.head(3))
print()
print(df.shape)