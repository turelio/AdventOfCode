# 2023-12-10
# Start	09:01	
# Part1	09:33	32min
# Part2	X	+48min
# Total	
with open('input') as f:
	lista=f.read().splitlines()
import copy
# |
test='''.....
.S-7.
.|.|.
.L-J.
.....'''.splitlines()
# lista=test
for y,v in enumerate(lista):
	lista[y]=list(lista[y])
	# print(lista)
	if 'S' in v:
		c=[v.index('S'), y]
		print(c)
		lista[y][v.index('S')]='|'

# [print(l) for l in lista]
start=copy.deepcopy(c)
prev='U'
c=start
pipes=set()
while True:
	# print(f'at {c} = {lista[c[1]][c[0]]}')
	stop=lista[c[1]][c[0]]
	pipes.add(tuple(c))
	if stop =='-':
		if prev=='R':
			c=[c[0]+1,c[1]]
			prev='R'
		elif prev=='L':
			c=[c[0]-1,c[1]]
			prev='L'
	elif stop =='|':
		if prev=='D':
			c=[c[0],c[1]+1]
			prev='D'
		elif prev=='U':
			c=[c[0],c[1]-1]
			prev='U'
	elif stop =='7':
		if prev=='R':
			c=[c[0],c[1]+1]
			prev='D'
		elif prev=='U':
			c=[c[0]-1,c[1]]
			prev='L'
		else:
			print('invalid')
			break
	elif stop =='J':
		if prev=='D':
			c=[c[0]-1,c[1]]
			prev='L'
		elif prev=='R':
			c=[c[0],c[1]-1]
			prev='U'
		else:
			print('invalid')
			break
	elif stop =='L':
		if prev=='L':
			c=[c[0],c[1]-1]
			prev='U'
		elif prev=='D':
			c=[c[0]+1,c[1]]
			prev='R'
		else:
			print('invalid')
			break
	elif stop =='F':
		if prev=='U':
			c=[c[0]+1,c[1]]
			prev='R'
		elif prev=='L':
			c=[c[0],c[1]+1]
			prev='D'
		else:
			print('invalid')
			break
	else:
		print(f'{stop} not specified')
		break
	if c==start:
		break

print(len(pipes)//2)
print(len(lista),len(lista[0]))
yr=len(lista)
xr=len(lista[0])
lista2=copy.deepcopy(lista)
for y,v in enumerate(lista2):
	for x,v2 in enumerate(v):
		if (x,y) not in pipes:
			lista2[y][x]='.'



# remove outer flood
outer=set()
outer.add((0,0))
visited=set()
while True:
	old=len(outer)
	for x,y in outer:
		if (x,y) in visited:
			continue
		near=[(x-1,y),(x+1,y),(x-1,y-1),(x,y-1),(x+1,y-1),(x-1,y+1),(x,y+1),(x+1,y+1)]
		near=[n for n in near if n[1] in range(xr) and n[0] in range(yr)]
		near=[n for n in near if lista2[n[1]][n[0]]=='.']
		# print(near)
		outer=outer.union(set(near))
		visited.add((x,y))
	print(len(outer))
	if len(outer)==old:
		break

for x,y in outer:
	print(lista2[y][x])
	lista2[y][x]=' '
	print(lista2[y][x])

[print(''.join(l)) for l in lista2]
tiles=0
for y in lista2:
	tiles+=y.count('.')
print(tiles)