# 2023-10-18
#Start	11:14
#Part1	11:27	13min
#Part2	12:24	53min	
#Total	66min
# long and messy but fast

with open('input') as f:
	lista=f.read().splitlines()

pre={}
for l in lista:
	l=l.split()

	step=l[-3]
	req=l[1]
	if step not in pre:
		pre[step]=set()
	if req not in pre:
		pre[req]=set()
	pre[step].add(req)

print(pre)
silver=[]
while len(pre)!=0:
	moves=[]
	for step, req in pre.items():
		if len(req)==0:
			moves.append(step)
	print(f'possible steps: {moves}')
	moves=sorted(moves)[0]
	print(f'choosing {moves}')
	silver.append(moves)
	del pre[moves]
	for step in pre:
		if moves in pre[step]:
			pre[step].remove(moves)
print(''.join(silver))

workers=5
time=60

pre={}
for l in lista:
	l=l.split()

	step=l[-3]
	req=l[1]
	if step not in pre:
		pre[step]=set()
	if req not in pre:
		pre[req]=set()
	pre[step].add(req)
gold=[]
s=0

workers=[[None,None] for w in range(workers)]
print()
while len(pre)!=0:
	for i,w in enumerate(workers):
		if w[0]==None:

			continue
		elif w[1]==0:
			# print(f'{w[0]} done, deleting')
			gold.append(w[0])
			del pre[w[0]]
			for step in pre:
				if w[0] in pre[step]:
					pre[step].remove(w[0])	
			workers[i]=[None,None]
		else:
			workers[i][1]-=1

	moves=[]
	# print(pre)
	for step, req in pre.items():
		if len(req)==0:
			moves.append(step)

	moves=sorted(moves)
	# print(f'possible steps: {moves}')

	for i,w in enumerate(workers):
		# print(f'look at worker {i}')
		if w[0]!=None:
			# print('\ttaken')
			continue
		elif len(moves)!=0:
			for task in moves:
				taken=False
				# print(task)
				for w2 in workers:
					if w2[0]==task:
						taken=True
				if not taken:
					# print(f'assigning {task} to worker {i}')				
					workers[i][0]=task
					workers[i][1]=ord(task)-64+time-1
					

	print(f'{s}\t{workers[0]}\t{workers[1]}\t{"".join(gold)}')
	s+=1
print(''.join(silver))