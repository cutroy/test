import pandas as pd
import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


from sklearn.model_selection import train_test_split



seed = random.randint(0,1000000)
data = pd.read_csv('train.csv')
data.fillna(0, inplace=True)
df = data[['Тип_жилья','Город', 'Площадь', 'Этаж', 'Размер_участка', 'Кво_комнат', 'Цена']]
X = data[['Кво_комнат']]
Y = data['Цена']
train_x, test_x, train_y, test_y = train_test_split(X,Y, test_size =0.25,random_state=seed)
#plt.figure(figsize=(5,5))
#plt.scatter(train_x,train_y)
lr=LinearRegression()
lr.fit(train_x, train_y)
k = lr.coef_[0]
b=lr.intercept_

def f_line(x):
    return k*x+b

x_ln = [1,60]
y_ln = [int(f_line(i)) for i in x_ln]
#plt.plot(x_ln,y_ln)
#plt.show()

y_test_pr = lr.predict(test_x)
print(k,b)