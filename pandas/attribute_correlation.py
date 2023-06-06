import pandas as pd

names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
df = pd.read_csv(r'..\data\test_csv.csv',names=names)
# pd.set_option('display.width',200)
correlations = df.corr(method='pearson')
print(correlations)