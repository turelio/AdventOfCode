#Start	14:30
#Part1	15:59
#Part2	16:19
#Total	111min

# Second pass, 180s
import copy
with open('input') as f:
	lista=f.read().splitlines()

elves=[]
for y,v1 in enumerate(lista):
	for x,v2 in enumerate(v1):
		if v2=='#':
			elves.append([(x,y),(x,y)])

r=0
queue=['n','s','w','e']
while True:
	if r==10:
		silver=copy.deepcopy(elves)
	stopped=0
	# print('Round',r+1)
	# print('\tFinding new positions')
	positions=set(list(zip(*elves))[0])
	for i,e in enumerate(elves):
		x,y=e[0]
		near=[(x+1,y),(x+1,y+1), (x+1,y-1), (x,y+1), (x,y-1),(x-1,y),(x-1,y-1),(x-1,y+1)]
		elves[i][1]=elves[i][0]
		if len(positions & set(near))==0:
			stopped+=1
		else:
			for o in queue:
				if o=='n':
					if not {(x-1,y-1),(x,y-1),(x+1,y-1)}&positions:
						elves[i][1]=(x,y-1)
						break
				elif o=='s':
					if not {(x-1,y+1),(x,y+1),(x+1,y+1)}&positions:
						elves[i][1]=(x,y+1)
						break
				elif o=='w':
					if not {(x-1,y-1),(x-1,y),(x-1,y+1)}&positions:
						elves[i][1]=(x-1,y)
						break
				elif o=='e':
					if not {(x+1,y-1),(x+1,y),(x+1,y+1)}&positions:
						elves[i][1]=(x+1,y)
						break
	# print('\tAttempting to move')
	news=list(zip(*elves))[1]
	stopping=set()
	for i2,e2 in enumerate(elves):
		if e2[1] in stopping:
			continue
		elif news.count(e2[1])==1:
			elves[i2][0]=elves[i2][1]
		else:
			stopping.add(e2[1])
	queue.append(queue.pop(0))
	# print('Round',r+1,'\t',stopped,'/',len(elves))
	if stopped==len(elves):
		break
	r+=1

silver=list(zip(*silver))[0]
silver2=silver
silver=list(zip(*silver))
print('Silver:', (max(silver[0])-min(silver[0])+1)*(max(silver[1])-min(silver[1])+1)-len(silver2))
print('Gold:', r+1)

# # First pass, 193s
# import copy
# with open('input') as f:
# 	lista=f.read().splitlines()

# print(lista, len(lista), len(lista[0]))


# elves=[]
# for y,v1 in enumerate(lista):
# 	for x,v2 in enumerate(v1):
# 		# print(v2)
# 		if v2=='#':
# 			elf=dict()
# 			elf['c']=(x,y)	
# 			elf['o']=['n','s','w','e']
# 			elves.append(elf)
# for i in elves:
# 	print(i)

# print(len(elves),'elves')
# # for r in range(10):
# r=0
# while True:
# 	if r==10:
# 		silver2=copy.deepcopy(elves)
# 	stopped=0
# 	print('Round',r+1)
# 	print('\tFinding new positions')
# 	positions=set()
# 	for e in elves:
# 		positions.add(e['c'])
# 	# print(len(positions),'elves')
# 	for i,e in enumerate(elves):
# 		x,y=e['c']
# 		alone=True
# 		near=[(x+1,y),(x+1,y+1), (x+1,y-1), (x,y+1), (x,y-1),(x-1,y),(x-1,y-1),(x-1,y+1)]
# 		if len(positions & set(near))!=0:
# 				alone=False
# 		if alone:
# 			elves[i]['n']=elves[i]['c']
# 			elves[i]['d']='x'
# 			stopped+=1
# 		else:
# 			elves[i]['n']=elves[i]['c']
# 			elves[i]['d']='x'
# 			for o in e['o']:
# 				if o=='n':
# 					if (x-1,y-1) not in positions and (x,y-1) not in positions and (x+1,y-1) not in positions:
# 						elves[i]['n']=(x,y-1)
# 						elves[i]['d']='n'
# 						break
# 				elif o=='s':
# 					if (x-1,y+1) not in positions and (x,y+1) not in positions and (x+1,y+1) not in positions:
# 						elves[i]['n']=(x,y+1)
# 						elves[i]['d']='s'
# 						break
# 				elif o=='w':
# 					if (x-1,y-1) not in positions and (x-1,y) not in positions and (x-1,y+1) not in positions:
# 						elves[i]['n']=(x-1,y)
# 						elves[i]['d']='w'
# 						break
# 				elif o=='e':
# 					if (x+1,y-1) not in positions and (x+1,y) not in positions and (x+1,y+1) not in positions:
# 						elves[i]['n']=(x+1,y)
# 						elves[i]['d']='e'
# 						break
# 	print('\tAttempting to move')
# 	news=[]
# 	for i1,e1 in enumerate(elves):
# 		news.append(e1['n'])
# 	print(len(news))
# 	for i2,e2 in enumerate(elves):
# 		if news.count(e2['n'])==1:
# 			elves[i2]['c']=elves[i2]['n']
# 	print('\tShuffling considerations')
# 	for i1,e1 in enumerate(elves):
# 		elves[i1]['o'].append(elves[i1]['o'].pop(0))
# 	print(stopped,'/',len(elves))
# 	if stopped==len(elves):
# 		break
# 	r+=1

