# 2023-12-15
#Start 09:00	
#Part1 11:42	162min	
#Part2 12:05	23min	
#Total 185min
# visualized, so run from terminal
import os, time, copy
with open('input') as f:
	lista=f.read().splitlines()
lista=[list(l) for l in lista]

if os.name=='nt':
	clear_cmd='cls'
else:
	clear_cmd='clear'

# print map, optional color
def board(lista, colored=False):
	if colored:
		elf='\x1b[6;30;42m' + 'E' + '\x1b[0m'
		gob='\x1b[6;30;41m' + 'E' + '\x1b[0m'
	else:
		elf, gob = 'E', 'G'
	for l in lista:
		# print(''.join(list(map(lambda y:y[0],l))), end='\t')
		row=''
		for e in l:
			if e[0]=='#':
				row+='█'
			if e[0]=='.':
				row+=' '
			if e[0]=='E':
				row+=elf
			if e[0]=='G':
				row+=gob
		print(row,end='\t')
		add=''
		for e in l:
			if e[0] in ['G','E']:
				add+=f'{e[0]}({e[1]}) '
		print(add)


# distances to all empty spots
def distances(lista,x,y):
	d={}
	for y2,v in enumerate(lista):
		for x2, v2 in enumerate(v):
			if v2=='.':
				d[(x2,y2)]=1000
	visited=set()
	queue=[(x,y)]
	d[(x,y)]=0
	while len(queue)!=0:
		x,y=queue.pop(0)
		visited.add((x,y))
		moves=[[x+1,y],[x-1,y],[x,y-1],[x,y+1]]
		moves=[(x,y) for x,y in moves if (x,y) in d]
		for x2,y2 in moves:
			if d[(x2,y2)]>d[(x,y)]:
				d[(x2,y2)]=d[(x,y)]+1
		moves=[(x,y) for x,y in moves if (x,y) not in visited and (x,y) not in queue]
		queue+=moves
	return d

def act(lista, c, x, y):
	if c[0]=='G':
		enemy='E'
	else:
		enemy='G'
	enemies=[]
	for y2,v in enumerate(lista):
		for x2, v2 in enumerate(v):
			if v2[0]==enemy:
				enemies.append([x2,y2])
	# end if no more enemies
	if len(enemies)==0:
		return (x,y),lista,True
	skipmove=False
	near=[[x+1,y],[x-1,y],[x,y-1],[x,y+1]]
	near=[(x2,y2) for x2,y2 in near if lista[y2][x2][0]==enemy]
	# skip moving if enemy in range
	if len(near)!=0:
		skipmove=True
		chosen2=(x,y)
	if not skipmove:
		inrange=[]
		# find positions near enemies, no duplicates
		for x2,y2 in enemies:
			adj=[[x2+1,y2],[x2-1,y2],[x2,y2-1],[x2,y2+1]]
			adj=[(x2,y2) for x2,y2 in adj if lista[y2][x2]=='.']
			inrange+=adj
		inrange=list(set(inrange))
		# calculate distances, filter by positions near enemies that are reachable
		d=distances(lista,x,y)
		reachable={k:v for k,v in d.items() if k in inrange and v!=1000}
		# skip moving if no reachable positions available
		if len(reachable)==0:
			chosen2=(x,y)
		else:
			# find closest positions, sort by reading order (y,x), choose first
			shortest=min(reachable.values())
			nearest=[k for k,v in reachable.items() if v==shortest]
			chosen=sorted(nearest,key=lambda m:(m[1],m[0]))
			chosen=chosen[0]
			# find next step towards the goal, compare distances, choose closest, sort by reading order
			moves2=[[x+1,y],[x-1,y],[x,y-1],[x,y+1]]
			moves2=[(x2,y2) for x2,y2 in moves2 if lista[y2][x2]=='.']
			moves3=[]
			shortest2=1000
			for m in moves2:
				d2=distances(lista,m[0],m[1])
				if d2[chosen]<shortest2:
					shortest2=d2[chosen]
				moves3.append([m,d2[chosen]])
			moves3=[m[0] for m in moves3 if m[1]==shortest2]
			chosen2=sorted(moves3,key=lambda m:(m[1],m[0]))
			chosen2=chosen2[0]
			# final destination, change grid
			x2,y2=chosen2
			lista[y2][x2]=c
			lista[y][x]='.'
			x,y=x2,y2
	# Attacking logic
	# find targets in range again
	near=[[x+1,y],[x-1,y],[x,y-1],[x,y+1]]
	near=[(x2,y2) for x2,y2 in near if lista[y2][x2][0]==enemy]
	# skip if no target to attack
	if len(near)==0:
		pass
	else:
		# choose target by lowest health then reading order
		targets=[[[x2,y2],lista[y2][x2][1]] for x2,y2 in near]
		targets=sorted(targets,key=lambda m:(m[1],m[0][1],m[0][0]))
		x3,y3=targets[0][0]
		# reduce target health, remove if killed
		lista[y3][x3][1]-=lista[y][x][2]
		if lista[y3][x3][1]<=0:
			lista[y3][x3]='.'
	return chosen2,lista,False

def round(lista):
	acted=set()
	for y,v in enumerate(lista):
		for x, v2 in enumerate(v):
			if v2[0] in ['G','E']:
				# skip if acted already
				if (x,y) not in acted:
					newpos,lista,won=act(lista, lista[y][x],x,y)
					acted.add(newpos)
					if won:
						return lista,True
				else:
					continue
	return lista,False

def battle(lista, attack=3, visualize=False):
	lista=copy.deepcopy(lista)
	elves_start=0
	# set hp and attack
	for y,v in enumerate(lista):
		for x, v2 in enumerate(v):
			if v2=='G':
				lista[y][x]=[v2,200,3]
			if v2=='E':
				lista[y][x]=[v2,200,attack]
				elves_start+=1
	# round loop
	for i in range(500):
		lista,won2=round(lista)
		if won2:
			break
		else:
			if visualize:
				os.system(clear_cmd)
				print(f'Round {i+1}:')
				board(lista,True)
				time.sleep(0.1)
	# calculate score and survivors
	result=0
	elves_end=0
	for y,v in enumerate(lista):
		for x, v2 in enumerate(v):
				if v2[0] in ['G','E']:
					result+=v2[1]
					if v2[0]=='E':
						elves_end+=1
	result*=i
	if visualize:
		os.system(clear_cmd)
		board(lista,True)
	print(f'Score {result}, {elves_end}/{elves_start} Elves survived at round {i}')
	return result

print('Silver:',battle(lista,3))
print('Gold:',battle(lista,34))
