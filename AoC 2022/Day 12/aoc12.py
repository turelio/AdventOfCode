
#Start	14:39
#Part1	16:16
#computing from 16:54 to17:06)
#Part2	17:06
#Total	135min

# Second pass, 5s, inverted search
with open('input') as f:
	lista=f.read().splitlines()

def height(coord):
	y,x=coord
	if lista[y][x]=='S':
		h=ord('a')
	elif lista[y][x]=='E':
		h=ord('z')
	else:
		h=ord(lista[y][x])
	return h

def valid(coord):
	y,x=coord
	moves=[]
	if y>0:
		moves.append([y-1,x])
	if y<len(lista)-1:
		moves.append([y+1,x])
	if x>0:
		moves.append([y,x-1])
	if x<len(lista[0])-1:
		moves.append([y,x+1])
	moves=[m for m in moves if height(m)>=height(coord)-1]
	return moves

def grid(coord):
	return lista[coord[0]][coord[1]]

def shortest(start):
	visited=set()
	traverse={}
	for y in range(len(lista)):
		for x in range(len(lista[0])):
			if [y,x]==start:
				traverse[str([y,x])]=0
			else:
				traverse[str([y,x])]=100000

	while True:
		traverse=dict(sorted(traverse.items(), key=lambda item: item[1]))
		for k,v in traverse.items():
			if k not in visited:
				c=eval(k)
				break
		if grid(c)=='S':
			print(f'Silver: {traverse[str(c)]} steps')
			gold=traverse[str(c)]
			break
		if traverse[str(c)]==100000:
			return 100000
		visited.add(str(c))
		moves=valid(c)
		for m in moves:
			if traverse[str(c)]+1<traverse[str(m)]:
				traverse[str(m)]=traverse[str(c)]+1
	return gold, traverse

for y in range(len(lista)):
	for x in range(len(lista[0])):
		if grid([y,x])=='E':
			start=[y,x]

gold, traverse=shortest(start)

for k,v in traverse.items():
	if grid(eval(k))=='a':
		print(f'Gold: {v} steps')
		break

## First pass, 711s, dijkstra-like
# import time
# with open('input') as f:
# 	lista=f.read().splitlines()

# # print(lista)
# test='''Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi'''
# test=test.split('\n')

# # lista=test

# # print(lista)


# def valid(coord):
# 	y,x=coord
# 	moves=[]
# 	if y>0:
# 		moves.append([y-1,x])
# 	if y<len(lista)-1:
# 		moves.append([y+1,x])
# 	if x>0:
# 		moves.append([y,x-1])
# 	if x<len(lista[0])-1:
# 		moves.append([y,x+1])
# 	# print(moves)
# 	return [m for m in moves if height(m)<=height(coord)+1]

# def grid(coord):
# 	return lista[coord[0]][coord[1]]

# def board():
# 	for l in lista:
# 		print(l)

# def height(coord):
# 	y,x=coord
# 	if lista[y][x]=='S':
# 		h=ord('a')
# 	elif lista[y][x]=='E':
# 		h=ord('z')
# 	else:
# 		h=ord(lista[y][x])
# 	return h

# # start=[0,0]
# # c=start

# # print(f'{c} ({lista[c[0]][c[1]]}) possible spots:')

# silver=[]
# traverse={}
# a_count=[]
# for y in range(len(lista)):
# 	for x in range(len(lista[0])):
# 		if grid([y,x])=='a':
# 			a_count.append([y,x])
# 		if grid([y,x])=='S':
# 			a_count.append([y,x])
# 			s_loc=[y,x]
# 			# traverse[str([y,x])]=0
# 		else:
# 			traverse[str([y,x])]=100000

# # board()
# total=len(a_count)
# time_start=time.time()
# time_last=time.time()
# def shortest(start):
# 	queue=set()
# 	traverse={}
# 	for y in range(len(lista)):
# 		for x in range(len(lista[0])):
# 			if [y,x]==start:
# 				traverse[str([y,x])]=0
# 			else:
# 				traverse[str([y,x])]=100000

# 	while True:
# 		traverse=dict(sorted(traverse.items(), key=lambda item: item[1]))
# 		for k,v in traverse.items():
# 			if k not in queue:
# 				c=eval(k)
# 				break
# 		if grid(c)=='E':
# 			print(f'{traverse[str(c)]} steps\t{round(time.time()-time_last, 3)}s\t{round(time.time()-time_start,2)}s\ttotal\t{total-left} left')
# 			gold=traverse[str(c)]
# 			break
# 		if traverse[str(c)]==100000:
# 			return 100000
# 		# print(f'choosing ({grid(c)}) at {c}, lowest value at {traverse[str(c)]}, queue count {len(queue)}')
# 		queue.add(str(c))
# 		moves=valid(c)
# 		# print(f'possible moves: {list(map(grid, moves))}')
# 		for m in moves:
# 			if traverse[str(c)]+1<traverse[str(m)]:
# 				traverse[str(m)]=traverse[str(c)]+1
# 	return gold
# print(len(a_count))
# gold=set()

# for left,v in enumerate(a_count):
# 	gold.add(shortest(v))
# 	time_last=time.time()

# print(min(gold))

