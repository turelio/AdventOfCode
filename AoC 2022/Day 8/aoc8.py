#Start	9:16
#Part1	10:00
#Part2	10:49
#Total	93min

with open('input') as f:
	lista=f.read().splitlines()

grid=[[int(k) for k in list(l)] for l in lista]

def checker(y,x, grid):
	if x==0 or y==0 or x==len(grid)-1 or y==len(grid)-1:
		return 1,True
	grid2=[list(i) for i in list(zip(*grid))]
	checks=[grid2[x][:y],grid[y][:x],grid[y][x+1:],grid2[x][y+1:]]
	vis=4
	gold1=1
	for odd,i in enumerate(checks):
		if odd<2:
			i=list(reversed(i))
		if max(i)>=grid[y][x]:
			vis-=1
		for k,v in enumerate(list(i)):
			if v>=grid[y][x] or k==len(i)-1:
				gold1=gold1*(k+1)
				break
	if vis>0:
		return gold1,True
	else:
		return gold1,False
silver=0
gold=[]

for y,v1 in enumerate(grid):
	for x,v2 in enumerate(v1):
		g1,s1=checker(y,x,grid)
		if s1:
			silver+=1
		gold.append(g1)

print(silver, max(gold))





## First pass, 2s
# with open('input') as f:
# 	lista=f.read().splitlines()

# lista=[[int(k) for k in list(l)] for l in lista]
# test='''30373
# 25512
# 65332
# 33549
# 35390'''
# test=test.split('\n')
# test=[[int(k) for k in list(l)] for l in test]
# # print(lista,len(lista), len(lista[0]))
# grid=lista

# def checker(y,x, grid):
# 	if x==0 or y==0 or x==len(grid)-1 or y==len(grid)-1:
# 		# print(f'exterior {y}-{x} visible')
# 		return 1,True
# 	print(f'check {y}-{x}, value {grid[y][x]}:')
# 	grid2=list(zip(*grid))
# 	grid2=[list(i) for i in grid2]
# 	# print(grid2)
# 	# print(type(grid2), type(grid2[0]))
# 	checks=[grid2[x][:y],grid[y][:x],grid[y][x+1:],grid2[x][y+1:]]
# 	vis=4
# 	gold1=1
# 	for odd,i in enumerate(checks):
# 		if odd<2:
# 			i=list(reversed(i))
# 		if max(i)>=grid[y][x]:
# 			vis-=1
# 		print(f'check {grid[y][x]} against {i}: ', end='')
# 		for k,v in enumerate(list(i)):
# 			if v>=grid[y][x] or k==len(i)-1:
# 				gold1=gold1*(k+1)
# 				print(k+1, ', total', gold1)
# 				break
# 	print('')
# 	if vis>0:
# 		return gold1,True
# 	else:
# 		return gold1,False
# silver=0

# gold=[]

# for y,v1 in enumerate(grid):
# 	for x,v2 in enumerate(v1):
# 		g1,s1=checker(y,x,grid)
# 		if s1:
# 			silver+=1
# 		gold.append(g1)

# print(silver, max(gold))
