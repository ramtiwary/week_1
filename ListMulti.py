def multiplylist (mylist):
    result = 1
    for x in mylist:
        result = result * x
    return result
# lists
list1 = [1,2,3]
list2 = [4,5,6]
print(multiplylist(list1))
print(multiplylist(list2))

# using numpy prod
#import numpy
#list3 = [3,2,1]
#list4 = [4,5,6]
#result1 = numpy.prod(list3)
#result2 = numpy.prod(list4)
#print(result1)
#print(result2)

