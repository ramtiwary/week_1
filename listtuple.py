def last(n):
    return n[-1]
def sorted_list_last(tuples):
    return sorted(tuples, key=last)
print(sorted_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
