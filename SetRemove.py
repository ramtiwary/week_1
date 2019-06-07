num_set = set([0,1,2,3,4,5,6])
#Remove items form the set
num_set.pop()
print(num_set)
num_set.pop()
print(num_set)
#Remove item form the set based on index
num_set.discard(2)
print(num_set)

#intersection of set
setx = set([1,2,4])
sety = set([1,2,6])
setz = setx & sety
print(setz)