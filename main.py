# 导入数据分析包：numpy（科学计算）、pandas（处理数据框）和 matplotlib/seaborn(可视化)
import numpy as np
import pandas as pd
#表示调用Matplotlib子类pyplot绘图，并as重命名为plt，方便代码调用。
import matplotlib.pyplot as plt
import seaborn as sns
# 导入数据：世界杯成绩汇总表
worldcup_chengji = pd.read_csv('WorldCupsSummary.csv')
#print(worldcup_chengji)
# 统一"Germany FR"和"Germany"  归一化
worldcup_chengji = worldcup_chengji.replace(['Germany FR'],'Germany')
#print(worldcup_chengji)
# 设置全局绘图参数
font = {
  'weight': 'bold',
  'size': '20'}#字体为加粗、大小为20
plt.rc('font', **font)
fig, ax= plt.subplots(figsize=(12,8))  #figure图片大小



#世界杯参加人数绘制：
plt.title('Attendance Number') #表名称
worldcup_chengji.plot.scatter(x='Attendance',c="red",y='Year',ax=ax,zorder=2,s=100)  #绘制散点图 设置标签获取表格参加人数与年份，设置s散点大小
#去掉上下左右边框
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
#设置坐标轴标签 例如年份和人数 year
#ax.set_ylabel(None)
#ax.set_xlabel(None)
#ax.grid()添加网格线。颜色为绿
ax.grid(visible=True,color='blue')
#设置x与y主刻度
ax.tick_params(axis='both',which='major',labelsize=15,colors='gold')
ax.set_yticks(worldcup_chengji['Year'].tolist())#获取表格年份信息并设置y刻度
ax.set_xticks([500000,1000000,1500000,2000000,2500000,3000000,3500000,4000000])#设置x的刻度
#禁止科学计数
ax.ticklabel_format(style='plain')
#设置绘图区四个边框线上的的刻度线是否显示，此处不显示刻度
#plt.tick_params(bottom=False, left=False)
#plt.show()#打印在屏幕
plt.savefig('观众人数散点图')#表格的储存


fig, ax= plt.subplots(figsize=(12,8))
plt.title('Goals Number')
worldcup_chengji.plot.scatter(x='GoalsScored',y='Year',ax=ax,zorder=2,s=100)
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.grid(visible=True)
ax.tick_params(axis='both', which='major', labelsize=15)
ax.set_yticks(worldcup_chengji['Year'].tolist())
ax.set_xticks([50,75,100,125,150,175,200])
plt.tick_params(bottom=False, left=False)
#plt.savefig("进球总数散点图")
plt.show()


#国家冠军数
palette=['yellow','red','red','blue','purple','yellow','yellow','purple']  #调色板
fig, ax= plt.subplots(figsize=(16,8))#设置画布大小
plt.title('总冠军数')
sns.countplot(x = worldcup_chengji['Winner'], palette=palette,linewidth=2.5, edgecolor=".2")#调用成绩汇总表绘图
#去除上下左右边框
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)
#设置x，y轴标签
ax.set_ylabel("冠军数",fontsize=14)
ax.set_xlabel("国家",fontsize=14)
plt.rcParams['font.sans-serif']=["SimHei"]#防止中文乱码
#plt.tick_params(labelleft=False, left=False,labelsize=14)
#提取并显示条形图中的条形值
for i in ax.containers:
    plt.bar_label(i, fontsize=15)
#plt.savefig("获得冠军的国家")
plt.show()




#夺冠队伍所在大洲分布
index1 = worldcup_chengji['WinnerContinent'].value_counts().index.tolist()#标签文本，value_count用于数据表的计数
value1 = worldcup_chengji['WinnerContinent'].value_counts().values.tolist()#饼图的比例，格式为数组或占比的序列，决定扇形面积
palette = ['yellow', 'blue']
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))
sns.countplot(ax=ax[0], x=worldcup_chengji['WinnerContinent'], palette=palette, linewidth=2.5, edgecolor=".2")
ax[0].set_title('Champion Continent Numbers')
ax[0].spines['right'].set_visible(False)
ax[0].spines['top'].set_visible(False)
ax[0].spines['left'].set_visible(False)
ax[0].spines['bottom'].set_visible(False)
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].tick_params(labelleft=False, left=False, labelsize=14)
for i in ax[0].containers:
    ax[0].bar_label(i, fontsize=15);
