'''from scipy import linalg
A=[[1,2],
   [3,4]]
inverse = linalg.inv(A)
print(inverse)'''

from scipy import stats
data = [10,20,30,40,50]
print("Mean :",stats.tmean(data))
print("Varience :",stats.tvar(data))