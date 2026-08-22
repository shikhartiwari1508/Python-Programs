#MATPLOTLIB PROGRAMME :

'''import matplotlib.pyplot as plt
x=[1,2,3]
y=[4,5,6]
plt.plot(x,y)
plt.show()'''

#Bar chart
'''import matplotlib.pyplot as plt
students = ["A","B","C","D"]
marks = [80,90,85,76]
plt.bar(students,marks)
plt.title("Student Marks")
plt.show()'''

#Pie chart

'''import matplotlib.pyplot as plt
subject =["Physics","Chemistry","Mathmatics","Biology","Computer Science"]
marks =[75,98,85,69,73]
plt.pie(marks , labels = subject,autopct = "%1.1f%%")
plt.title("Marks Distribution ")
plt.show()'''


#Draw a histogram

'''import matplotlib.pyplot as plt
marks =[98,96,85,76,89,48,69,82]
plt.hist(marks)
plt.title("Histogram")
plt.show()'''


#Scatter plot

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y =[98,96,85,76,89]
plt.scatter(x,y)
plt.title("Scatter plot")
plt.show()