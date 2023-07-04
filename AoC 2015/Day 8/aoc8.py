# 2022-12-26
#Part1	19:21-19:35	(14min)
#Part2	19:35-19:44 (9min)
#Total	23min

with open('input') as f:
	lista=f.read().splitlines()

import re

silver=0
for l in lista:
	silver+=len(l)
	silver-=len(eval(l))
print("Silver:",silver)

gold=0
for l in lista:
	gold-=len(l)
	l2='"'
	for v in l:
		if v in ["\\", '"']:
			l2+='\\'
		l2+=v
	l2+='"'
	gold+=len(l2)

print('Gold:',gold)