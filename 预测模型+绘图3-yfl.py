import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import csv
fname=['Critically Endangered.csv','Endangered.csv','Vulnerable.csv']
with open('Critically Endangered.csv') as file:
    reader=csv.reader(file,delimiter=',')
    header=next(reader)

for i in fname:
    data=pd.read_csv(i,thousands=',')
    xTrain=np.array(data['Year'])[:,np.newaxis]
    yuce=[]
    for j in range(1,len(header)):
        yTrain=np.array(data[header[j]])
        # 创建模型对象
        model = LinearRegression()
        # 根据训练数据拟合出直线(以得到假设函数)
        hypothesis = model.fit(xTrain, yTrain)
        # 截距
        # print("theta0=", hypothesis.intercept_)
        # # 斜率
        # print("theta1=", hypothesis.coef_)
        xNew = np.array([2023,2024,2025,2026,2027])[:, np.newaxis]
        yNew = np.ceil(model.predict(xNew)).astype(int)
        # print("预测新数据：", xNew)
        # print("预测结果：", yNew)
        # print(model.score(xTrain,yTrain))
        yuce.append(yNew.tolist())
        # def initPlot():
        #     # 先准备好一块画布
        #     plt.figure()
        #     # 生成图表的名字
        #     name='2023~2028 '+header[j]
        #     plt.title(name)
        #     # 横坐标名字
        #     plt.xlabel('year')
        #     # 纵坐标名字
        #     plt.ylabel('number')
        #     # 表内有栅格（不想要栅格把此行注释掉即可）
        #     plt.grid(True)
        #     return plt
        # plt = initPlot()  # 画图
        # # k是黑色，.是以点作为图上显示
        # plt.plot(xTrain, yTrain, 'k.')
        # # 画出通过这些点的连续直线
        # plt.plot(xNew, yNew, 'g--')
        # # 将图显示出来
        # plt.show()
    species=['Mammals','Birds','Reptiles','Amphibians','Fishes','Insects','Molluscs','Other invertebrates','Plants','Fungi & protists','Total']
    yuce=np.array(yuce)
    year=[2023,2024,2025,2026,2027]
    x = np.arange(2023, 2028)
    # 将所有大于2000的点替换为NaN
    thres = 2000
    yuce_filt = [np.where(yuce[k] > thres, np.nan, yuce[k]) for k in range(len(species))]
    yuce_large = [np.where(yuce[k] <= thres, np.nan, yuce[k]) for k in range(len(species))]

    # 创建多个子图
    fig, axes = plt.subplots(nrows=2, sharex=True,figsize=(10,18))
    # 绘制小于3000的数据
    for k in range(len(species)):
        axes[0].plot(year, yuce_filt[k], label=species[k])
        for i, val in enumerate(yuce_filt[k]):
            if not np.isnan(val):
                axes[0].annotate(str(val), xy=(x[i], val), xytext=(x[i]+0.1, val+0.5))

    # 绘制大于3000的数据
    for k in range(len(species)):
        axes[1].plot(year, yuce_large[k], label=species[k])
        for i, val in enumerate(yuce_large[k]):
            if not np.isnan(val):
                axes[1].annotate(str(val), xy=(x[i], val), xytext=(x[i]+0.1, val+0.5))

    # 添加图例
    axes[0].legend(loc='upper right')
    axes[1].legend(loc='upper right')

    # 显示图形
    plt.show()