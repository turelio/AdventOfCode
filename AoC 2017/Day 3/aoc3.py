# 2022-02-02
#Start	18:56
#Part1	19:57
#Part2	20:13
#Total	77min

# First pass
def neighbours(grid,x,y):
	result=0
	near=[(x+1,y),(x+1,y+1),(x,y+1),(x-1, y+1),(x-1,y),(x-1,y-1),(x,y-1),(x+1,y-1)]
	for i in near:
		if i in grid.keys():
			result+=grid[i]
	return result


def snail(n):
	grid={}
	z=1
	d=1
	x,y=0,0
	grid[(x,y)]=1
	print(f'{grid[(x,y)]} at {x},{y}')
	while z<n:
		x+=1
		grid[(x,y)]=neighbours(grid,x,y)
		z+=1
		print(f'{z}/{grid[(x,y)]} at {x},{y}')
		for i in range(d):	
			y+=1
			grid[(x,y)]=neighbours(grid,x,y)
			z+=1
			print(f'{z}/{grid[(x,y)]} at {x},{y}')
		for i in range(d+1):
			x-=1
			grid[(x,y)]=neighbours(grid,x,y)
			z+=1
			print(f'{z}/{grid[(x,y)]} at {x},{y}')
		for i in range(d+1):
			y-=1
			grid[(x,y)]=neighbours(grid,x,y)
			z+=1
			print(f'{z}/{grid[(x,y)]} at {x},{y}')
		for i in range(d+1):
			x+=1
			grid[(x,y)]=neighbours(grid,x,y)
			z+=1
			print(f'{z}/{grid[(x,y)]} at {x},{y}')
		if grid[(x,y)]>n:
			break
		d+=2

snail(265149)