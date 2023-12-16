# 2023-12-16
# Start	09:00	
# Part1	09:53	53min
# Part2	10:25	32min	
# Total	85min
with open('input') as f:
	lista=f.read().splitlines()
lista=[list(l) for l in lista]

dirs=('U','R','D','L')
dm=[(0,-1),(1,0),(0,1),(-1,0)]
xr=range(len(lista[0]))
yr=range(len(lista))

def light(x,y,d):
	queue=[]
	visited=set()
	visited2=set()
	queue.append((x,y,d))
	while len(queue)!=0:
		x,y,d=queue.pop(0)
		visited.add((x,y))
		visited2.add((x,y,d))
		if lista[y][x]=='.':
			x2=x+dm[dirs.index(d)][0]
			y2=y+dm[dirs.index(d)][1]
			if x2 in xr and y2 in yr and (x2,y2,d) not in visited2:
				# print(f'\tmoving forward {d}')
				queue.append((x2,y2,d))
		elif lista[y][x]=='|':
			if d in ['L','R']:
				moves=[(x,y-1,'U'),(x,y+1,'D')]
				moves=[(x2,y2,d2) for x2,y2,d2 in moves if x2 in xr and y2 in yr]
				moves=[(x2,y2,d2) for x2,y2,d2 in moves if (x2,y2,d2) not in visited2]
				# print(f'\tat splitter, possible moves {moves}')
				queue+=moves
			else:
				x2=x+dm[dirs.index(d)][0]
				y2=y+dm[dirs.index(d)][1]
				if x2 in xr and y2 in yr and (x2,y2,d) not in visited2:
					queue.append((x2,y2,d))
		elif lista[y][x]=='-':
			if d in ['U','D']:
				moves=[(x+1,y,'R'),(x-1,y,'L')]
				moves=[(x2,y2,d2) for x2,y2,d2 in moves if x2 in xr and y2 in yr]
				moves=[(x2,y2,d2) for x2,y2,d2 in moves if (x2,y2,d2) not in visited2]

				# print(f'\tat splitter, possible moves {moves}')
				queue+=moves
			else:
				x2=x+dm[dirs.index(d)][0]
				y2=y+dm[dirs.index(d)][1]
				if x2 in xr and y2 in yr and (x2,y2,d) not in visited2:
					queue.append((x2,y2,d))
		elif lista[y][x]=='/':
			if d in ['L','R']:
				d2=dirs[(dirs.index(d)-1)%len(dirs)]
				# print(f'\tturn left from {d} to {d2}')
				x2=x+dm[dirs.index(d2)][0]
				y2=y+dm[dirs.index(d2)][1]
				if x2 in xr and y2 in yr and (x2,y2,d) not in visited2:
					queue.append((x2,y2,d2))
			else:
				d2=dirs[(dirs.index(d)+1)%len(dirs)]
				# print(f'\tturn right from {d} to {d2}')
				x2=x+dm[dirs.index(d2)][0]
				y2=y+dm[dirs.index(d2)][1]
				if x2 in xr and y2 in yr and (x2,y2,d) not in visited2:
					queue.append((x2,y2,d2))

		elif lista[y][x]=='\\':
			if d in ['L','R']:
				d2=dirs[(dirs.index(d)+1)%len(dirs)]
				# print(f'\tturn left from {d} to {d2}')
				x2=x+dm[dirs.index(d2)][0]
				y2=y+dm[dirs.index(d2)][1]
				if x2 in xr and y2 in yr and (x2,y2,d) not in visited2:
					queue.append((x2,y2,d2))
			else:
				d2=dirs[(dirs.index(d)-1)%len(dirs)]
				# print(f'\tturn right from {d} to {d2}')
				x2=x+dm[dirs.index(d2)][0]
				y2=y+dm[dirs.index(d2)][1]
				if x2 in xr and y2 in yr and (x2,y2,d) not in visited2:
					queue.append((x2,y2,d2))
	return len(visited)

print('Silver:',light(0,0,'R'))
# Part2
gold=0
corners=[(0,0,'R'),(0,0,'D'),(len(lista[0])-1,0,'D'),(len(lista[0])-1,0,'L'),(0,len(lista)-1,'U'),(0,len(lista)-1,'R'),(len(lista[0])-1,len(lista)-1,'U'),(len(lista[0])-1,len(lista)-1,'L')]

for x,y,d in corners:
	entry=light(x,y,d)
	if entry>gold:
		gold=entry

for x in range(1,len(lista[0])-1):
	entry=light(x,0,'D')
	if entry>gold:
		gold=entry
	entry=light(x,len(lista)-1,'U')
	if entry>gold:
		gold=entry

for y in range(1,len(lista)-1):	
	entry=light(0,y,'R')
	if entry>gold:
		gold=entry
	entry=light(len(lista[0])-1,y,'L')
	if entry>gold:
		gold=entry

print('Gold:',gold)