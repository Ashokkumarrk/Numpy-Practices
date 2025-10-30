import numpy as np
arr=np.array([10,20,30,40,50])
print(arr[0])
print(arr[1])
print(arr[-1])
arr=np.array([[10,20,30],
              [40,50,60],
              [70,80,90]])
print(arr[0,1])
print(arr[2,2])


##slicing----
print(arr[0:1])
print(arr[:3])
print(arr[:])
print(arr[0:1])
print(arr[1:2])
print(arr[1:0])
print(arr[1:2])

Reshaping and Resizing:

arr=np.array([1,4,5,8])
ass=arr.reshape(2,2)                                # for reshaping process
print(ass)
ass=arr.reshape(4)                                   # For return to the original value.
print(ass)
abc=arr.reshape(2,1,2)
print(abc)
efg=arr.reshape(-1,2)                              # for unknown size and manage 
print(efg)
ars=np.array([1,2,3,4,5,6])
print(ars.reshape(3,2))
ars.resize(3,3)                                     # for resize its constantly Inplace = True
print(ars)

Stacking:
arr=np.arange(5,10,2)
print(arr)
a=np.array([1,2,3])
b=np.array([3,5,6])
print(np.stack((a,b),axis=0))                            # for merging option Stack
print(np.stack((a,b),axis=1))
a=np.array([[1,2,3],
            [3,5,6]])
b=np.array([[7,8,9],
            [4,7,8]])
c=np.array([[10,11,12],
            [13,24,15]])
print(np.stack((a,b),axis=0))
print(np.stack((a,b),axis=1))                  # 2 Dimension array stack          # stack always become 1d +.
print(np.stack((a,b),axis=2))
print(np.stack((a,b,c),axis=2))

NUMPY Arithmetic operations:
Addition:

a=np.array([1,5,6,])
b=np.array([5])
c=np.array([7,8,9])
add_ab=np.add(a,b)    
print(add_ab)

Subraction:
sub_ab=np.subtract(a,b)
print(sub_ab)

Multiply:
mul_ab=np.multiply(a,b)
print(mul_ab)

Division:
div_ab=np.divide(a,b)
print(div_ab)

Exponentation:
power_asb=np.power(a,b)
print(power_asb)

Modulus Operation:
mod_ab=np.mod(a,b)        # Reminder
print(mod_ab)

All Arithmetic operations will must be on same shape.

Matrix Manipulation arithmetic operations:
a=np.array([[1,2],[3,4]])
b=np.array([[5,6],[7,8]])
add_ab=np.add(a,b).T
print(add_ab)
sub_ab=np.subtract(b,a)
print(sub_ab)
mul_ab=np.multiply(a,b)
print(mul_ab)
dot_ab=np.dot(a,b)
print(dot_ab)
sqrt_ab=np.sqrt(a)
print(sqrt_ab)
sum_a=np.sum(a)  
print(sum_a)
um_ab=np.sum(a,axis=0)   #axis =1 column 
print(um_ab)

Masking
a=[3,5,np.nan,2,np.inf]
b=np.sum(a)                          
print(b)
import numpy.ma as mp
b=mp.array(a,mask=[0,0,1,0,1],hard_mask=True)
print(b)
print(mp.sum(b))
b[2]=mp.masked_all_like

print(b)
print(b[1])
print(~b.mask)
mas=b[~ b.mask]
print(mas)
ash=np.random.randint(0,10,(2,3))
print(ash)