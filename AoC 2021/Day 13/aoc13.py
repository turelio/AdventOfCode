
#Start	10:03	20211213
#Part1	10:31	28min
#Part2	11:05	34min	
#Total	62min
with open('input') as f:
	lista=f.read().split('\n\n')

grid0=lista[0].splitlines()
fold=lista[1].splitlines()

for c,f in enumerate(fold):
	f=f.replace("fold along ","").split("=")
	fold[c]=f
	fold[c][1]=int(fold[c][1])

grid0=[[int(j) for j in i.split(',')] for i in grid0]
grid=[[0 for i in range(1500)] for i in range(1500)]

for i in grid0:
	grid[i[1]][i[0]]+=1

def newfold(instr, grid):
	newgrid=[]
	fold=instr[1]
	if instr[0]=='x':
		for y,v1 in enumerate(grid):
			for x,v2 in enumerate(v1):
				if x>fold and v2>0:
					x2=2*fold-x
					grid[y][x2]+=1
			newgrid.append(grid[y][0:fold])
		return newgrid
	else:
		for y,v1 in enumerate(grid):
			for x,v2 in enumerate(v1):
				if y>fold and v2>0:
					y2=2*fold-y
					grid[y2][x]+=1
		newgrid=grid[0:fold]
		return newgrid		

#Silver
silver=0
grid3=newfold(fold[0], grid)
for y,v1 in enumerate(grid3):
	for x,v2 in enumerate(v1):
		if grid3[y][x]>0:
			silver+=1
print(silver)

for i in fold:
	#print(f"grid size x={len(grid[0])} y={len(grid)}")
	#print(f"fold by {i}:")
	grid=newfold(i, grid)

#Gold
for i in grid:
	for j in i:
		if j==0:
			print(' ',end='')
		else:
			print(j, end='')
	print('')
