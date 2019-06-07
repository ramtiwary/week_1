# Tuple colon
from copy import deepcopy
tuplex = ["Hi",10,[],True]
print(tuplex)

tuplex_colon = deepcopy(tuplex)
tuplex_colon[2].append(40)
print(tuplex_colon)

# repeated Item in Tuple
tuplex = 2,1,2,3,4,2,5,3,3,3
print(tuplex)
count = tuplex.count(3)
print(count)
