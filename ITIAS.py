#!/usr/bin/env python
# -*- coding: utf-8 -*-
#2016-05-26 08:45:28 by sixer

import matplotlib.pyplot as pl #引入绘图库
import matplotlib as mpl
from matplotlib.ticker import MultipleLocator
import numpy as np #计算库
import xlwt


def printMatrix(matrix):  
    for i in range(matrix_size):  
        for j in range(matrix_size):  
            print matrix[i][j],  
        print '\n' 
def makeStatisticsGraphic(view_key,is_display_value,data_teacher,data_student,data_silent,data_tech):

	data_size=len(data_teacher)

	fig = pl.figure(2,figsize=(20,8))


	y = []#教师1
	z=[] #学生2
	a=[]#沉寂
	b=[]#技术
	t = []#横轴

	for i in xrange(0,data_size):
		y.append(data_teacher[i]);
		z.append(data_student[i]);
		a.append(data_silent[i]);
		b.append(data_tech[i]);
		t.append(i+1);
	
	x = np.arange(0, data_size, 1)#横坐标


	#print x
	#print y

	if view_key[0]==1:
		pl.plot(x, y,'-ro', label=u'教师语言')
		if is_display_value:
			for xy in zip(x,y):
    				pl.annotate(xy[1], xy=xy, xytext=(2,5),fontsize=7,fontproperties=zhfont,textcoords = 'offset points')
	if view_key[1]==1:
		pl.plot(x, z,'-go', label=u'学生语言')
		if is_display_value:
			for xz in zip(x,z):
    				pl.annotate(xz[1], xy=xz, xytext=(2,5),fontsize=7,fontproperties=zhfont,textcoords = 'offset points')
	if view_key[2]==1:
		pl.plot(x, a,'-bo', label=u'沉寂')
		if is_display_value:
			for xa in zip(x,a):
    				pl.annotate(xa[1], xy=xa, xytext=(2,5),fontsize=7,fontproperties=zhfont,textcoords = 'offset points')
	if view_key[3]==1:
		pl.plot(x, b,'-mo', label=u'技术')
		if is_display_value:
			for xb in zip(x,b):
    				pl.annotate(xb[1], xy=xb, xytext=(2,5),fontsize=7,fontproperties=zhfont,textcoords = 'offset points')

	
    
	
    		#pl.annotate(xa[1], xa=xa, xatext=(2,5),fontsize=7,textcoords = 'offset points')
    		#pl.annotate(xb[1], xb=xb, xbtext=(2,5),fontsize=7,textcoords = 'offset points')
    		#print xz

	
	#print np.max(x)
	
	
	ax = pl.gca()

	ax.xaxis.set_major_locator(MultipleLocator(1))
	ax.yaxis.set_major_locator( MultipleLocator(20) )#设置Y轴的密度

	

	# 设置两个坐标轴的范围
	pl.ylim(0,120)
	pl.xlim(1, np.max(x)-1)



	# 设置图的底边距
	pl.subplots_adjust(bottom = 0.15)

	pl.grid() #开启网格


	#获取当前x轴的label
	locs,labels = pl.xticks()
	#print locs
	#重新设置新的label,用时间t设置
	pl.xticks(locs, t, fontsize=8)

	#设置Y轴字体
	pl.yticks(fontsize=9,fontproperties=zhfont)


	pl.title(u'CCNU杨浩导师组ITIAS分析工具',fontsize=16,fontproperties=zhfont)  
	#pl.xlabel(u'日期')  
	pl.ylabel(u'比例',fontsize=8,fontproperties=zhfont) 

	pl.legend(fontsize=10,prop=zhfont)

	#自动调整label显示方式，如果太挤则倾斜显示
	fig.autofmt_xdate()

	#保存曲线为图片格式
	pl.savefig("./result.png")
	#pl.show()
	#print 'succ'
	pl.close(2)

def savaMatrix(matrix):
	#生成Excel
	book=xlwt.Workbook()
	sheet=book.add_sheet('matrix')
	for i in range(matrix_size):  
		for j in range(matrix_size):
			sheet.write(i,j,matrix[i][j])
			sheet.col(j).width = 256*5
	book.save("matrix.xls")

#设置字体
zhfont = mpl.font_manager.FontProperties(fname='font/Microsoft Yahei.ttf')
MultipleLocator.MAXTICKS = 100000
f = open("datas.txt","r")
for m in f:
	testData=m.split();

total_len=len(testData)#数据总个数
#print total_len
matrix_size=18#矩阵行列大小

matrix = [[0 for col in range(matrix_size)] for row in range(matrix_size)]

for i in range(0,total_len-1):
	x=int(testData[i]);
	y=int(testData[i+1]);

	if(x>matrix_size or y>matrix_size):#编码出错提示
		print "错误编码："+testData[i]+","+testData[i+1]
	matrix[x-1][y-1]+=1;

#printMatrix(matrix)
savaMatrix(matrix)

data=[]

for i in xrange(0,matrix_size):
	line_total=0;
	for j in xrange(0,matrix_size):
		line_total+=matrix[i][j]
	#print line_total
	data.append(str(round(line_total*100.0/(total_len-1),2))+"%")
#print data



teacher_percent=[]
student_percent=[]
silent_percent=[]
tech_percent=[]
for i in xrange(1,total_len/20+1):
	teacher_count=0
	student_count=0
	silent_count=0
	tech_count=0

	
	for j in xrange((i-1)*20,i*20):
		code=int(testData[j]);
		if code>=1 and code<=8:#教师语言
			teacher_count+=1;
		elif code>=9 and code<=12:#学生语言
			student_count+=1;
		elif code>=13 and code<=15:#沉寂
			silent_count+=1;
		else:#技术
			tech_count+=1;
	teacher_percent.append(teacher_count*100/20.0)
	student_percent.append(student_count*100/20.0)
	silent_percent.append(silent_count*100/20.0)
	tech_percent.append(tech_count*100/20.0)
	#print "%d,%d,%d,%d"%(teacher_count,student_count,silent_count,tech_count);
#print teacher_percent
#print student_percent
#print silent_percent
#print tech_percent

makeStatisticsGraphic([1,1,1,1],True,teacher_percent,student_percent,silent_percent,tech_percent)
print "执行完成！"