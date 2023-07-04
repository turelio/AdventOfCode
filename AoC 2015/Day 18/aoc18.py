#2022-12-28
#Part1	15:00-15:20 (20min)
#Part2	15:20-15:25 (5min)
#Total	25min
import copy
with open('input') as f:
	lista=f.read().splitlines()

grid={}
print(lista, len(lista), len(lista[0]))
for y,v1 in enumerate(lista):
	for x, v2 in enumerate(v1):
		if lista[y][x]=='#':
			grid[(x,y)]=1
		else:
			grid[(x,y)]=0

corners=[(0,0),(99,0),(0,99),(99,99)]
for i in corners:
	grid[i]=1

for i in range(100):
	grid2=copy.deepcopy(grid)
	for k,v in grid.items():
		if k in corners:
			grid2[k]=1
			continue
		x,y=k
		neighbors=[(x,y+1), (x+1,y+1), (x+1,y), (x+1,y-1), (x,y-1),(x-1,y-1),(x-1,y),(x-1,y+1)]
		neighbors=[n for n in neighbors if n in grid.keys() and grid[n]==1]
		if v==1:
			if len(neighbors) not in (2,3):
				grid2[k]=0
		else:
			if len(neighbors) == 3:
				grid2[k]=1
	grid=copy.deepcopy(grid2)

silver=0
for k in grid:
	if grid[k]==1:
		silver+=1

print(silver)

