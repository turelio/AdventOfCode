#Start	9:52
#Part1	10:39
#Part2	10:56
#Total	64min

# Second pass, 1.6s
with open('input') as f:
	lista=f.read().splitlines()

import copy

grid=[['.' for i in range(1000)] for j in range(1000)]
max_y=0
lista=[[c.split(',') for c in l.split(' -> ')] for l in lista]
for l in lista:
	for i, coords in enumerate(l):
		x1,y1=int(coords[0]), int(coords[1])
		if y1>max_y:
			max_y=y1
		if i==0:
			x2,y2=x1,y1
		else:
			if x1==x2:
				if y1>y2:
					for j in range(y2,y1+1):
						grid[j][x1]='#'
				else:
					for j in range(y1,y2+1):
						grid[j][x1]='#'
			elif y1==y2:
				if x1>x2:
					for j in range(x2,x1+1):
						grid[y1][j]='#'
				else:
					for j in range(x1,x2+1):
						grid[y1][j]='#'
			x2,y2=x1,y1

grid2=copy.deepcopy(grid)
grid2[max_y+2]=['#' for i in range(1000)]

silver=0
over=0
while not over:
	y=0
	x=500
	while not over:
		if y+1>=1000:
			over=1
			break
		if grid[y+1][x]=='.':
			y+=1
		elif grid[y+1][x-1]=='.':
			y+=1
			x-=1
		elif grid[y+1][x+1]=='.':
			y+=1
			x+=1
		else:
			silver+=1
			grid[y][x]='o'
			break

over=0
gold=0
while not over:
	y=0
	x=500
	while not over:
		if grid2[y+1][x]=='.':
			y+=1
		elif grid2[y+1][x-1]=='.':
			y+=1
			x-=1
		elif grid2[y+1][x+1]=='.':
			y+=1
			x+=1
		else:
			if y==0 and x==500:
				grid2[y][x]='o'
				gold+=1
				over=1
				break
			gold+=1
			grid2[y][x]='o'
			break

print('Silver:', silver)
print('Gold:', gold)


# # First pass, 2.2s
# with open('input') as f:
# 	lista=f.read().splitlines()

# import copy

# grid=[['.' for i in range(1000)] for j in range(1000)]
# max_y=0
# lista=[[c.split(',') for c in l.split(' -> ')] for l in lista]
# # lista=lista[:4]
# for l in lista:
# 	# print(l)
# 	for i, coords in enumerate(l):
# 		x1,y1=int(coords[0]), int(coords[1])
# 		if y1>max_y:
# 			max_y=y1
# 		if i==0:
# 			x2,y2=x1,y1
# 			# print(f'\tstart at{x2,y2}')
# 		else:
# 			# print(f'\tfrom {x2,y2} to {x1,y1}:')
# 			if x1==x2:
# 				# print('\tsame x')
# 				if y1>y2:
# 					for j in range(y2,y1+1):
# 						# print(f'\t\twall at {x1,j}')
# 						grid[j][x1]='#'
# 				else:
# 					for j in range(y1,y2+1):
# 						# print(f'\t\twall at {x1,j}')
# 						grid[j][x1]='#'
# 			elif y1==y2:
# 				# print('\tsame y')
# 				if x1>x2:
# 					for j in range(x2,x1+1):
# 						# print(f'\t\twall at {j,y1}')
# 						grid[y1][j]='#'
# 				else:
# 					for j in range(x1,x2+1):
# 						# print(f'\t\twall at {j,y1}')
# 						grid[y1][j]='#'
# 			x2,y2=x1,y1
# grid2=copy.deepcopy(grid)
# silver=0
# over=0
# while True:
# 	y=0
# 	x=500
# 	if over:
# 		break
# 	while True:
# 		# print(f'at {x,y} {grid[y][x]}')
# 		if y+1>=1000:
# 			print(f'stop at {silver}')
# 			over=1
# 			break
# 		if grid[y+1][x]=='.':
# 			# print(f'moving down to {x, y+1} ({grid[y+1][x]})')
# 			y+=1
# 		elif grid[y+1][x-1]=='.':
# 			# print(f'moving left to {x-1, y+1} ({grid[y+1][x-1]})')
# 			# print('moving left')
# 			y+=1
# 			x-=1
# 		elif grid[y+1][x+1]=='.':
# 			# print(f'moving down to {x+1,y+1} ({grid[y+1][x+1]})')

# 			# print('moving right')
# 			y+=1
# 			x+=1
# 		else:
# 			silver+=1
# 			grid[y][x]='o'
# 			# print(f'stopped at\t{x,y}\t{grid[y][x]}\t{silver}')
# 			break

# print(max_y)
# grid2[max_y+2]=['#' for i in range(1000)]
# over=0
# gold=0
# while True:
# 	y=0
# 	x=500
# 	if over:
# 		break
# 	while True:
# 		# print(f'at {x,y} {grid[y][x]}')
# 		if grid2[y+1][x]=='.':
# 			# print(f'moving down to {x, y+1} ({grid[y+1][x]})')
# 			y+=1
# 		elif grid2[y+1][x-1]=='.':
# 			# print(f'moving left to {x-1, y+1} ({grid[y+1][x-1]})')
# 			# print('moving left')
# 			y+=1
# 			x-=1
# 		elif grid2[y+1][x+1]=='.':
# 			# print(f'moving down to {x+1,y+1} ({grid[y+1][x+1]})')

# 			# print('moving right')
# 			y+=1
# 			x+=1
# 		else:
# 			if y==0 and x==500:
# 				grid2[y][x]='o'
# 				# gold+=1
# 				print(f'over at {gold}')
# 				over=1
# 				break
# 			gold+=1
# 			grid2[y][x]='o'
# 			print(f'stopped at\t{x,y}\t{grid[y][x]}\t{gold}')
# 			break
# counter=0
# for i in grid2:
# 	for j in i:
# 		if j=='o':
# 			counter+=1
# print(counter) 