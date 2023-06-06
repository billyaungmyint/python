import pandas as pd

# dict = {'a' : 3 , 'b' : 'cat', 'c' : 2.5}
# pd.Series(dict)
# dict

d = {'A' : pd.Series([100.,200.,300.], index=['apple','pear','orange']) ,
     'B' : pd.Series([111.,222.,333.,444.], index=['apple','pear','orange','melon'])}

df = pd.DataFrame(d)
print(df)