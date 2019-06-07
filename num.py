#1.convert a list of numeric value into a one-dimensional array
import numpy as np
OgList = [12.23, 13.32, 100, 36.32]
print("Original List: ",OgList)
One_Dim_narray = np.array(OgList)
#a = np.array(OgList)
print("One-dimensional numpy array: ",One_Dim_narray)
#2. 3x3 matrix with values ranging from 2 to 10
x = np.arange(2,11).reshape(3,3)
print(x)
#3. create a null vector of size 10 and update sixth value to 11
b = np.zeros(10)
print(b)
c = int(input("Enter number: "))
b[6] = c
print(b)
#4. reverse an array (first element becomes last)
from array import *
Oarr = array('i', [12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37])
print("Original Array: " +str(Oarr))
Oarr.reverse()
print("Reverse Array: ")
print(str(Oarr))
#5. 2d array with 1 on the border and 0 inside
d = np.ones((5,5))
print("Original Array :")
print(d)
d[1:-1,1:-1] = 0
print("1 on the border and 0 inside in the array")
print(d)
