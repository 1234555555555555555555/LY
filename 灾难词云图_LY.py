#灾难词云图
import wordcloud
import matplotlib.pyplot as plt
# 读取文本文件
filename="/home/mw/input/disaster2792/Disaster.csv"
data = pd.read_csv(filename,encoding="utf-8")
text1=data["Disaster Type"]
text=""
for i in text1:
    text+=" "+i

# 创建词云对象
wc = wordcloud.WordCloud(width=1600, height=1200, background_color='white',collocations=False)
# 生成词云图
wc.generate(text)
# 显示词云图
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()
