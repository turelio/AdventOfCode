
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