plt.pie(value1, labels=index1, autopct='%.0f%%', colors=['blue', 'yellow'],
        wedgeprops={"edgecolor": "0", 'linewidth': 2.5,
                    'antialiased': True}, startangle=90, textprops={'fontsize': 20})
ax[1].set_title('Champion Continent Ratios', size=20, weight='bold');
#plt.imsave("夺冠大洲分布")
plt.show()



# 东道主夺冠概率
worldcup_chengji['HostWinner']= worldcup_chengji['HostCountry']== worldcup_chengji['Winner']#将winner和hostcountry作比较，赋值ture和false
index = worldcup_chengji['HostWinner'].value_counts().index.tolist()#标签文本，value_count用于数据表的计数
value = worldcup_chengji['HostWinner'].value_counts().values.tolist()#饼图的比例，格式为数组或占比的序列，决定扇形面积
palette = ['blue', 'yellow']
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(16, 8))
sns.countplot(ax=ax[0], x=worldcup_chengji['HostWinner'], palette=palette, linewidth=2.5, edgecolor=".2")
ax[0].set_title('Champion Number', size=20, weight='bold')
ax[0].spines['right'].set_visible(False)
ax[0].spines['top'].set_visible(False)
ax[0].spines['left'].set_visible(False)
ax[0].spines['bottom'].set_visible(False)
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].tick_params(labelleft=False, left=False, labelsize=25)
for i in ax[0].containers:
    ax[0].bar_label(i, fontsize=15);
plt.pie(value, labels=index, autopct='%.0f%%', colors=['blue', 'yellow'],
        wedgeprops={"edgecolor": "0", 'linewidth': 2.5,
                    'antialiased': True}, startangle=90, textprops={'fontsize': 20})
ax[1].set_title('Champion Probability', size=20, weight='bold');
#plt.savefig("东道主夺冠概率")
plt.show()



# 导入数据：比赛信息表
matches = pd.read_csv('WorldCupMatches.csv')
#print(matches)
# 中国队参加的比赛
#matches[(matches['Away Team Name'] == 'China PR') | (matches['Home Team Name'] == 'China PR')]
# 统一“联邦德国”和“德国”
matches = matches.replace(['Germany FR'],'Germany')
# 类型转化
matches['Home Team Goals']= matches['Home Team Goals'].astype(int)#astype()函数可用于转化dateframe某一列的数据类型
matches['Away Team Goals']= matches['Away Team Goals'].astype(int)
# 格式化比赛结果，如 3-2
matches['result'] = matches['Home Team Goals'].astype(str)+"-"+matches['Away Team Goals'].astype(str)
#比赛进球数分析
matches['total_goals'] = matches['Home Team Goals'] + matches['Away Team Goals']#总进球数
matches['VS'] = matches['Home Team Name'] + " VS " + matches['Away Team Name']#哪两个队比赛
top10_goals = matches.sort_values(by='total_goals', ascending=False)[:10]#排序函数，将total_goals排序
#print(top10_goals)
top10_goals['VS'] = top10_goals['Home Team Name'] + " VS " + top10_goals['Away Team Name']
top10_goals['total_goals_str'] = top10_goals['total_goals'].astype(str) + " goals scored" #总进球数
top10_goals['Home Team Goals'] = top10_goals['Home Team Goals'].astype(int)#主队进球数
top10_goals['Away Team Goals'] = top10_goals['Away Team Goals'].astype(int)#客队进球数
top10_goals['result'] = top10_goals['Home Team Goals'].astype(str) + "-" + top10_goals['Away Team Goals'].astype(str)#主客队的比分
plt.figure(figsize=(30, 30))
ax = sns.barplot(y=top10_goals['VS'], x=top10_goals['total_goals'])#绘制柱状图，调用vs数据并显示在y轴上
sns.despine(right=True)
plt.ylabel('Match',fontsize=25)
plt.xlabel('Goals',fontsize=25)
plt.yticks(size=15)
plt.xticks(size=15)
plt.title('Top10 Goals Match', size=20)
for i, s in enumerate("Stadium " + top10_goals['Stadium'] + ", Date: " + top10_goals['Datetime'] + "\n" +
                      top10_goals['total_goals_str'] + ", match result: " + top10_goals['result']):
    ax.text(1, i, s, fontsize=18, color='white', va='center')#体育场比赛时间等信息
plt.show()
#plt.savefig("比赛总进球数排名")













