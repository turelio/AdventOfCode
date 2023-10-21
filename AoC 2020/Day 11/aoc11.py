# 2023-10-21
#Start	17:03
#Part1	17:23	20min
#Part2	17:50	27min
#Total	47min
import copy
with open('input') as f:
	lista=f.read().splitlines()

lista=[list(l) for l in lista]

yrange=range(len(lista))
xrange=range(len(lista[0]))
i=0

lista3=copy.deepcopy(lista)
while True:
	print('round ',i)
	lista2=copy.deepcopy(lista)
	for y,v1 in enumerate(lista):
		for x,v2 in enumerate(v1):
			if lista[y][x]=='.':
				continue
			near=[(y,x+1),(y,x-1),(y+1,x),(y-1,x),(y+1,x+1),(y-1,x+1),(y+1,x-1),(y-1,x-1)]
			taken=0
			for y2,x2 in near:
				if y2 in yrange and x2 in xrange:
					if lista[y2][x2]=='#':
						taken+=1
			if lista[y][x]=='L' and taken==0:
				# print('taking seat')
				lista2[y][x]='#'
			if lista[y][x]=='#' and taken>=4:
				lista2[y][x]='L'
	if lista==lista2:
		print('stable')
		silver=0
		for l in lista:
			silver+=l.count('#')
		break
	else:
		lista=lista2
		i+=1

def gaze(board, y,x,y2,x2):
	y+=y2
	x+=x2
	while True:
		if y not in yrange or x not in xrange:
			return False
		if board[y][x]=='L':
			return False
		if board[y][x]=='#':
			return True
		y+=y2
		x+=x2


lista=lista3
i=0
while True:
	print('round ',i)
	lista2=copy.deepcopy(lista)
	for y,v1 in enumerate(lista):
		for x,v2 in enumerate(v1):
			if lista[y][x]=='.':
				continue
			near=[(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,1),(1,-1),(-1,-1)]
			taken=0
			for y2,x2 in near:
				if gaze(lista,y,x,y2,x2):
					taken+=1
			if lista[y][x]=='L' and taken==0:
				# print('taking seat')
				lista2[y][x]='#'
			if lista[y][x]=='#' and taken>=5:
				lista2[y][x]='L'
	if lista==lista2:
		print('stable')
		gold=0
		for l in lista:
			gold+=l.count('#')
		break
	else:
		lista=lista2
		i+=1

print(silver, gold)