# 2023-10-21
#Start	17:53
#Part1	18:14	19min
#Part2	18:33	19min
#Total	38min
with open('input') as f:
	lista=f.read().splitlines()


lista=[[l[0], int(l[1:])] for l in lista]

d=[[1,0],[0,-1],[-1,0],[0,1]]
t={'E':0,'S':1,'W':2,'N':3}

turn=0
pos=[0,0]
for c,v in lista:
	# print(c,v, pos, turn)
	if c=='F':
		pos[0]+=v*d[turn][0]
		pos[1]+=v*d[turn][1]
	elif c=='R':
		# 90 clockwise -> invert x and swap values
		rotate=v//90
		turn=(turn+rotate)%4
	elif c=='L':
		# 90 counterclockwise -> invert y and swap values
		rotate=v//90
		turn=(turn-rotate)%4
	else:
		pos[0]+=v*d[t[c]][0]
		pos[1]+=v*d[t[c]][1]

silver=(abs(pos[0])+abs(pos[1]))
print(pos, silver)


pos=[0,0]
way=[10,1]
for c,v in lista:
	print(c,v, pos, way)
	if c=='F':
		pos[0]+=v*way[0]
		pos[1]+=v*way[1]
	elif c=='R':
		rotate=v//90
		for _ in range(rotate):
			way[0]*=-1
			way.append(way.pop(0))
	elif c=='L':
		rotate=v//90
		for _ in range(rotate):
			way[1]*=-1
			way.append(way.pop(0))
	else:
		way[0]+=v*d[t[c]][0]
		way[1]+=v*d[t[c]][1]

silver=(abs(pos[0])+abs(pos[1]))
print(pos, silver)
