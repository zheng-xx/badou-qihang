from math import sqrt
import numpy as np
import unicodedata
from numpy.core.defchararray import isdigit


def CalculateCOS():
	print("请输入第一个向量坐标，x，y坐标用空格隔开,按Enter键完成:")
	p1 = input()
	tmp1 = p1.split()
	if isdigit(tmp1[0]) == False or isdigit(tmp1[1]) == False:
		print("输入非法,请重新输入!")
		return

	if isinstance(int(tmp1[0]),int) and isinstance(int(tmp1[1]),int):
		print("您输入的第一个向量为("+p1.split()[0]+","+p1.split()[1]+")"+"\n"+"请按照同样的方式输入第二个向量坐标，按Enter键完成:")
		p2 = input()
		tmp2 = p2.split()
		if isdigit(tmp2[0]) == False or isdigit(tmp2[1]) == False:
			print("输入非法,请重新输入!")
			return
		if isinstance(int(tmp2[0]),int) and isinstance(int(tmp2[1]),int):
			print("您输入的第二个向量为("+p2.split()[0]+","+p2.split()[1]+")")
			p1x = int(p1.split()[0])
			p1y = int(p1.split()[1])
			p2x = int(p2.split()[0])
			p2y = int(p2.split()[1])
			a = p1x*p2x + p1y*p2y
			b = sqrt( (p1x ** 2)+(p1y ** 2) )
			c = sqrt( (p2x ** 2)+(p2y ** 2) )
			cos = a / (b * c)
			print( "您输入的两个向量的余玄值为%f："%(cos) )
			return
		pass
	return

CalculateCOS()
