# 2023-10-18
#Start	16:07
#Part1	16:18	11min
#Part2	16:30	12min
#Total	23min
from itertools import groupby
test=[156218,652527]

silver=0
gold=0
for v2 in range(test[0], test[1]+1):
	v=list(str(v2))
	v=[int(i) for i in v]
	prev=0
	cond1=True
	cond2=False
	for i,n in enumerate(v):
		if n<prev:
			cond1=False
			break
		else:
			prev=n
		if i+1<len(v):
			if n==v[i+1]:
				# print(f'{n}=={v[i+1]}')
				cond2=True
	if cond1 and cond2:
		silver+=1
		grouped=[list(g) for k, g in groupby(str(v2))]
		grouped=[len(i) for i in grouped]
		print(grouped)
		if 2 in grouped:
			gold+=1
		# print(v)

print(silver,gold)
