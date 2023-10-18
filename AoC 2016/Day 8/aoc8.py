# 2023-10-17
#Start	17:15
#Part1	18:17 62min
#Part2	18:18 1min
#Total	63min
import re

with open('input') as f:
	lista=f.read().splitlines()


def rect(board, x,y):
	for i in range(y):
		for j in range(x):
			board[i][j]=1
	return board

def rotate(board, direction, i,n):
	if direction=='y':
		for j in range(n):
			temp=[board[i].pop()]
			board[i]=temp+board[i]
	if direction=='x':


		board=list(zip(*board))
		board=[list(x) for x in board]

		for j in range(n):
			temp=[board[i].pop()]
			board[i]=temp+board[i]
	
		board=list(zip(*board))
		board=[list(x) for x in board]

	return board

def print_board(board):
	for row in board:
		row=[str(r) for r in row]
		row=''.join(row)
		row=row.replace('0',' ')
		row=row.replace('1','█')
		print(row)

board=[[0 for i in range(50)]for i in range(6)]
print_board(board)
for l in lista:
	print(l)
	if l[1]=='o':
		instr=re.match(r'rotate \w* (\w)=(\d*) by (\d*)', l).groups()
		board=rotate(board,instr[0], int(instr[1]), int(instr[2]))
	else:
		instr=re.match(r'rect (\d*)x(\d*)', l).groups()
		board=rect(board, int(instr[0]), int(instr[1]))
	print_board(board)

silver=sum([b.count(1) for b in board])

print(silver)
# gold = UPOJFLBCEZ