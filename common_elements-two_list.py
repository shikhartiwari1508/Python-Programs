list1 = [10,20,30,40,50]
list2 = [30,40,50,60,70]
common = []
for num in list1:
    if num in list2:
        common.append(num)
print("Common Elements :", common)    