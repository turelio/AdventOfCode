# 2023-12-01
#Start	14:30
#Part1	14:52	22min
#Part2	14:54	2min
#Total	24min
with open('input') as f:
	lista=f.read().splitlines()

import re

c=[]
for l in lista:
	test=re.match(r'position=<(.?\d+), (.?\d+)> velocity=<(.?\d+), (.?\d+)>',l)
	test=test.groups()
	test=[int(t.strip()) for t in test]
	c.append(test)

print(len(c))

def draw_stars(c):
	c2=list(zip(*c))
	c3=set([tuple(x[:2]) for x in c])
	x1,x2=min(c2[0]),max(c2[0])
	y1,y2=min(c2[1]),max(c2[1])
	area=(abs(x2-x1)*abs(y2-y1))
	for y in range(y1,y2+1):
		row=''
		for x in range(x1,x2+1):
			if (x,y) in c3:
				row+='#'
			else:
				row+='.'
		print(row)


def get_area(c):
	c2=list(zip(*c))
	x1,x2=min(c2[0]),max(c2[0])
	y1,y2=min(c2[1]),max(c2[1])
	area=(abs(x2-x1)*abs(y2-y1))
	return area
import copy

n=0
while True:
	if n%1000==0:
		print('####',n)
	c2=[]
	for i, star in enumerate(c):
		c2.append([c[i][0]+c[i][2],c[i][1]+c[i][3],c[i][2],c[i][3]])
	i
	if get_area(c2)>get_area(c):
		print(n)
		draw_stars(c)
		break
	c=c2
	n+=1