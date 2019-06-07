#1.draw a line with suitable label in the x axis, y axis and a title
import pandas as pd
import matplotlib.pyplot as plt
X = range(1,50)
Y = [value * 3 for value in X]
print("Values of X: ")
print(*range(1,50))
print("Values of Y(thrice of X):")
print(Y)
plt.plot(X,Y)
plt.xlabel('x - axis')
plt.xlabel('y - axis')
plt.title('Draw a Line')
plt.show()

#2. draw a line using given axis values with suitable label in the x axis,y axis and a title
x = [1,2,3]
y = [2,4,1]
plt.plot(x, y)
plt.xlabel('x - axis')
plt.ylabel('y - axis')
plt.title('Sample graph!')
plt.show()

#3.draw a line using given axis values taken from a text file, with
#suitable label in the x axis, y axis and a title
# with open("/home/admin1/Documents/text.txt") as f:
#     data = f.read()
# data = data.split('\n')
# x = [row.split(' ')[0] for row in data]
# y = [row.split(' ')[1] for row in data]
# plt.plot(x, y)
# plt.xlabel('x - axis')
# plt.ylabel('y - axis')
# plt.title('Sample graph!')
# plt.show()

#4. draw line charts of the financial data of Alphabet Inc. between
#October 3, 2016 to October 7, 2016
df = pd.read_csv('/home/admin1/Documents/fdata.csv', sep=',', parse_dates=True,index_col=0)
df.plot()
plt.show()

#5. plot two or more lines on same plot with suitable legends of each
#line
x1 = [10,20,30]
y1 = [20,40,10]
plt.plot(x1, y1, label='line 1')
x2 = [10,20,30]
y2 = [40,10,30]
plt.plot(x2, y2, label='line 2')
plt.xlabel('x - axis ')
plt.ylabel('y - axis')
plt.title('Two or more lines on same plot with suitable legends')
plt.legend()
plt.show()

#6.plot two or more lines with legends, different widths and colors
x3 = [10,20,30]
y3 = [20,40,10]
x4 = [10,20,30]
y4 = [40,10,30]
plt.xlabel('x - axis ')
plt.ylabel('y - axis')
plt.title('Two or more lines with legends, different widths and colors')
plt.plot(x1, y1, color='blue', linewidth = 3, label ='line1-width-3')
plt.plot(x2, y2, color='red', linewidth = 5, label ='line2-width-5')
plt.legend()
plt.show()

