# 2023-11-25
#Start	12:04
#Part1	13:13	69min
#Part2	13:23	10min
#Total	79min
with open('input') as f:
	lista=f.read()

grid=[list(l) for l in lista.splitlines()]

stops={}
for y,v1 in enumerate(grid):
	for x,v2 in enumerate(v1):
		if grid[y][x] not in ['.','#']:
			stops[grid[y][x]]=(x,y)
print(stops)


xr=range(len(grid[0]))
yr=range(len(grid))
# finally a working pathfinding algorithm from scratch
def pf(x1,y1, x2,y2):
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
		# print(f'at {x},{y}, visited {len(visited)} so far')
		# print(queue)

		# possible moves except for out-of bounds and walls
		moves=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
		moves=[m for m in moves if m[0] in xr and m[1]in yr]
		moves=[m for m in moves if grid[m[1]][m[0]]!='#']

		# print(f'possible moves: {moves}')
		
		# for every move assign current distance +1 or keep the previous values if it's lower
		for move in moves:
			if move not in steps:
				steps[move]=steps[(x,y)]+1
			else:
				if steps[move]>steps[(x,y)]+1:
					steps[move]=steps[(x,y)]+1
				# steps[move]=min(steps[move],steps[(x,y)]+1)
		# filter visited moves and add rest to queue
		moves=[m for m in moves if m not in visited and m not in queue]
		# print(f'added {len(moves)} new tiles to queue ({len(queue)})')
		queue+=moves
		# print()


	return steps[(x2,y2)]

silver=10000
# bruteforce
import itertools
test=itertools.permutations('1234567')
for j,t in enumerate(test):
	## silver
	# t=['0']+list(t)
	# gold
	t=['0']+list(t)+['0']
	distance=0
	over=False
	for i in range(len(t)-1):
		x1,y1=stops[t[i]]
		x2,y2=stops[t[i+1]]
		entry=pf(x1,y1,x2,y2)
		distance+=entry
		if distance>silver:
			over=True
			break
	if distance<silver and not over:
		silver=distance
		print(j,silver)
