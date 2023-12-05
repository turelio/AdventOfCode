# 2023-12-04
#Start	10:34
#Part1	10:53	19min
#Part2	11:05	12min
#Total	31min
import copy
with open('input') as f:
	lista=f.read().splitlines()

lista=[list(l) for l in lista]
yr=len(lista)
xr=len(lista[0])
states={}
i=0
while True:
	lista2=copy.deepcopy(lista)
	for y,v1 in enumerate(lista):
		for x,v2 in enumerate(v1):
			near=[(x+1,y),(x-1,y),(x-1,y+1),(x,y+1),(x+1,y+1),(x-1,y-1),(x,y-1),(x+1,y-1)]
			near=[n for n in near if n[0] in range(xr) and n[1] in range(yr)]
			near=[lista[n[1]][n[0]] for n in near]
			if v2=='.' and near.count('|')>=3:
				lista2[y][x]='|'
			elif v2=='|' and near.count('#')>=3:
				lista2[y][x]='#'
			elif v2=='#' and (near.count('#')==0 or near.count('|')==0):
				lista2[y][x]='.'
	lista=lista2
	entry=''.join([''.join(l) for l in lista])
	if i == 9:
		silver=entry.count('#')*entry.count('|')
	if entry not in states:
		print(f'new state at {i}')
		states[entry]=i
	else:
		delta=i-states[entry]
		print(f'repeat state from {states[entry]} at {i}, delta = {delta}')
		states[entry]=i
		if (999999999-i)%delta==0:
			gold=entry.count('#')*entry.count('|')
			break
	i+=1
print(silver,gold)
