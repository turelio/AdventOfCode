# 2022-12-28
#Part1	13:58-14:42	(44min)
#Part2	14:42-14:47 (5min)
#Total	49min

# second pass, 400ms
import itertools
lista=[50,44,11,49,42,46,18,32,26,40,21,7,18,43,10,47,36,24,22,40]
lista=[(i,v) for i,v in enumerate(lista)]
# i know highest number of containers that can still equal 150 is 9 from sums of n lowest containers
ranges=[itertools.combinations(lista,i) for i in range(2,10)]
silver,gold=0,0

for i,r in enumerate(ranges):
	current=0
	for j in r:
		if sum(list(zip(*j))[1])==150:
			silver+=1
			current+=1
	print(i+2,current)
	if current>0 and gold==0:
		gold=current
print(silver, gold)

# first pass, few minutes
# import copy
# lista=[50,44,11,49,42,46,18,32,26,40,21,7,18,43,10,47,36,24,22,40]
# lista=[(i,v) for i,v in enumerate(lista)]
# lista=sorted(lista)
# test=[(0,20),(1,15),(2,10),(3,5),(4,5)]
# print(lista)

# silver=[]

# def fill(c, left, lista=set(),j=0):
# 	if len(silver)==654:
# 		return
# 	if left==0:
# 		if lista not in silver:
# 			silver.append(lista)
# 		return
# 	elif left<0:
# 		return
# 	else:
# 		c=[l for l in c if l[1]<=left]
# 		remainder=0
# 		for i in c:
# 			remainder+=i[1]
# 		if remainder<left:
# 			return
# 		for i0, i in c:
# 			if j<2:
# 				print(j*'\t',i0, len(silver))
# 			left2=left-i
# 			c2=copy.deepcopy(c)
# 			c2.pop(c2.index((i0,i)))
# 			lista2=copy.deepcopy(lista)
# 			lista2.add(i0)
# 			fill(c2,left2,lista2,j+1)

# # fill(test, 25)
# fill(lista,150)
# print(len(silver))
# gold=[len(s) for s in silver]
# for i in range(20):
# 	print(i, gold.count(i))