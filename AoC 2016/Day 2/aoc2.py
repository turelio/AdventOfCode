#Start	11:09	20211218	
#Part1	11:28 	19min
#Part2	11:37	9min
#Total	28min
with open('input') as f:
	lista=f.read().strip().splitlines()

keypad=[[1,2,3],[4,5,6],[7,8,9]]
keypad2=[[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,"A", "B", "C",0],[0,0,"D",0,0]]
def decode(n,y,x):
	for i in n:
		if i=="U":
			if y-1>=0:
				y-=1
		elif i=="L":
			if x-1>=0:
				x-=1
		elif i=="R":
			if x+1<=2:
				x+=1
		elif i=="D":
			if y+1<=2:
				y+=1
	return y,x

def decode2(n,y,x):
	for i in n:
		if i=="U":
			if y-1>=0:
				if keypad2[y-1][x]!=0:
					y-=1
		elif i=="L":
			if x-1>=0:
				if keypad2[y][x-1]!=0:
					x-=1
		elif i=="R":
			if x+1<=4:
				if keypad2[y][x+1]!=0:
					x+=1
		elif i=="D":
			if y+1<=4:
				if keypad2[y+1][x]!=0:
					y+=1
	return y,x

coord=[1,1]
coord2=[2,2]
silver=[]
gold=[]
for l in lista:
	coord=decode(l, coord[0],coord[1])
	coord2=decode2(l, coord2[0],coord2[1])
	silver.append(keypad[coord[0]][coord[1]])
	gold.append(keypad2[coord2[0]][coord2[1]])
print(silver)
print(gold)