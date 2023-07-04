
#Start	12:20	20211222
#Part1	12:51	31min
#Part2	
#Total
import re
with open('input') as f:
	lista=f.read().splitlines()

lista2=lista[21:].copy()
lista=lista[:20]

cube=[[[0 for z in range(101)] for y in range(101)]for x in range(101)]
#print(lista)
commands=[]
for l in lista:
	command={}
	if 'on' in l:
		command["on"]=1
	else:
		command["on"]=0
	x = re.findall('-?\d+', l)
	command["x1"]=int(x[0])+50
	command["x2"]=int(x[1])+50
	command["y1"]=int(x[2])+50
	command["y2"]=int(x[3])+50
	command["z1"]=int(x[4])+50
	command["z2"]=int(x[5])+50
	commands.append(command)

for c in commands:
	for x in range(c["x1"],c["x2"]+1):
		for y in range(c["y1"],c["y2"]+1):
			for z in range(c["z1"],c["z2"]+1):
				if c["on"]==1:
					cube[x][y][z]=1
				else:
					cube[x][y][z]=0
silver=0
for x,v1 in enumerate(cube):
	for y,v2 in enumerate(v1):
		for z,v3 in enumerate(v2):
			if cube[x][y][z]==1:
				silver+=1

print(silver)

# def overlap2(x1,x2,y1,y2,z1,z2,a1,a2,b1,b2,c1,c2):
# 	vol1=(x2-x1+1)*(y2-y1+1)*(z2-z1+1)
# 	vol2=(a2-a1+1)*(b2-b1+1)*(c2-c1+1)
# 	overl=(max(min(a2,x2)-max(a1,x1),0)+1)*(max(min(b2,y2)-max(b1,y1),0)+1)*(max(min(c2,z2)-max(c1,z1),0)+1)
# 	return overl, vol1-overl


# def overlap(x1,x2,y1,y2,z1,z2,a1,a2,b1,b2,c1,c2):
# 	vol1=(x2-x1+1)*(y2-y1+1)*(z2-z1+1)
# 	vol2=(a2-a1+1)*(b2-b1+1)*(c2-c1+1)
# 	overl=(max(min(a2,x2)-max(a1,x1),0)+1)*(max(min(b2,y2)-max(b1,y1),0)+1)*(max(min(c2,z2)-max(c1,z1),0)+1)
# 	print(vol1, vol2, overl, vol1-overl)

# gold
# on_count=(commands[0]["x2"]-commands[0]["x1"]+1)*(commands[0]["y2"]-commands[0]["y1"]+1)*(commands[0]["z2"]-commands[0]["z1"]+1)
# prev_list=[commands[0]]

# print(on_count, prev_list)
# for c in commands[1:]:
# 	if c["on"]==1:
# 		on_count+=(c["x2"]-c["x1"]+1)*(c["y2"]-c["y1"]+1)*(c["z2"]-c["z1"]+1)
# 		for p in prev_list:
# 			result=overlap2(c["x1"],c["x2"],c["y1"],c["y2"],c["z1"],c["z2"],p["x1"],p["x2"],p["y1"],p["y2"],p["z1"],p["z2"])

