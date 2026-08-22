'''import seaborn as sns

# 1. List all available built-in dataset names
print(sns.get_dataset_names())

# 2. Load a specific dataset as a Pandas DataFrame
df = sns.load_dataset('tips')
print(df.head())'''

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.DataFrame({
    "Name":["Shikhar","Shivam","Saurabh","Shivansh","Suryansh","Shivesh"],
    "Marks":[80, 58, 68, 95, 74, 55],
    #"Address":["Pratapgarh","Ballia","Kunda","Prayagraj","Allahabad","Rewa"]
})
# sns.barplot(data=df,x="Name",y="Marks")
# plt.show()
# sns.scatterplot(data=df,x="Name",y="Marks")
# plt.show()
# sns.lineplot(data=df,x="Name",y="Marks")
# plt.show()
# sns.countplot(x="Name",data = df)
# plt.show()
# sns.boxplot(data=df,x="Name",y="Marks")
# plt.show()
# sns.violinplot(data=df,x="Name",y="Marks")
# plt.show()
# sns.histplot(df["Marks"])
# plt.show()
# sns.pairplot(df)
# plt.show()
# correlation = df.corr(numeric_only=True)
# sns.heatmap(correlation, annot = True)
# plt.show()
# sns.barplot(data=df,x="Name",y="Marks", color="green")
# plt.show()
# sns.set_style("darkgrid")
# sns.barplot(data=df,x="Name",y="Marks")
# plt.show()
# sns.barplot(data=df,x="Name",y="Marks", hue= "Marks")
# plt.show()
# sns.kdeplot(df["Marks"])
# plt.show()
# sns.stripplot(data=df,x="Name",y="Marks")
# plt.show()
# sns.swarmplot(data=df,x="Name",y="Marks")
# plt.show()
# sns.catplot(data=df,x="Name",y="Marks",kind="bar")
# plt.show()
# plt.figure(figsize=(8,5))
# sns.barplot(data=df,x="Name",y="Marks")
# plt.show()
# sns.barplot(data=df,x="Name",y="Marks")
# plt.savefig("graph.png")
sns.set_style("whitegrid")
sns.barplot(data=df,x="Name",y="Marks",hue="Marks")
plt.title("Student Marks")
plt.xlabel("Marks")
plt.ylabel("Name")
plt.show()