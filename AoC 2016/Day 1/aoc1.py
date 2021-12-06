#Start	13:40
#Part1	14:03	23min
#Part2	14:34	31min
#Total	54min
with open('input') as f:
	lista=f.read().strip().split(', ')

#	0
#3 		1
#	2
# directions

def changedir(direction,n):
	if n=="R":
		direction+=1
		if direction==4:
			direction=0
	else:
		direction-=1
		if direction==-1:
			direction=3
	return direction

def check_cross(x,y,lista):
	if [x,y] in lista:
		print(f"crossed {abs(x)+abs(y)} units away")


pos_list=[[0,0]]

direction,x,y,x1,y1=0,0,0,0,0
for l in lista:
	n=l[0]
	mv=int(l[1:])
	direction=changedir(direction, n)
	#print(f"position {x}:{y}, moving {mv} units in direction {direction}")
	if direction==0:
		for i in range(1, mv+1):
			y+=1
			check_cross(x,y,pos_list)
			pos_list.append([x,y])
		y1+=mv
	elif direction==1:
		for i in range(1, mv+1):
			x+=1
			check_cross(x,y,pos_list)
			pos_list.append([x,y])
		x1+=mv
	elif direction==2:
		for i in range(1, mv+1):
			y-=1
			check_cross(x,y,pos_list)
			pos_list.append([x,y])
		y1-=mv
	else:
		for i in range(1, mv+1):
			x-=1
			check_cross(x,y,pos_list)
			pos_list.append([x,y])
		x1-=mv
	#print(f"Turn {l[0]}, {l[1:]} steps, direction {direction}, position x: {x} y: {y}, position x: {x1} y: {y1}")

print(abs(x)+abs(y))