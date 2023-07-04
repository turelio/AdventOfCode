#Start	10:15
#Part1	11:30
#Part2	12:05
#Total	110min

## Second pass, 137ms
with open('input') as f:
	lista=f.read().splitlines()

lista=[(l[0], int(l[2:])) for l in lista]

def follow(head, tail):
	rel=[head[0]-tail[0], head[1]-tail[1]]
	if rel[0]>=-1 and rel[0]<=1 and rel[1]>=-1 and rel[1]<=1:
		return tail
	elif rel[0]==0:
		if rel[1]==2:
			tail[1]+=1
		elif rel[1]==-2:
			tail[1]-=1
		return tail
	elif rel[1]==0:
		if rel[0]==2:
			tail[0]+=1
		elif rel[0]==-2:
			tail[0]-=1
		return tail
	elif rel in [[-2,1],[-1,2],[-2,2]]:
		tail[0]-=1
		tail[1]+=1
		return tail
	elif rel in [[2,1],[1,2],[2,2]]:
		tail[0]+=1
		tail[1]+=1
		return tail
	elif rel in [[-1,-2],[-2,-1],[-2,-2]]:
		tail[0]-=1
		tail[1]-=1
		return tail
	elif rel in [[1,-2],[2,-1],[2,-2]]:
		tail[0]+=1
		tail[1]-=1
		return tail

def snek(lista, n):
	visited=set()
	rope=[[0,0] for i in range(n)]
	for l in lista:
		for i in range(l[1]):	
			if l[0]=='R':
				rope[0][0]+=1
			elif l[0]=='L':
				rope[0][0]-=1
			elif l[0]=='U':
				rope[0][1]+=1
			elif l[0]=='D':
				rope[0][1]-=1
			for j in range(1,n):
				rope[j]=follow(rope[j-1], rope[j])
			visited.add(f'{rope[n-1][0]},{rope[n-1][1]}')
	return len(visited)

print(snek(lista, 2),snek(lista,10))


## First pass, 430ms
# import copy

# with open('input') as f:
# 	lista=f.read().splitlines()

# lista=[(l[0], int(l[2:])) for l in lista]

# test='''R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2'''
# test=test.split('\n')
# test=[(t[0], int(t[2:])) for t in test]
# print(test)
# # lista=test
# silver=set()
# head=[0,0]
# tail=[0,0]
# grid=[['.' for j in range(6)] for i in range(5)]
# # x,y

# def follow(head, tail, direction):
# 	samerow=head[1]==tail[1]
# 	samecol=head[0]==tail[0]
# 	rel=[head[0]-tail[0], head[1]-tail[1]]
# 	# print(f'relative {rel[0]},{rel[1]}')
# 	# print(f'head {head} to tail {tail}, relative pos {rel}')
# 	# 1 to 9: same place
# 	if rel[0] in [-1,0,1] and rel[1] in [-1,0,1]:
# 		return tail
# 	# 10,11
# 	elif rel[0]==0:
# 		if rel[1]==2:
# 			tail[1]+=1
# 		elif rel[1]==-2:
# 			tail[1]-=1
# 	# 12,13
# 	elif rel[1]==0:
# 		if rel[0]==2:
# 			tail[0]+=1
# 		elif rel[0]==-2:
# 			tail[0]-=1
# 	# 14,15
# 	elif rel in [[-2,1],[-1,2],[-2,-2]]:
# 		tail[0]-=1
# 		tail[1]+=1
# 	# 16,17
# 	elif rel in [[2,1],[1,2],[2,2]]:
# 		tail[0]+=1
# 		tail[1]+=1
# 	# 18,19
# 	elif rel in [[-1,-2],[-2,-1],[-2,-2]]:
# 		tail[0]-=1
# 		tail[1]-=1
# 	# 20,21
# 	elif rel in [[1,-2],[2,-1],[2,-2]]:
# 		tail[0]+=1
# 		tail[1]-=1
# 	return tail

# for l in lista:
# 	# print(l[0], l[1])
# 	for i in range(l[1]):	
# 		if l[0]=='R':
# 			head[0]+=1
# 		elif l[0]=='L':
# 			head[0]-=1
# 		elif l[0]=='U':
# 			head[1]+=1
# 		elif l[0]=='D':
# 			head[1]-=1
# 		tail=follow(head, tail, l[0])
# 		# pos=copy.deepcopy(grid)
# 		# pos[tail[1]][tail[0]]='T'
# 		# pos[head[1]][head[0]]='H'
# 		# pos=pos[::-1]
# 		# for i in pos:
# 		# 	print(''.join(i))
# 		# print('')
# 		silver.add(f'{tail[0]},{tail[1]}')


# gold=set()


# rope=[[0,0] for i in range(10)]

# def follow2(head, tail, direction):
# 	samerow=head[1]==tail[1]
# 	samecol=head[0]==tail[0]
# 	rel=[head[0]-tail[0], head[1]-tail[1]]
# 	# print(f'relative {rel[0]},{rel[1]}')
# 	# print(f'head {head} to tail {tail}, relative pos {rel}')
# 	# 1 to 9: same place
# 	if rel[0] in [-1,0,1] and rel[1] in [-1,0,1]:
# 		return tail
# 	# 10,11
# 	elif rel[0]==0:
# 		if rel[1]==2:
# 			tail[1]+=1
# 		elif rel[1]==-2:
# 			tail[1]-=1
# 	# 12,13
# 	elif rel[1]==0:
# 		if rel[0]==2:
# 			tail[0]+=1
# 		elif rel[0]==-2:
# 			tail[0]-=1
# 	# 14,15
# 	elif rel in [[-2,1],[-1,2],[-2,2]]:
# 		tail[0]-=1
# 		tail[1]+=1
# 	# 16,17
# 	elif rel in [[2,1],[1,2],[2,2]]:
# 		tail[0]+=1
# 		tail[1]+=1
# 	# 18,19
# 	elif rel in [[-1,-2],[-2,-1],[-2,-2]]:
# 		tail[0]-=1
# 		tail[1]-=1
# 	# 20,21
# 	elif rel in [[1,-2],[2,-1],[2,-2]]:
# 		tail[0]+=1
# 		tail[1]-=1
# 	return tail

# # lista=test
# for l in lista:
# 	for i in range(l[1]):	
# 		if l[0]=='R':
# 			rope[0][0]+=1
# 		elif l[0]=='L':
# 			rope[0][0]-=1
# 		elif l[0]=='U':
# 			rope[0][1]+=1
# 		elif l[0]=='D':
# 			rope[0][1]-=1
# 		pos=copy.deepcopy(grid)
# 		for j in range(1,10):
# 			rope[j]=follow2(rope[j-1], rope[j], l[1])
# 		# 	pos[rope[j][1]][rope[j][0]]=str(j)
# 		# print(rope)
# 		# pos[rope[0][1]][rope[0][0]]='0'
# 		# pos=pos[::-1]
# 		# for i in pos:
# 		# 	print(''.join(i))
# 		# print('')

# 		# tail=follow(head, tail, l[0])
# 		# print('')
# 		gold.add(f'{rope[9][0]},{rope[9][1]}')

# print(rope)


# print(len(silver), len(gold))
