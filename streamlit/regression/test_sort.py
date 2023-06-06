import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Advert": ["Radio" , "TV" , "FB"],
    "Sales": [1000, 2500, 3500]
}
df = pd.DataFrame(data)

fig = plt.figure()
sorted = df.sort_values(by="Sales",ascending=False)
plt.bar("Advert" , "Sales" , data=sorted)
plt.show()

# education = ["Bachelor's", "Less than Bachelor's","Master's","PhD","Professional"]
# # mean annual salary in US dollars
# salary = [110000,105000,126000,144200,95967]
#
# # create Pandas dataframe from two lists
# df = pd.DataFrame({"Education":education,
#                   "Salary":salary})
#
# df_sorted_desc= df.sort_values('Salary',ascending=False)
#
# plt.figure(figsize=(10,6))
# # bar plot with matplotlib
# plt.bar('Education', 'Salary',data=df_sorted_desc)
# plt.xlabel("Education", size=15)
# plt.ylabel("Salary in US Dollars", size=15)
# plt.title("Bar plot in Descending Order with Matplotlib", size=18)
# plt.show()