# 2023-11-23
#Start	20:04
#Part1	21:04	60min
#Part2	21:12	8min
#Total	68min

# input
n=1358



# finally a working pathfinding algorithm from scratch
def pf(x1,y1, x2,y2):
	def state(x,y,n):
		result=x*x+3*x+2*x*y+y+y*y
		result+=n
		result=str(bin(result))
		result=result.count('1')
		print(x,y, result)
		if result%2==0:
			return '.'
		else:
			return '#'
	
	# make grid
	grid=[]
	for y in range(x2*2):
		grid.append([])
		for x in range(y2*2):
			grid[y].append(state(x,y,n))

	## draw
	# for y in grid:
	# 	print(''.join(y))

	x=x1
	y=y1

	# don't explore visited tiles
	visited=set()
	# possible moves
	queue=[(x,y)]
	# shortest distances so far
	steps={(x,y):0}

	# while there are new tiles to check
	while len(queue)!=0:
		# add current tile to visited
		x,y= queue.pop(0)
		visited.add((x,y))
		# print(f'at {x},{y}')
		# print(queue)

		# possible moves except for out-of bounds and walls
		moves=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
		moves=[m for m in moves if m[0] in range(len(grid)) and m[1]in range(len(grid)) ]
		moves=[m for m in moves if grid[m[1]][m[0]]=='.']

		print(f'possible moves: {moves}')
		
		# for every move assign current distance +1 or keep the previous values if it's lower
		for move in moves:
			if move not in steps:
				steps[move]=steps[(x,y)]+1
			else:
				steps[move]=min(steps[move],steps[(x,y)]+1)
		# filter visited moves and add rest to queue
		moves=[m for m in moves if m not in visited]
		queue+=moves

	silver=steps[(x2,y2)]
	gold=len([s for s in steps.values() if s<=50])

	return silver, gold
print(pf(1,1,31,39))



