import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据
data = pd.read_csv('huitu.csv')

sns.set()
fig, ax = plt.subplots(figsize=(30, 18))
sns.heatmap(data.pivot_table(index='Disaster Type', columns='Year', values='Times', aggfunc='sum'), cmap='Reds',annot=True,fmt='.2f',ax=ax)
plt.savefig('heatmap.png')
