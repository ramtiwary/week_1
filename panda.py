#1. one-dimensional array-like object
#containing an array of data using Pandas module
import pandas as pd
ds = pd.Series([1,2,3,4,5,6])
print(ds)

#2. convert a Panda module Series to Python list and it's type
dse = pd.Series([4,8,12,16,20])
print("Panda Series and its type")
print(dse)
print(type(dse))
print("Python list and its type")
print(dse.tolist())
print(type(dse.tolist()))

#3 add, subtract, multiple and divide two Pandas Series
ds1 = pd.Series([1,3,5,7,9])
ds2 = pd.Series([2,4,6,8,10])
print("Addition of two panda Series")
ds3 = ds1 + ds2
print(ds3)
print("Substraction of two panda Series")
ds3 = ds1 - ds2
print(ds3)
print("Multiplication of two panda Series")
ds3 = ds1 * ds2
print(ds3)
print("Division of two panda Series")
ds3 = ds1 / ds2
print(ds3)
#4. get the powers of an array values element-wise
import numpy as np
Y = np.arange(7)
print("print Legacy array: ")
print(Y)
print("powers of an array values element-wise: ")
print(np.power(Y,3))
#5.DataFrame from a specified dictionary
#data which has the index labels
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael',
'Matthew', 'Laura', 'Kevin', 'Jonas'],
'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
print(df)