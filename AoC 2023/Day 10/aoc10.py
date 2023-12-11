# 2023-12-10, 2023-12-11
# Start	09:01	
# Part1	09:33		32min
# Part2	9.45-10.45 	60+48min
# Total	140min
# slow but finally works
import copy
with open('input') as f:
	lista=f.read().splitlines()
prev='U'
initial='|'

for y,v in enumerate(lista):
	lista[y]=list(lista[y])
	if 'S' in v:
		c=[v.index('S'), y]
		print(c)
		lista[y][v.index('S')]=initial

start=copy.deepcopy(c)
c=start
pipes=set()
while True:
	stop=lista[c[1]][c[0]]
	pipes.add(tuple(c))
	if stop =='-':
		if prev=='R':
			c=[c[0]+1,c[1]]
			prev='R'
		elif prev=='L':
			c=[c[0]-1,c[1]]
			prev='L'
	elif stop =='|':
		if prev=='D':
			c=[c[0],c[1]+1]
			prev='D'
		elif prev=='U':
			c=[c[0],c[1]-1]
			prev='U'
	elif stop =='7':
		if prev=='R':
			c=[c[0],c[1]+1]
			prev='D'
		elif prev=='U':
			c=[c[0]-1,c[1]]
			prev='L'
		else:
			print('invalid')
			break
	elif stop =='J':
		if prev=='D':
			c=[c[0]-1,c[1]]
			prev='L'
		elif prev=='R':
			c=[c[0],c[1]-1]
			prev='U'
		else:
			print('invalid')
			break
	elif stop =='L':
		if prev=='L':
			c=[c[0],c[1]-1]
			prev='U'
		elif prev=='D':
			c=[c[0]+1,c[1]]
			prev='R'
		else:
			print('invalid')
			break
	elif stop =='F':
		if prev=='U':
			c=[c[0]+1,c[1]]
			prev='R'
		elif prev=='L':
			c=[c[0],c[1]+1]
			prev='D'
		else:
			print('invalid')
			break
	else:
		print(f'{stop} not specified')
		break
	if c==start:
		break
print('Silver:',len(pipes)//2)

yr=len(lista)
xr=len(lista[0])
lista2=copy.deepcopy(lista)

for y,v in enumerate(lista2):
	for x,v2 in enumerate(v):
		if (x,y) not in pipes:
			lista2[y][x]='.'

i=0
for j in range(yr):
	lista2.insert(i,[' ']*xr)
	i+=2
lista2=list(zip(*lista2))
i=0
for j in range(len(lista2)):
	lista2.insert(i,[' ']*len(lista2[0]))
	i+=2
lista2=list(zip(*lista2))

yr=len(lista2)
xr=len(lista2[0])
hori=[['-','-'],['F','-'],['-','7'],['L','-'],['-','J'],['L','7'],['F','J'],['F','7'],['L','J']]
vert=[['|','|'],['F','|'],['7','|'],['|','L'],['|','J'],['7','L'],['F','J'],['F','L'],['7','J']]
lista2=[list(x) for x in lista2]
dots=set()
# add pipes between pipes so there's no holes, count 'real' empty spaces (dots)
for y,v in enumerate(lista2):
	for x,v2 in enumerate(v):
		if v2=='.':
			dots.add((x,y))
		if v2==' ':
			nearx=[(x-1,y),(x+1,y)]
			nearx=[n for n in nearx if n[0] in range(xr) and n[1] in range(yr)]
			neary=[(x,y-1),(x,y+1)]
			neary=[n for n in neary if n[0] in range(xr) and n[1] in range(yr)]
			if len(nearx)==2:
				nearx=[lista2[j][i] for i,j in nearx]
				if nearx in hori:
					lista2[y][x]='-'
					continue
			if len(neary)==2:
				neary=[lista2[j][i] for i,j in neary]
				if neary in vert:
					lista2[y][x]='|'
					continue

# flood fill outside, inside is all-outside
visited=set()
queue=[(0,0)]
while len(queue)!=0:
	x,y=queue.pop(0)
	visited.add((x,y))
	near=[(x-1,y),(x+1,y),(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y+1),(x,y+1),(x+1,y+1)]
	near=[(x,y) for x,y in near if x in range(xr) and y in range(yr)]
	near=[(x,y) for x,y in near if lista2[y][x] in [' ','.']]
	near=[(x,y) for x,y in near if (x,y) not in visited and (x,y) not in queue]
	queue+=near
dots2=[(x,y) for x,y in visited if lista2[y][x]=='.']
gold=len(dots)-len(dots2)
print('Gold:', gold)
