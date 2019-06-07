# To draw a scatter graph taking a random distribution in X and Y and
# plotted against each other
import matplotlib.pyplot as plt
#import pandas as pd
import numpy as np
import math
import random
from pylab import randn

x = randn(200)
y = randn(200)
plt.scatter(x, y, color='r')
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
#2.To draw a scatter plot with empty circles taking a random distribution
#in X and Y and plotted against each other

x1 = np.random.randn(50)
y1 = np.random.randn(50)
plt.scatter(x1,y1, s=70,facecolors='none',edgecolors='g')
plt.xlabel("x1")
plt.ylabel("y1")
plt.show()
#3. To draw a scatter plot using random distributions to generate balls of different sizes

no_of_balls = 25
x = [random.triangular() for i in range(no_of_balls)]
y = [random.gauss(0.5,0.25) for i in range(no_of_balls)]
colors = [random.randint(1,4) for i in range(no_of_balls)]
areas = [math.pi * random.randint(5, 15)**2 for i in range (no_of_balls)]
plt.figure()
plt.scatter(x, y, s=areas, c=colors, alpha=0.85)
plt.axis([0.0,1.0,0.0,1.0])
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
#4.to draw a scatter plot comparing two subject marks of Mathematics
#and Science. Use marks of 10 students

math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.scatter(marks_range, math_marks, label='Math Marks', color='r')
plt.scatter(marks_range,science_marks, label='Science Marks',color='g')
plt.title('Scatter Plot')
plt.xlabel('Marks Range')
plt.ylabel('Marks Scored')
plt.legend()
plt.show()
#5. To draw a scatter plot for three different groups camparing weights
#and heights
#import numpy as np
weight1=[67,57.2,59.6,59.64,55.8,61.2,60.45,61,56.23,56]
height1=[101.7,197.6,98.3,125.1,113.7,157.7,136,148.9,125.3,114.9] 
weight2=[61.9,64,62.1,64.2,62.3,65.4,62.4,61.4,62.5,63.6]
height2=[152.8,155.3,135.1,125.2,151.3,135,182.2,195.9,165.1,125.1] 
weight3=[68.2,67.2,68.4,68.7,71,71.3,70.8,70,71.1,71.7]
height3=[165.8,170.9,192.8,135.4,161.4,136.1,167.1,235.1,181.1,177.3]
weight=np.concatenate((weight1,weight2,weight3))
height=np.concatenate((height1,height2,height3))
plt.scatter(weight, height, marker = '*', color=['red','green','blue'])
plt.xlabel('weight', fontsize=16)
plt.ylabel('height', fontsize=16)
plt.title('Group wise Weight vs Height scatter plot',fontsize=20)
plt.show()