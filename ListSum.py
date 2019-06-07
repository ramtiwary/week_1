lst = []
num = int(input('how many numbers: '))
for n in range(num):
    nums = int(input('Enter Number '))
    lst.append(nums)
print("Sum of Entered numbers:",sum(lst))
