# 2023-10-18
#Start	15:25
#Part1	15:41	16min
#Part2	16:05	24min
#Total	40min
# some renundant if statements and double loop

with open('input') as f:
	lista=f.read().splitlines()

lista=[l.split(',') for l in lista]
paths=[]
for wire in lista:
	y=0
	x=0
	path=set()
	for point in wire:
		direction=point[0]
		n=int(point[1:])
		# print(direction, n)
		if direction=='U':
			for y2 in range(y,y+n):
				path.add((x,y2))
			y+=n
		elif direction=='D':
			for y2 in range(y,y-n,-1):
				path.add((x,y2))
			y-=n
		elif direction=='R':
			for x2 in range(x,x+n):
				path.add((x2,y))
			x+=n
		else:
			for x2 in range(x,x-n,-1):
				path.add((x2,y))
			x-=n
	paths.append(path)

ports=set.intersection(*paths)
ports.remove((0,0))

silver=[]
for p in ports:
	silver.append(abs(p[0])+abs(p[1]))

print(min(silver))

steps={p:[None,None]for p in ports}


for i, wire in enumerate(lista):
	y=0
	x=0
	score=0
	for point in wire:
		# print(x,y)
		direction=point[0]
		n=int(point[1:])
		# print(direction, n)
		if direction=='U':
			for y2 in range(y,y+n):
				y+=1
				score+=1
				if (x,y) in ports:
					if steps[(x,y)][i]==None:
						steps[(x,y)][i]=score
		elif direction=='D':
			for y2 in range(y,y-n,-1):
				y-=1
				score+=1
				if (x,y) in ports:
					if steps[(x,y)][i]==None:
						steps[(x,y)][i]=score
		elif direction=='R':
			for x2 in range(x,x+n):
				x+=1
				score+=1
				if (x,y) in ports:
					if steps[(x,y)][i]==None:
						steps[(x,y)][i]=score
		else:
			for x2 in range(x,x-n,-1):
				x-=1
				score+=1
				if (x,y) in ports:
					if steps[(x,y)][i]==None:
						steps[(x,y)][i]=score

print(sum(sorted(steps.items(), key=lambda x:sum(x[1]))[0][1]))