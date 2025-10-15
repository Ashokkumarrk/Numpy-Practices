import numpy as np
a1=np.zeros((3,3))
print(a1)

a2=np.ones((3,3))
print(a2)

a3=np.eye(3,3)
print(a3)

a4=np.arange(0,10,2)
print(a4)

a5=np.array([10,20,30])
print(a5[2])

a6=np.array([[1,2],[3,4]])
print(a6)
a6[1,1]
print(a6[1,1])
print(a6[0,0])
print(a6[0,1])
print(a6[1,0])

a7 = np.full((3,3),5)
print(a7)

a8=np.linspace(0,10,3)
print(a8)

a9=np.random.randint(1,10,size=(2,3))
print(a9)

b1=np.random.rand(2,3)
print(b1)

b2=np.diag((3,4))
print(b2)

b3=np.zeros_like(a6)
print(b3)

b4=np.ones_like(a6)
print(b4)



