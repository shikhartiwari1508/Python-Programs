'''name = "python"
print(name)

message = "i love python"
print(message)

greet = "hello"
#indexing
print(greet[1])
#negative indexing
print(greet[-5])
#slicing
print(greet[1:5])


#compare two string
str1="hello world"
str2="i love python"
str3="hello world"
print(str1==str2)
print(str1==str3)


#join two or more string
name="shikhar"
cost="tiwari"
fullname= name+cost
print(fullname)


#iterate through a python string
greet="hello"
for letter in greet:
    print(letter)

#string length
var="hello"
print(len(var))


#string membership test
print("a"in "program")
print("a" not in "program")


#python string formatting (f-string)
name = "shikhar"
country="india"
print(f'{name} is from {country}')


a = ''hello how are you , are you fine .
what can you doing , are you working?''
print(a)

for character in name:
    print (name)


fruit = "Mango"
mangolen = len(fruit)
print(mangolen)
print(fruit[0:4])
print(fruit[1:4])
print(fruit[:4])
print(fruit[0:-4])
print(fruit[:-3])
print(fruit[-4:-2])'''

#string methods :
nm = "Rohit"
print(nm.upper())
print(nm.lower())
print(nm.rstrip())
print(nm.rstrip("!"))
print(nm.replace("Rohit" , "Shikhar"))
print(nm.split())
print(nm.capitalize())
print(nm.center(10))
print(nm.count("h"))
print(nm.endswith("t"))
print(nm.startswith("R"))
print(nm.find("h"))
print(nm.index("h"))
print(nm.isalnum())
print(nm.isalpha())
print(nm.islower())
print(nm.isprintable())
print(" ".isspace())
print(nm.istitle())
print(nm.startswith("R"))
print(nm.swapcase())
print(nm.title())