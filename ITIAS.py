#!/usr/bin/env python
# -*- coding: utf-8 -*-
#2016-05-26 08:45:28 by sixer

import matplotlib.pyplot as pl
from matplotlib.ticker import MultipleLocator
import numpy as np


def printMatrix(matrix):  
    for i in range(matrix_size):  
        for j in range(matrix_size):  
            print matrix[i][j],  
        print '\n' 
MultipleLocator.MAXTICKS = 100000
def makeStatisticsGraphic(view_key,data_teacher,data_student,data_silent,data_tech):

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
	if view_key[1]==1:
		pl.plot(x, z,'-go', label=u'学生语言')
	if view_key[2]==1:
		pl.plot(x, a,'-bo', label=u'沉寂')
	if view_key[3]==1:
		pl.plot(x, b,'-mo', label=u'技术')

	for xy in zip(x,y):
    		pl.annotate(xy[1], xy=xy, xytext=(2,5),fontsize=7,textcoords = 'offset points')
    		#print xy

	
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
	pl.yticks(fontsize=9)


	pl.title(u'CCNU杨浩导师组ITIAS分析工具',fontsize=16)  
	#pl.xlabel(u'日期')  
	pl.ylabel(u'比例',fontsize=8) 

	pl.legend(fontsize=8)

	#自动调整label显示方式，如果太挤则倾斜显示
	fig.autofmt_xdate()

	#保存曲线为图片格式
	#pl.savefig("./preview.png")
	pl.show()
	#print 'succ'
	pl.close(2)


f = open("datas.txt","r")
for m in f:
	testData=m.split();

total_len=len(testData)#数据总个数
#print total_len
matrix_size=18

matrix = [[0 for col in range(matrix_size)] for row in range(matrix_size)]

for i in range(0,total_len-1):
	x=int(testData[i]);
	y=int(testData[i+1]);

	if(x>17 or y>17):
		print testData[i]+","+testData[i+1]
	matrix[x-1][y-1]+=1;

printMatrix(matrix)

data=[]

for i in xrange(0,matrix_size):
	line_total=0;
	for j in xrange(0,matrix_size):
		line_total+=matrix[i][j]
	#print line_total
	data.append(round(line_total*100.0/(total_len-1),2))
print data



teacher_percent=[]
student_percent=[]
silent_percent=[]
tech_percent=[]
for i in xrange(1,total_len/20+1):
	#print "i",
	teacher_count=0
	student_count=0
	silent_count=0
	tech_count=0

	

	for j in xrange((i-1)*20,i*20):
		code=int(testData[j]);
		if code>=1 and code<=8:
			#print "%s"%testData[j];
			teacher_count+=1;
		elif code>=9 and code<=12:
			student_count+=1;
		elif code>=13 and code<=15:
			silent_count+=1;
		else:
			tech_count+=1;
	teacher_percent.append(teacher_count*100/20.0)
	student_percent.append(student_count*100/20.0)
	silent_percent.append(silent_count*100/20.0)
	tech_percent.append(tech_count*100/20.0)
	#print "%d,%d,%d,%d"%(teacher_count,student_count,silent_count,tech_count);
#print teacher_percent

makeStatisticsGraphic([1,1,0,1],teacher_percent,student_percent,silent_percent,tech_percent)