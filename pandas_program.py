# PANDAS PROGRAMME :

'''import pandas as pd
data = {
    "name": ["A","B","C","D"]
}
df = pd.DataFrame(data)
print(df)'''



'''import pandas as pd
data = {
    "name": ["Shikhar","Saurabh","Shivam","Shivansh"],
    "Marks":[20,19,18,17]
}
df = pd.DataFrame(data)
print(df)
'''


import pandas as pd

df = pd.DataFrame({"Marks":[20,19,18,17]})
print("Average = ",df["Marks"].mean())

