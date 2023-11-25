#Start	2023-11-25
#Part1	14:20	X
#Part2	
#Total
with open('input2') as f:
	lista=f.read().splitlines()
print(lista)

import copy, itertools
# manually parsed
r=[[0,1,0,1],[1,0,0,0],[0,0,1,0],[0,0,0,0]]
g=['HG','HM','LG','LM']
win=[1,1,1,1]
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

silver=[]
def solve(r,n=0,d=0,vis=set()):
	# print(f'############################\tstep {d}:')
	# drawf(r,n)
	# print(r)
	# add step to visited
	vis.add(str(n)+str(r))
	current=r[n]
	genes=current[::2]
	chips=current[1::2]
	# print(current,genes,chips)
	# check failure conditions:
	boom=False
	# if any chip and any generator:
	if sum(chips)!=0 and sum(genes)!=0:
		# check every chip
		for i,v in enumerate(chips):
			# if not here
			if v==0:
				continue
			# if doesn't have generator
			if genes[i]!=1:
				boom=True
				break
	if boom:
		# print('exploded')
		return
	# win condition
	if r[-1]==win:
		silver.append(d)
		print(f'found {d},{min(silver)}')
		return

	# check floor moves
	n2=[n-1,n+1]
	n2=[n3 for n3 in n2 if n3 in range(4)]
	# print(n2)

	# check possible items
	items=[]
	for i, v in enumerate(current):
		if v==1:
			items.append(i)
	moves=list(itertools.combinations(items,1))+list(itertools.combinations(items,2))
	# print(moves)
	# print()
	for n3 in n2:
		for items in moves:
			# print(len(moves), moves)
			r2=copy.deepcopy(r)
			for item in items:
				r2[n][item]=0
				r2[n3][item]=1
			if str(n3)+str(r2) in vis:
				continue
			else:
				# print('for',n3,items)
				# drawf(r2,n3)
				solve(r2,n3,d+1,copy.deepcopy(vis))
# i give up for now
solve(r)
