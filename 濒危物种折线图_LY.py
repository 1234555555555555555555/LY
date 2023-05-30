#1996年到2022年濒危物种数量的变化
import pandas as pd
import matplotlib.pyplot as plt
y_lable=[]
x_lable=[]
fnames=["/home/mw/input/endangered3545/Critically Endangered.csv","/home/mw/input/endangered3545/Endangered.csv","/home/mw/input/endangered3545/Vulnerable.csv"]
for i in fnames:
    #将1996/1998分开并添加列
    data = pd.read_csv(i,encoding="utf-8",thousands=',')
    s=1998
    data["Year"].loc[21]=s
    data.to_csv(i, index=False, header=True)
    m=data.loc[21]
    data.loc[22]=m
    data.to_csv(i, index=False, header=True)
    s1=1996
    data["Year"].loc[22]=s1
    data.to_csv(i, index=False, header=True)
    x_lable=data["Year"]
    y_lable.append(data["TOTAL"])
    #print(data["Year"])
    #scaler = MinMaxScaler()
    # 将数据进行归一化处理
   # scaled_data = scaler.fit_transform(data)
    #print(scaled_data)
def show():
    plt.figure(figsize=(20, 10), dpi=100)
    plt.plot(x_lable, y_lable[0], c='red', label="极度濒危物种")
    plt.plot(x_lable, y_lable[1], c='green', linestyle='--', label="濒危物种")
    plt.plot(x_lable, y_lable[2], c='blue', linestyle='-.', label="易濒危物种")
    plt.scatter(x_lable, y_lable[0], c='red')
    plt.scatter(x_lable, y_lable[1], c='green')
    plt.scatter(x_lable, y_lable[2], c='blue')
    plt.legend(loc='best')
    plt.yticks(range(0, 10, 22))
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.xlabel("年份", fontdict={'size': 16})
    plt.ylabel("濒危物种数量", fontdict={'size': 16})
    plt.title("1996年到2022年濒危物种数量的变化", fontdict={'size': 20})
    plt.show()
show()
