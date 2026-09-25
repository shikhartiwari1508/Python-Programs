#List

print("List :")
list = [ 8,2,2.5,[-4,5],["apple","banana"]]
print(list)
print(list[1])



#Largest Element in a list

num = [10,24,85,69,36]
largest = num[0]
for n in num :
    if n > largest:
        largest = n
print("Largest Number :", largest)

#Smallest Element in a list

num = [10,24,85,69,36]
smallest = num[0]
for n in num :
    if n < smallest :
        smallest = n
print("Smallest Number :", smallest)



#Tuple

print("Tuple :")
tuple = (("lion","dog","tiger"),("banana","apple","pineapple"))
print(tuple)



#Dictionary

print("Dictionary :")
dict = {"name":"shikhar", "age": 20, "eligible for vote": True}
print(dict)



# OR dictionary

dict = {
    "name":"hello",
    "roll no.": 25
}
print(dict["name"])



#Set

print("Set")
s = {1,2,3,4,5}
print(s)