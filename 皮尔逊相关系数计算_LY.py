from collections import Counter
import pandas as pd
import textwrap
import matplotlib.pyplot as plt
import csv
import numpy as np
plt.rcParams['font.sans-serif'] = ['SimHei']
fname=["/home/mw/input/endangered3545/Vulnerable.csv","/home/mw/input/endangered3545/Endangered.csv","/home/mw/input/endangered3545/Critically Endangered.csv"]
file=pd.read_csv('output.csv')
from collections import defaultdict
# 创建一个字典，用于存储每种灾难类型的发生次数
disaster_counts = defaultdict(lambda: [0] * 21)
# 循环遍历所有的年份，统计每种灾难类型的发生次数
for k in range(21):
    year = 2002 + k
    data = file.loc[(file['Start Year'] == year)]
    data_list = data['Disaster Type'].values.tolist()
    result = Counter(data_list)
    for disaster_type, count in result.items():
        disaster_counts[disaster_type][k] = count
# 创建一个列表，用于存储按照灾难类型统计的结果
disaster_counts_list = []
# 循环遍历所有的灾难类型，获取每种灾难类型在每个年份中的发生次数
for disaster_type in disaster_counts.keys():
    counts = disaster_counts[disaster_type]
    disaster_counts_list.append([disaster_type] + counts)
# 输出统计的结果
Y_lable=[]
X=[]
for i in fname:
    file1=pd.read_csv(i,thousands=",")
    Y=file1["TOTAL"]
    Y=np.array(Y[2:]).tolist()
    temp=[]
    for row in disaster_counts_list:
        s=row[0]
        if s not in X:
            X.append(s)
        row1=row[1:]
        del(row1[3])
        corr = np.corrcoef(row1, Y)[0, 1]#求皮尔逊相关系数
        corr=round(corr,2)
        temp.append(corr)
        #print(s,corr)
    Y_lable.append(temp)
dictionary = dict(zip(X, Y_lable[0]))
dictionary=sorted(dictionary.items(),key=lambda x:x[1],reverse=True)
dictionary1 = dict(zip(X, Y_lable[1]))
dictionary1=sorted(dictionary1.items(),key=lambda x:x[1],reverse=True)
dictionary2 = dict(zip(X, Y_lable[2]))
dictionary2=sorted(dictionary2.items(),key=lambda x:x[1],reverse=True)
print(dictionary2)
X=X[2:11]
Y_lable[0]=Y_lable[0][2:11]
Y_lable[1]=Y_lable[1][2:11]
Y_lable[2]=Y_lable[2][2:11]
# 绘制散点图
fig, ax = plt.subplots(figsize=(17, 12))
ax.scatter(X, Y_lable[0], alpha=0.5, color='r', s=100, label='Vulnerable')
ax.scatter(X, Y_lable[1], alpha=0.5, color='g', s=100, label='Endangered')
ax.scatter(X, Y_lable[2], alpha=0.5, color='b', s=100, label='Critically Endangered')
# 添加数字标签
for i in range(len(X)):
    ax.annotate(str(Y_lable[0][i]), (X[i], Y_lable[0][i]), color='r', ha='center', va='bottom')
    ax.annotate(str(Y_lable[1][i]), (X[i], Y_lable[1][i]), color='g', ha='center', va='bottom')
    ax.annotate(str(Y_lable[2][i]), (X[i], Y_lable[2][i]), color='b', ha='center', va='bottom')
# 设置横纵坐标标签和标题
plt.xlabel('disaster type',fontsize=14)
plt.ylabel('Pearson coefficient',fontsize=14)
plt.title('Correlation coefficient between the number of disasters and the number of endangered species')
# 添加图例
plt.legend(loc='best', bbox_to_anchor=(0.5, 1), ncol=3)
# 显示图形
plt.show()

