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


# Remove duplicates from a list

numbers = [10,52,20,95,0,10,20]
unique = []
for num in numbers :
    if num not in unique :
        unique.append(num)
print("Original list : ", numbers)
print("List without duplicates :", unique)        


# sum of elements in a list

numbers = [10,20,30,40,50]
sum = 0
for num in numbers :
    sum = sum + num
print("Sum of list =", sum)


#Count Even and odd in list

numbers = [10,52,20,95,0,10,20]
even = 0
odd = 0 
for num in numbers :
    if num % 2 == 0 :
        even = even + 1
    else :
        odd = odd + 1
print("Even Numbers :", even)
print("Odd Numbers : ", odd)            


# find average of elements in a list

numbers = [10,52,20,95,0,10,20]
sum = 0
for num in numbers :
    sum = sum  + num
    average = sum / len(numbers)
    print("Average =", average)

# Reverse a list 

numbers = [10,20,30,40,50]
reverse = numbers[ :: -1]
print("Original List =", numbers)
print("Reversed List =", reverse)

#Check if an element exist in a list

numbers = [10,52,20,95,0,10,20]
num = int(input("Enter the Number :"))
if num in numbers :
    print("Element is Present in  a list")
else:
    print("Element is not present in a list")    

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