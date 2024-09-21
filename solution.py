import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_percentage_error
from sklearn.neighbors import KNeighborsRegressor
import random
from sklearn.model_selection import train_test_split
seed = random.randint(0,1000000)

data = pd.read_csv('train.csv')
data_test = pd.read_csv('public_test.csv')
data.fillna(0, inplace=True)
print(data.columns)
X=data[[ 'Площадь','Кво_комнат','Этаж','Нлч_гаража','Кво_фото']]
Y = data['Цена']
XTRAIN,XTEST, YTRAIN, YTEST = train_test_split(X,Y, test_size=0.1, random_state=seed)
knn = KNeighborsRegressor(n_neighbors=128)
knn.fit(XTRAIN, YTRAIN)
x_test = data_test[[ 'Площадь', 'Кво_комнат','Этаж','Нлч_гаража','Кво_фото']]
x_test.fillna(0, inplace=True)
y_pred = knn.predict(x_test)
data_ans_to_csv =[]
for i in range(len(data_test)):
    data_ans_to_csv.append([int(data_test['id'][i]), int(y_pred[i])])
with open('public_sample_submission_seed_0.csv','w',newline='') as f:
    csv.writer(f).writerow(['id', 'Цена'])
    csv.writer(f).writerows(data_ans_to_csv)