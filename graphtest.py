import seaborn as sns
import matplotlib.pyplot as plt
import math

x = []
y =[]
for i in range(-10,11):
    x.append(i)
    y.append(i**2+i**0.5-10)


sns.lineplot(x=x, y=y)
plt.show()