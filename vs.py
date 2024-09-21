import numpy as np
import pandas as pd 
import random
import seaborn as sns
import matplotlib.pyplot as plt
#create a dataset
np.random.seed(0)
mas_day = []
mas_time=[]
check =[]
mas_sales=[]
for i in range(0,15):
    a=random.choice(['Mon','Tue','Wed','Thu','Fri','Sat','Sun'])
    b=random.choice(['00:00-4:00', '4:00-8:00', '8:00-12:00', '12:00-16:00', '16:00-18:00', '18:00-22:00', '22:00-23:59'])
    c=random.randint(1, 100)
    a=str(a)
    b=str(b)
    c=int(c)
    if [a,b,c] not in check:
        mas_day.append(a)
        mas_time.append(b)
        mas_sales.append(c)
        check.append([a,b,c])
        print([a,b,c])
data = {'day': mas_day,
 'time': mas_time,
 'sales': mas_sales
 }
print(data)

df = pd.DataFrame(data,columns=['day','sales','sales'])
print(df)
df = df.pivot(index='day', columns='sales', values='sales')
print(df)
# sns.heatmap(df, linewidths=.5,annot=True) 
# plt.show()