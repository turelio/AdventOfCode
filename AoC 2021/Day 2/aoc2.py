# 15 min
with open('input') as f:
	lista=[l.split(" ") for l in f.read().splitlines()]

depth1, depth2, position1, position2, aim2=0,0,0,0,0
for l in lista:
	if l[0]=="forward":
		position1+=int(l[1])
		position2+=int(l[1])
		depth2+=aim2*int(l[1])
	elif l[0]=="down":
		depth1+=int(l[1])
		aim2+=int(l[1])
	else:
		depth1-=int(l[1])
		aim2-=int(l[1])

print(depth1*position1, depth2*position2)