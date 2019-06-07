#1.create a pie chart of the popularity of programming Languages.
import matplotlib.pyplot as plt

languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
Popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
explode = (0.1,0,0,0,0,0)
plt.pie(Popularity, explode=explode, labels=languages,colors=colors,
autopct='%1.1f%%',shadow=True,startangle=140)
plt.axis('equal')
plt.show()
#2.create a pie chart with a title of the popularity of programming Languages
#import matplotlib.pyplot as plt
languages = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
Popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]
explode = (0.1,0,0,0,0,0)
plt.pie(Popularity, explode=explode, labels=languages,colors=colors,
autopct='%1.1f%%',shadow=True,startangle=140)
plt.axis('equal')
plt.title("PopularitY of Programming Language\n" + "Worldwide, Oct 2018 compared to a year ago", bbox={'facecolor':'0.8', 'pad':5})
plt.show()
#3.a pie chart of gold medal achievements of five most successful countries in 2016 Summer Olympics.
#  Read the data from a csv file
import pandas as pd
df = pd.read_csv('medal.csv')
country_data = df["country"]
medal_data = df["gold medal"]
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#8c564b"]
explode = [0.1,0,0,0,0]
plt.pie(medal_data, lables=country_data, explode = explode, colors=colors,
autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Gold medal achievements of five most successful\n"+"countries in 2016 Summer Olympics")
plt.show()    