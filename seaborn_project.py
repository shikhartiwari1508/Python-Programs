import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.DataFrame({
    "total_bill":[80, 58, 68, 95, 74, 55],
    "tip":[5, 8, 6, 9, 4, 3],
    "Sex":["male","female","male","female","male","female"],
    "Smoker":["No","No","No","No","No","No"],
    "Day":["Mon","Wed","Fri","Sun","Sat","Sat"],
    "Time":["Dinner","Dinner","Dinner","Lunch","Breakfast","Lunch"],
    "Size":[2,1,3,1,2,1],
})
sns.set_style("whitegrid")
sns.barplot(data=df,x="Day",y="total_bill",hue="Sex")
plt.title("Average bill Day by Day")
plt.xlabel("Day")
plt.ylabel("Average Bill")
plt.show()