# silver=[]
# for e in silver2:
# 	silver.append(e['c'])
# silver2=silver
# silver=list(zip(*silver))
# print('Silver:', (max(silver[0])-min(silver[0])+1)*(max(silver[1])-min(silver[1])+1)-len(silver2))
# print('Gold:', r+1)


# # First pass,
# import copy
# with open('input') as f:
# 	lista=f.read().splitlines()

# print(lista, len(lista), len(lista[0]))


# elves=[]
# for y,v1 in enumerate(lista):
# 	for x,v2 in enumerate(v1):
# 		# print(v2)
# 		if v2=='#':
# 			elf=dict()
# 			elf['c']=(x,y)	
# 			elf['o']=['n','s','w','e']
# 			elves.append(elf)
# for i in elves:
# 	print(i)

# print(len(elves),'elves')
# # for r in range(10):
# r=0
# while True:
# 	if r==10:
# 		silver2=copy.deepcopy(elves)
# 	stopped=0
# 	print('Round',r+1)
# 	print('\tFinding new positions')
# 	positions=set()
# 	for e in elves:
# 		positions.add(e['c'])
# 	# print(len(positions),'elves')
# 	for i,e in enumerate(elves):
# 		x,y=e['c']
# 		alone=True
# 		near=[(x+1,y),(x+1,y+1), (x+1,y-1), (x,y+1), (x,y-1),(x-1,y),(x-1,y-1),(x-1,y+1)]
# 		if len(positions & set(near))!=0:
# 				alone=False
# 		if alone:
# 			elves[i]['n']=elves[i]['c']
# 			elves[i]['d']='x'
# 			stopped+=1
# 		else:
# 			elves[i]['n']=elves[i]['c']
# 			elves[i]['d']='x'
# 			for o in e['o']:
# 				if o=='n':
# 					if (x-1,y-1) not in positions and (x,y-1) not in positions and (x+1,y-1) not in positions:
# 						elves[i]['n']=(x,y-1)
# 						elves[i]['d']='n'
# 						break
# 				elif o=='s':
# 					if (x-1,y+1) not in positions and (x,y+1) not in positions and (x+1,y+1) not in positions:
# 						elves[i]['n']=(x,y+1)
# 						elves[i]['d']='s'
# 						break
# 				elif o=='w':
# 					if (x-1,y-1) not in positions and (x-1,y) not in positions and (x-1,y+1) not in positions:
# 						elves[i]['n']=(x-1,y)
# 						elves[i]['d']='w'
# 						break
# 				elif o=='e':
# 					if (x+1,y-1) not in positions and (x+1,y) not in positions and (x+1,y+1) not in positions:
# 						elves[i]['n']=(x+1,y)
# 						elves[i]['d']='e'
# 						break
# 	print('\tAttempting to move')
# 	news=[]
# 	for i1,e1 in enumerate(elves):
# 		news.append(e1['n'])
# 	print(len(news))
# 	for i2,e2 in enumerate(elves):
# 		if news.count(e2['n'])==1:
# 			elves[i2]['c']=elves[i2]['n']
# 	print('\tShuffling considerations')
# 	for i1,e1 in enumerate(elves):
# 		elves[i1]['o'].append(elves[i1]['o'].pop(0))
# 	print(stopped,'/',len(elves))
# 	if stopped==len(elves):
# 		break
# 	r+=1

# silver=[]
# for e in silver2:
# 	silver.append(e['c'])
# silver2=silver
# silver=list(zip(*silver))
# print('Silver:', (max(silver[0])-min(silver[0])+1)*(max(silver[1])-min(silver[1])+1)-len(silver2))
# print('Gold:', r+1)
