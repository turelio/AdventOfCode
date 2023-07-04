#2022-12-26
#Part1	19:50-20:13	(23min)
#Part2	20:13-20:14	(1min)
#Total	24min
with open('input') as f:
	lista=f.read().splitlines()

import itertools

moves={}
for l in lista:
	l=l.split(' ')
	start,end,distance=l[0],l[2],int(l[4])
	if not start in moves.keys():
		moves[start]={}
	if not end in moves.keys():
		moves[end]={}
	moves[start][end]=distance
	moves[end][start]=distance

silver=[]
for x in itertools.permutations(moves.keys()):
	valid=True
	path=0
	for i,v in enumerate(x):
		if i==0:
			prev=v
		elif v not in moves[prev].keys():
			valid=False
			break
		else:
			path+=moves[prev][v]
			prev=v
	if valid:
		silver.append(path)

print('Silver:',min(silver))
print('Gold:',max(silver))