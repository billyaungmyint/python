import pandas as pd

names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
df = pd.read_csv(r'..\data\pima-indians-diabetes.csv' , names=names)

class_count= df.groupby('class').size()
# class 0 has 500 but class 1 has 268
print(class_count)
