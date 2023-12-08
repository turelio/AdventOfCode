# 2023-12-08
# Start	06:00	
# Part1	06:15	15min
# Part2	06:54	39min
# Total	54min
from math import lcm
with open('input') as f:
	lista=f.read().strip().splitlines()

code=[1 if l=='R' else 0 for l in lista[0]]
moves={}
for l in lista[2:]:
	l=l.split(' ')
	moves[l[0]]=(l[2][1:-1],l[3][:-1])

c,i,j='AAA',0,0
while c!='ZZZ':
	v=code[i%len(code)]
	c=moves[c][v]
	i=(i+1)%len(code)
	i%=len(code)
	j+=1
print('Silver:\t',j)

ghost=[[k,0] for k in moves.keys() if k[-1]=='A']
end=[k for k in moves.keys() if k[-1]=='Z']
i,j=0,0
while True:
	v=code[i%len(code)]
	fin=True
	for x,g in enumerate(ghost):
		if ghost[x][0] in end and ghost[x][1]==0:
			ghost[x][1]=j
		if ghost[x][1]==0:
			fin=False
	if fin:
		break
	for x,g in enumerate(ghost):
		ghost[x][0]=moves[ghost[x][0]][v]
	i=(i+1)%len(code)
	j+=1

ghost=list(zip(*ghost))[1]
print('Gold:\t', lcm(*ghost))