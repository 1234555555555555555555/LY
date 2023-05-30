from collections import Counter
import pandas as pd
import textwrap
import matplotlib.pyplot as plt
import csv

file=pd.read_csv('output.csv')
f=open('huitu.csv',"w",newline='')
csv_write=csv.writer(f)
header=['Year','Disaster Type','Times']
csv_write.writerow(header)
for k in range(21):
    line=[]
    year=2002+k
    data=file.loc[(file['Start Year']==year)]
    # print(data['Disaster Type'])
    data_list=data['Disaster Type'].values.tolist()
    # print(data_list)
    result=Counter(data_list)
    x = list(result.keys())
    y = list(result.values())
    for l in range(len(x)):
        line=[year,x[l],y[l]]
        csv_write.writerow(line)
    # line.to_csv('huitu.csv',index=False,header=not os.path.exists('huitu.csv'), mode='a', encoding='utf-8-sig')
    plt.bar(x, y)
    for i, v in enumerate(y):
        plt.annotate(str(v), xy=(i, v), ha='center', va='bottom')
    # 自动换行输出横坐标标签
    x = [textwrap.fill(label, 5) for label in x]
    plt.xticks(range(len(x)), x)
    name=str(k)+'.png'
    plt.savefig(name)
    plt.show()
f.close()