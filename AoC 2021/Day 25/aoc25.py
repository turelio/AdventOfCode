#Start	9:35	20211225
#Part1	10:37 	62min	
#Total	62min
with open('input') as f:
	lista=[list(l) for l in f.read().splitlines()]

def step(grid):
	counter=0
	for y,v1 in enumerate(grid):
		for x, v2 in enumerate(v1):
			if grid[y][x]=='.':
				continue
			elif grid[y][x]=='>':
				if x!=len(grid[0])-1:
					x2=x+1
				else:
					x2=0
				if grid[y][x2]=='.':
					grid[y][x2]='R'
					grid[y][x]=','
					counter+=1
	for x,v1 in enumerate(grid[0]):
		for y, v2 in enumerate(grid):
			if grid[y][x]=='.':
				continue
			elif grid[y][x]=='v':
				if y!=len(grid)-1:
					y2=y+1
				else:
					y2=0
				if grid[y2][x]=='.' or grid[y2][x]==',':
					grid[y2][x]='S'
					grid[y][x]=';'
					counter+=1
	for y,v1 in enumerate(grid):
		for x, v2 in enumerate(v1):
			if grid[y][x]=='R':
				grid[y][x]='>'
			if grid[y][x]=='S':
				grid[y][x]='v'
			if grid[y][x]==',' or grid[y][x]==';':
				grid[y][x]='.'

	if counter!=0:
		return grid, False
	else:
		return grid, True

grid=lista.copy()
j=1
while True:
	print(f"step {j}")
	grid, same=step(grid)
	if same:
		print(f"stopped at {j}")
		break
	j+=1