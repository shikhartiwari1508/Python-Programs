# Writing file:

'''file = open ("C:\\Users\\Dell\\OneDrive\\Desktop\\shikhar\\demo.txt","w")
file.write("Hello Python...\n Hello Suresh")
print("file wrote succesfully...")
file.close()

# Reading file:

file = open ("C:\\Users\\Dell\\OneDrive\\Desktop\\shikhar\\demo.txt","r")
print(file.read())
file.close()

file = open ("C:\\Users\\Dell\\OneDrive\\Desktop\\shikhar\\demo.txt","r")
print(file.read(7))
file.close()


f=open("C:\\Users\\Dell\\OneDrive\\Desktop\\shikhar\\demo.txt","r")
print(f.readline())
a=(f.readline())
print(len(a))

f=open("C:\\Users\\Dell\\OneDrive\\Desktop\\shikhar\\demo.txt","r")
print(f.readlines())'''


#if file was not exist then we can use "try-except" and print messege.......

try:
   f=open("C:\\Users\\Dell\\OneDrive\\Desktop\\shikhar\\A.txt","r")
   print(f.readlines())
except:
   print("File not avalible... please create first...")   
