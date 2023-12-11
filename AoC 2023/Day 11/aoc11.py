# 23-12-11
# Start	08:50	
# Part1	09:03	13min
# Part2	09:30	27min
# Total	40min
import copy, itertools
with open('input') as f:
	lista=f.read().splitlines()
lista=[list(l) for l in lista]

# galaxy coordinates
galaxies=[]
for y,v in enumerate(lista):
	for x,v2 in enumerate(v):
		if lista[y][x]=='#':
			galaxies.append([x,y])

# save indices of empty rows and columns
y, ye=0,[]
for y,v in enumerate(lista):
	if '#' not in v:
		ye.append(y)

x,xe=0,[]
for x,v in enumerate(list(zip(*lista))):
	if '#' not in v:
		xe.append(x)

# increment coordinate by n if row/column is before it
def solve(galaxies,n):
	galaxies2=[]
	for g in galaxies:
		entry=copy.deepcopy(g)
		for x in xe:
			if x<g[0]:
				entry[0]+=n
		for y in ye:
			if y<g[1]:
				entry[1]+=n
		galaxies2.append(entry)

	# manhattan distance on pairs
	pairs=list(itertools.combinations(galaxies2,2))
	result=0
	for g1,g2 in pairs:
		result+=abs(g1[0]-g2[0])+abs(g1[1]-g2[1])
	return result

print('Silver:', solve(galaxies,1))
print('Gold:', solve(galaxies,999999))
