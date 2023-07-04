#Start	11:17	20211215	
#Part1	
#Part2	
#Total
#this shit doesn't work anymore for part 2 real input??
import math
with open('input2') as f:
	lista=f.read().splitlines()

lista=[[int(i) for i in l] for l in lista]


def increment_row(row):
	row=list(map(lambda x:x+1, row))
	for c1,l in enumerate(row):
		if l>9:
			row[c1]=l%9
	return row

newlista=[]
for y,c in enumerate(lista):
	newlista.append(c+list(map(lambda x:x+1, c))+list(map(lambda x:x+2, c))+list(map(lambda x:x+3, c))+list(map(lambda x:x+4, c)))
	for c1,l in enumerate(newlista[y]):
		if l>9:
			newlista[y][c1]=l%9

for i in range(4):
	lenn=len(lista)*-1
	lista2=newlista[lenn:]
	for c,v in enumerate(lista2):
		lista2[c]=increment_row(v)
	newlista+=lista2

lista=newlista.copy()
costs=[[math.inf for i in l] for l in lista]
visited=[[0 for i in l] for l in lista]
costs[0][0]=0
print(len(lista), len(lista[0]))
def drawc():
	for l,c in zip(lista, costs):
		print(l,c)

def get_kolejka():
	kolejka=[]
	for y,v1 in enumerate(lista):
		for x,v2 in enumerate(v1):
			if visited[y][x]==0:
				kolejka.append([y,x,costs[y][x]])
	kolejka.sort(key=lambda x:x[2])
	return kolejka

kolejka=get_kolejka()
while len(kolejka)!=0:
	kolejka.sort(key=lambda x:x[2])
	y=kolejka[0][0]
	x=kolejka[0][1]
	kolejka.pop(0)
	print(f"{len(kolejka)} left")
	visited[y][x]=1
	near=[]
	if x+1<len(lista):
		near.append([y,x+1,lista[y][x+1]])
	if x>0:
		near.append([y,x-1,lista[y][x-1]])	
	if y+1<len(lista):
		near.append([y+1,x,lista[y+1][x]])
	if y>0:
		near.append([y-1, x,lista[y-1][x]])
	#print(f"at {y},{x} - neighbours: {near}")
	for n in near:
		y2=n[0]
		x2=n[1]
		val=lista[y2][x2]
		if costs[y][x]+val<costs[y2][x2]:
			costs[y2][x2]=costs[y][x]+val

print(costs[-1][-1])

