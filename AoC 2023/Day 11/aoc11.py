# 23-12-11
# Start	08:50	
# Part1	09:03	13min
# Part2	09:30	27min
# Total	40min
with open('input') as f:
	lista=f.read().splitlines()

test='''...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....'''.splitlines()
# lista=test
lista=[list(l) for l in lista]
# [print(''.join(l)) for l in lista]
# print(lista)
g3=[]
for y,v in enumerate(lista):
	for x,v2 in enumerate(v):
		if lista[y][x]=='#':
			g3.append([x,y])

y=0
ye=[]
for y,v in enumerate(lista):
	if '#' not in v:
		ye.append(y)
lista=list(zip(*lista))

x=0
xe=[]
for x,v in enumerate(lista):
	if '#' not in v:
		xe.append(x)
lista=list(zip(*lista))

import copy
print(g3,xe,ye)
gal=[]
for g in g3:
	print(g)
	entry=copy.deepcopy(g)
	for x in xe:
		if x<g[0]:
			entry[0]+=999999
	for y in ye:
		if y<g[1]:
			entry[1]+=999999
	gal.append(entry)
	print('\t',entry)

import itertools
pairs=list(itertools.combinations(gal,2))
print(len(pairs))
silver=0
for g1,g2 in pairs:
	silver+=abs(g1[0]-g2[0])+abs(g1[1]-g2[1])
print(silver)



# y=0
# while y<len(lista):
# 	if '#' in lista[y]:
# 		y+=1
# 	else:
# 		lista.insert(y,lista[y])
# 		y+=2
# # print('part1')
# # [print(''.join(l)) for l in lista]
# lista=list(zip(*lista))
# # [print(''.join(l)) for l in lista]
# y=0
# while y<len(lista):
# 	if '#' in lista[y]:
# 		y+=1
# 	else:
# 		lista.insert(y,lista[y])
# 		y+=2
# lista=list(zip(*lista))
# g=[]
# # [print(''.join(l)) for l in lista]
# # print('part2')
# for y,v in enumerate(lista):
# 	for x,v2 in enumerate(v):
# 		if lista[y][x]=='#':
# 			g.append((x,y))
# print(len(g))
# import itertools
# pairs=list(itertools.combinations(g,2))
# print(len(pairs))
# silver=0
# for g1,g2 in pairs:
# 	silver+=abs(g1[0]-g2[0])+abs(g1[1]-g2[1])
# print(silver)
# print(g3)