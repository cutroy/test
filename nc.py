import numpy as np
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
#create a dataset
np.random.seed(0)
sns.set_theme()
data=pd.read_csv('data_set.csv')
df = pd.DataFrame(data,columns=['day','time','val'])
df=df.pivot(index='day', columns='time', values='val')
plt.subplots(figsize=(15, 8))
sns.heatmap(data=df, annot=True,cmap=sns.cubehelix_palette(as_cmap=True),vmin=0, vmax=150)
plt.show()