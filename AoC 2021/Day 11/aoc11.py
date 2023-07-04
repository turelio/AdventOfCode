#Start	11:50	20211211
#Part1	12:55	65min
#Part2	13:09	14min-8min przerwy
#Total	71min
with open('input') as f:
	lista=f.read()
grid=[list(map(int, list(l))) for l in lista.splitlines()]

def draw_grid(grid):
	for i in grid:
		print(i)
	print('\n')

def neighbours(y,x):
	n = [grid[y-1][x],y-1,x] if 9>=y-1>=0 else 0
	s = [grid[y+1][x],y+1,x] if 9>=y+1>=0 else 0
	w = [grid[y][x-1],y,x-1] if 9>=x-1>=0 else 0
	e = [grid[y][x+1],y,x+1] if 9>=x+1>=0 else 0

	ne = [grid[y-1][x+1],y-1,x+1] if all([9>=y-1>=0,9>=x+1>=0]) else 0
	se = [grid[y+1][x+1],y+1,x+1] if all([9>=y+1>=0,9>=x+1>=0]) else 0
	sw = [grid[y+1][x-1],y+1,x-1] if all([9>=x-1>=0,9>=y+1>=0]) else 0
	nw = [grid[y-1][x-1],y-1,x-1] if all([9>=x-1>=0,9>=y-1>=0]) else 0
	return [i for i in [n,ne,e,se,s,sw,w,nw] if i!=0]


def check_flash(grid):
	for i in grid:
		for j in i:
			if j>9:
				return True
	return False

def check_flash_big(grid):
	for i in grid:
		for j in i:
			if j!=0:
				return False
	return True

silver=0
silverlist=[]
gold=0
while True:
	#print(f"step {gold}")
	#draw_grid(grid)
	if check_flash_big(grid):
		break
	for c1,v1 in enumerate(grid):
		for c2,v2 in enumerate(v1):
			grid[c1][c2]+=1
	while check_flash(grid):
		for c1,v1 in enumerate(grid):
			for c2,v2 in enumerate(v1):
				if grid[c1][c2]>9:
					grid[c1][c2]=0
					silver+=1
					for i in neighbours(c1,c2):
						if grid[i[1]][i[2]]!=0:
							grid[i[1]][i[2]]+=1
	silverlist.append(silver)											
	gold+=1

print(silverlist[99], gold)