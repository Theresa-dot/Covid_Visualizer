import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from time import sleep


data = pd.read_csv('teddy.csv')

Y = data.iloc[61:,1].values
R = data.iloc[61:,3].values
D = data.iloc[61:,5].values
X = data.iloc[61:,0]


axes = plt.axes()
axes.grid(linewidth = 0.4, color = "#28a9ff")
axes.set_facecolor("white")
axes.set_xlabel('\n',size=20,color='#4bb4f2')
axes.set_ylabel("total cases\n",size=20,color="#4bb4f2")

plt.xticks(rotation='vertical',size=20,color='black')
plt.yticks(size=20, color='black')
plt.tick_params(size=20,color='black')

for i,j in zip(X,Y):
	axes.annotate(str(j),xy=(i,j+100),color='black',size='13')

axes.annotate('second lockdown', xy =(15.2, 860), 
             xytext =(20, 500),
             size='25', 
             arrowprops = dict(color ='black', 
                               shrink = 0.05))
plt.title('COVID-19 DAILY CONFIRMED',size=50,color='#28a9ff')


axes.plot(X,Y,
	color="#00FFFF",
	marker="o",
	linewidth=4,
	markersize=15,
	markeredgecolor="#035E9B")

plt.show()