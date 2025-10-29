# matrix  calculation in Normal Python:

a=[[1,2],[3,4]]
b=[[5,6],[7,8]]
result=[[0,0],[0,0]]
for i in range(len(a)):
    for j in range(len(a)):
        result[i][j]=a[i][j] + b[i][j]
for o in result:
    print(o)

# Matrix Calculation with the uses of Numpy Library:

import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
print(a+b)
    
# matrix Calculation using Numpy library and Loop concepts:
import numpy as np
a=np.array([[1,2],[3,4]])
b=np.array([[1,5],[7,8]])
for row in a:
    print(np.sum(row))                      # row wise sum
for rwo in b:
    print(np.sum(rwo))  
              
result=np.zeros((2,2),dtype=int)
for i in range(a.shape[0]):                     # rows
    for j in range(b.shape[1]):                 # Columns
        result[i][j]=a[i][j] + b[i][j]
for o in result:
    print(o)


result=np.zeros_like(a)   
for i,j in np.ndindex(a.shape):                   # np.nindex() gives all i,j easy to loop matrix elements.
    result[i,j]=a[i,j] * b[i,j]
    
print(result)

asc=np.nditer(a)
print(asc)

for x in asc:
    print(x)                     # np.nditer() is the best way to loop through all elements one by one.


#----Normal concepts of loop wise calculations and numpy wise and both for just known about differences.
