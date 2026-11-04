# ESE5023\_Assignments\_12632748

Comments on HW1 Liyl(101/100)

You write your solving thoughts in detail in .pdf, good!(+2p)
Only .ipynb also is OK, you DON'T change into .py. Thanks.

1-2: A small error,"M3\[i,j]=M1\[i,k]\*M2\[k,j]" should be changed as M3\[i,j]+=M1\[i,k]\*M2\[k,j].
Need corrsponding rows and columns multiple and add. (-3p)

1-3: Good job!(+2p)

1-4: you listed all your calculated results ,that's right.
But there is a more smart method.Reverse thinking, for x,
if x is even, divide by 2; if x is odd, make it even first(minus 1),
then divide. if Please reference:
def Least\_moves(x):
moves = 0
while x > 1:
if x % 2 == 0:
x = x // 2
else:
x = x - 1
moves = moves + 1
print(moves)
print("Least\_moves(10):")
Least\_moves(10)

1-5:
5.1 Good job! YOU ARE SO SMART!(+2p)
5.2 You don't plot.(-2p)





HW2 from Lijh（88/100）

1.1.2的图像纵坐标无标注，可读性差（-2）



2\.日期处理采用字符串拆分方式，未转换为标准日期时间格式，不利于后续时间序列分析



3.3.5 应筛选 NAME == 'MANGKHUT' 且 SEASON == 2018，否则可能混入其他年份的数据。3.10 建议使用 resample('YE').mean() 计算年度平均距平，而不是 .sum()。另外，3.8和3.9应统一闰年与非闰年的 DOY。



4\.能够完成数据读取、清洗、时间序列绘图和基本统计分析，但统计分析较为简单，建议对内容进行丰富

你的代码中基本上没有注释，AI生成的痕迹非常明显，并且pdf内没有说明借助了AI工具（-10）

