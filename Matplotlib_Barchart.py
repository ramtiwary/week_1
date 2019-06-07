#1.Bar chart of the popularity of programming
#Languages
import matplotlib.pyplot as plt
x = ['Java','Python','PHP','JavaScript','C#','C++']
Popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x_pos = [i for i, _ in enumerate(x)]
plt.bar(x_pos, Popularity, color=(0.4,0.6,0.8,1.0), edgecolor ='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2018 compared to a year ago")
plt.xticks(x_pos,x)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()
#2. To display a horizontal bar chart of the popularity of
#programming Languages
x1 = ['Java','Python','PHP','JavaScript','C#','C++']
Popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x1_pos = [i for i, _ in enumerate(x1)]
plt.barh(x_pos, Popularity, color=(0.4,0.6,0.8,1.0), edgecolor ='blue')
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2018 compared to a year ago")
plt.yticks(x_pos,x1)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()
#3. To display a bar chart of the popularity of programming
#Languages. Use uniform color 
x2 = ['Java','Python','PHP','JavaScript','C#','C++']
Popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x2_pos = [i for i, _ in enumerate(x2)]
plt.bar(x2_pos, Popularity, color=(0.4,0.6,0.8,1.0))
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2018 compared to a year ago")
plt.xticks(x2_pos,x2)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()
#4.To display a bar chart of the popularity of programming
#Languages. Use different color for each bar
x3 = ['Java','Python','PHP','JavaScript','C#','C++']
Popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x3_pos = [i for i, _ in enumerate(x2)]
plt.bar(x3_pos, Popularity, color=['red','green','blue','black', 'yellow','cyan'])
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2018 compared to a year ago")
plt.xticks(x3_pos,x3)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()
#5. to display a bar chart of the popularity of programming Languages.
#  Attach a text label above each bar displaying its popularity (float value)
x4 = ['Java','Python','PHP','JavaScript','C#','C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
x4_pos = [i for i, _ in enumerate(x4)]
fig, ax = plt.subplots()
rects1 = ax.bar(x4_pos, popularity, color='b')
plt.bar(x4_pos, Popularity, color=['red','green','blue','black', 'yellow','cyan'])
plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2018 compared to a year ago")
plt.xticks(x4_pos,x4)
plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='red')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,'%f' % float(height), ha ="center", va ="bottom")
autolabel(rects1)

plt.show()




