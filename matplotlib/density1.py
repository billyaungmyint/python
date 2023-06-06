from matplotlib import pyplot as plt
import pandas as pd

names = ['preg','plas','pres','skin','test','mass','pedi','age','class']
df = pd.read_csv(r'..\data\pima-indians-diabetes.csv',names=names)
df.plot(kind='density',subplots=True,layout=(3,3),sharex=False)
plt.show()
