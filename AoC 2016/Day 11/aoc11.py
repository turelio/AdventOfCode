#Start	2023-11-25
#Part1	14:20	X
#Part2	
#Total
with open('input2') as f:
	lista=f.read().splitlines()
# print(lista)
import sys

# sys.setrecursionlimit(100000)
# The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
# The second floor contains a hydrogen generator.
# The third floor contains a lithium generator.
# The fourth floor contains nothing relevant.

# The first floor contains a polonium generator, a thulium generator, a thulium-compatible microchip, a promethium generator, a ruthenium generator, a ruthenium-compatible microchip, a cobalt generator, and a cobalt-compatible microchip.
# The second floor contains a polonium-compatible microchip and a promethium-compatible microchip.
# The third floor contains nothing relevant.
# The fourth floor contains nothing relevant.

import copy, itertools
# manually parsed
r=[[0,1,0,1],[1,0,0,0],[0,0,1,0],[0,0,0,0]]
g=['HG','HM','LG','LM']
win=[1,1,1,1]
r=[[1,0,1,1,1,0,1,1,1,1],[0,1,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
g=['PoG','PoM','ThG','ThM','PrG','PrM','RuG','RuM','CoG','CoM']
win=[1]*10
empty=[0]*10
print('moves')
# base_moves=[[i] for i,v in enumerate(g)]
# print(base_moves)
# base_moves+=[[i,i+1] for i in range(0,len(g),2)]
base_moves=list(itertools.combinations(range(len(g)),1))+list(itertools.combinations(range(len(g)),2))
print(base_moves)

def drawf(r,n):
	f=4
	for floor in r[::-1]:
		print(f'F{f}', end='\t')
		if n+1==f:
			print('E',end='\t')
		else:
			print('.',end='\t')

		for j,fl in enumerate(floor):
			if fl:
				print(g[j], end='\t')
			else:
				print('.', end='\t')
		print('')
		f-=1
	print()

silver=[72]

def isvalid(r):
	for floor in r:
		genes=floor[::2]
		chips=floor[1::2]
		# if any chip and any generator:
		if sum(chips)!=0 and sum(genes)!=0:
			# check every chip
			for i,v in enumerate(chips):
				# if not here
				if v==0:
					continue
				# if doesn't have generator
				if genes[i]!=1:
					return False
	return True
bad=set()
def solve(r,n=0,d=0,vis=set()):
	if len(silver)>1:
		print(len(vis),len(bad))
	if d>=min(silver):
		return
	# print(silver)
	if r[-1]==win:
		silver.append(d)
		print(f'found {d}')
		return
	# print(f'############################\tstep {d}:')
	# drawf(r,n)

	# add step to visited
	vis.add(str(n)+str(r))
	current=r[n]

	# check floor moves
	floors=[]
	if n+1 in range(4):
		floors.append(n+1)
	if n-1 in range(4):
		if r[n-1]!=empty:
			floors.append(n-1)
	# floors=[n2 for n2 in floors if n2 in range(4)]

	# print(n2)

	# check possible items
	moves2=copy.deepcopy(base_moves)
	moves3=[]
	for move in moves2:
		valid=True
		for element in move:
			if current[element]==0:
				valid=False
		if valid:
			moves3.append(move)
	# print(len(moves3))
	moves4=[]
	for n2 in floors:
		for move in moves3:
			r2=copy.deepcopy(r)
			for item in move:
				r2[n][item]=0
				r2[n2][item]=1
			if str(n2)+str(r2) in vis or str(n2)+str(r2) in bad:
				continue
			if not isvalid(r2):
				bad.add(str(n2)+str(r2))
			else:
				moves4.append([n2,r2])
	# print(len(moves3)*len(floors), len(moves4))
	if len(moves4)==0:
		bad.add(str(n)+str(r))
	else:
		for n2,r2 in moves4:
			solve(r2,n2,d+1,copy.deepcopy(vis))
	# print('\t going up?')
	return 'eh?'

# print(solve(r))
# print(min(silver))