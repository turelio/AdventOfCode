# 2023-11-24
#Start	13:02
#Part1	14:01	59min
#Part2	14:02	1min
#Total	60min
import hashlib

s='hhhxzeay'
silver=set()
op=set(['b','c','d','e','f'])
sequence=['U','D','L','R']


def move(x,y,path=''):
	if x==4 and y==4:
		silver.add(path)
		return
	md=hashlib.md5((s+path).encode()).hexdigest()[:4]
	#inverted vertically to visualize easier
	moves=[(x,y-1),(x,y+1),(x-1,y),(x+1,y)]
	moves2=[]
	for i in range(4):
		if md[i] in op:
			moves2.append(moves[i])
	moves2=[m for m in moves2 if m[0] in range(1,5) and m[1] in range(1,5)]
	if len(moves2)==0: #stuck
		return
	for m in moves2:
		d=sequence[moves.index(m)]
		move(m[0],m[1],path+d)


move(1,1)
silver=list(sorted(silver, key=lambda x:len(x)))
print(len(silver), silver[0],len(silver[-1]))