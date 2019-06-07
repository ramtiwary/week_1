# using list numbers
list1 = [12,5,70,98]
print("Smallest number in the list: ",min(list1))
print("Greatest number in the list: ",max(list1))

#using user inputs
lst = []
num = int(input("how many elements you want: "))
for x in range(1,num+1):
    elem = int(input("Enter Element: "))
    lst.append(elem)
print("Smallest element in the list :",min(lst))