#Start	12:41
#Part1	12:53
#Part2	~13:45
#Total	66min

# Second pass, 114s, ~2min
with open('input') as f:
	lista=f.read().splitlines()

import random,copy


shape=[]
for l in lista:
	l=l.split(',')
	c=(int(l[0]), int(l[1]), int(l[2]))
	shape.append(c)

def getneighbors(x,y,z):
	return [(x+1, y, z), (x-1, y, z), (x,y+1,z),(x,y-1, z),(x,y,z+1),(x,y,z-1)]

silver=0
surface={}

for s in shape:
	x,y,z=s
	sides=6
	neighbors=getneighbors(x,y,z)
	empty_near=[]
	for n in neighbors:
		if n in shape:
			sides-=1
		else:
			empty_near.append(n)

	if sides!=0:
		surface[s]=empty_near
	silver+=sides

print('Silver:',silver)

shape2=list(zip(*shape))

def inbounds(c):
	x,y,z=c
	if x not in range(min(shape2[0]), max(shape2[0])+1):
		return False
	elif y not in range(min(shape2[1]), max(shape2[1])+1):
		return False
	elif z not in range(min(shape2[2]), max(shape2[2])+1):
		return False
	else:
		return True

def escape(c):
	x,y,z=c
	if not inbounds(c):
		return True
	for i in range(300):
		near=getneighbors(x,y,z)
		near=[n for n in near if n not in shape]
		if len(near)==0:
			return False
		x,y,z=random.choice(near)
		if not inbounds((x,y,z)):
			return True
	return False


gold=silver
i=0
guaranteed=set()
escaped=set()

for k,v in surface.items():
	print(f'{i} / {len(surface)}')
	for c in v:
		if c in escaped:
			continue
		elif c in guaranteed or not escape(c):
			gold-=1
			guaranteed.add(c)
		else:
			escaped.add(c)
	i+=1

print(gold)

# # First pass, 812s / 13.5min
# with open('input') as f:
# 	lista=f.read().splitlines()

# import random
# # print(lista)
# shape0=set()
# shape=[]
# for l in lista:
# 	l=l.split(',')
# 	c=(int(l[0]), int(l[1]), int(l[2]))
# 	shape.append(c)
# 	shape0.add(c)

# print(len(shape), len(shape0))

# def getneighbors(x,y,z):
# 	return [(x+1, y, z), (x-1, y, z), (x,y+1,z),(x,y-1, z),(x,y,z+1),(x,y,z-1)]

# silver=0
# surface={}
# empty=[]

# for s in shape:
# 	x,y,z=s
# 	sides=6
# 	neighbors=getneighbors(x,y,z)
# 	empty_near=[]
# 	for n in neighbors:
# 		if n in shape:
# 			sides-=1
# 		else:
# 			empty_near.append(n)
# 			empty.append(n)

# 	if sides!=0:
# 		surface[s]=empty_near
# 	silver+=sides

# print('Silver:',silver)

# print(len(surface))

# shape2=list(zip(*shape))
# print(f'x from {min(shape2[0])} to {max(shape2[0])}\ny from {min(shape2[1])} to {max(shape2[1])}\nz from {min(shape2[2])} to {max(shape2[2])}')

# def inbounds(c):
# 	x,y,z=c
# 	if x not in range(min(shape2[0]), max(shape2[0])+1):
# 		return False
# 	elif y not in range(min(shape2[1]), max(shape2[1])+1):
# 		return False
# 	elif z not in range(min(shape2[2]), max(shape2[2])+1):
# 		return False
# 	else:
# 		return True

# 	print(i)

# print(len(empty))
# for i in empty:
# 	print(i, inbounds(i))

# def escape(c):
# 	x,y,z=c
# 	if not inbounds(c):
# 		# print(c,'escaped')
# 		return True
# 	for i in range(1000):
# 		near=getneighbors(x,y,z)
# 		near=[n for n in near if n not in shape]
# 		if len(near)==0:
# 			# print(c,'single cell')
# 			return False
# 		x,y,z=random.choice(near)
# 		if not inbounds((x,y,z)):
# 			# print(c, 'escaped')
# 			return True
# 	# print(c,'stuck?')
# 	return False

# gold=silver
# i=0
# for k,v in surface.items():
# 	print(f'{i} / {len(surface)}')
# 	for c in v:
# 		if not escape(c):
# 			gold-=1
# 	i+=1

# print(gold)