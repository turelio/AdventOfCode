# 2023-12-16
# Start	09:00	
# Part1	09:53	53min
# Part2	10:25	32min	
# Total	85min
with open('input') as f:
	lista=f.read().splitlines()
lista=[list(l) for l in lista]

dirs=('U','R','D','L') # for turning left/right by index
dm={'U':(0,-1),'R':(1,0),'D':(0,1),'L':(-1,0)}
r=range(len(lista)) # input is always square

def light(x,y,d):
	queue=[]
	visited=set() # energized positions
	visited2=set() # same but with direction to avoid going through same steps
	queue.append((x,y,d))
	while len(queue)!=0:
		x,y,d=queue.pop(0)
		visited.add((x,y))
		visited2.add((x,y,d))
		if lista[y][x]=='.':
			moves=[(x+dm[d][0],y+dm[d][1],d)]
		elif lista[y][x]=='|' and d in ['L','R']:
			moves=[(x,y-1,'U'),(x,y+1,'D')]
		elif lista[y][x]=='-' and d in ['U','D']:
			moves=[(x+1,y,'R'),(x-1,y,'L')]
		elif lista[y][x]=='/':
			if d in ['L','R']:
				d2=dirs[(dirs.index(d)-1)%len(dirs)]
				moves=[(x+dm[d2][0],y+dm[d2][1],d2)]
			else:
				d2=dirs[(dirs.index(d)+1)%len(dirs)]
				moves=[(x+dm[d2][0],y+dm[d2][1],d2)]
		elif lista[y][x]=='\\':
			if d in ['L','R']:
				d2=dirs[(dirs.index(d)+1)%len(dirs)]
				moves=[(x+dm[d2][0],y+dm[d2][1],d2)]
			else:
				d2=dirs[(dirs.index(d)-1)%len(dirs)]
				moves=[(x+dm[d2][0],y+dm[d2][1],d2)]
		else:
			moves=[(x+dm[d][0],y+dm[d][1],d)]
		moves=[(x2,y2,d2) for x2,y2,d2 in moves if x2 in r and y2 in r and (x2,y2,d2) not in visited2]
		queue+=moves
	return len(visited)

print('Silver:',light(0,0,'R'))
gold=set()
corner=len(lista)-1
for i in r:
	gold.add(light(i,0,'D'))
	gold.add(light(i,corner,'U'))
	gold.add(light(0,i,'R'))
	gold.add(light(corner,i,'L'))
print('Gold:',max(gold))