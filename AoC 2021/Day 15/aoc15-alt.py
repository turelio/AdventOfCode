#Start	11:17	20211215	
#Part1	17:17
#Part2	
#Total
with open('input2') as f:
	lista=f.read().splitlines()

lista=[[int(i) for i in l] for l in lista]
costs=[[2000 for i in l] for l in lista]

visited=[[0 for i in l] for l in lista]


costs[0][0]=0
lista[0][0]=0
def drawc():
	for l,c in zip(lista, costs):
		print(l,c)


nexts=[]
def cost(y,x):

	visited[y][x]=1
	near=[]
	if x+1<len(lista):
		if not [y,x+1] in near:
			near.append([y,x+1,lista[y][x+1]])
	if x>0:
		if not [y,x-1] in near:
			near.append([y,x-1,lista[y][x-1]])	
	if y+1<len(lista):
		if not [y+1,x] in near:
			near.append([y+1,x,lista[y+1][x]])
	if y>0:
		if not [y-1,x] in near:
			near.append([y-1, x,lista[y-1][x]])
	print(f"at {y},{x} - neighbours: {near}")
	nextstep=[]
	for n in near:
		y2=n[0]
		x2=n[1]
		val=lista[y2][x2]
		if costs[y][x]+val<costs[y2][x2]:
			costs[y2][x2]=costs[y][x]+val
	for n in near:
		if visited[n[0]][n[1]]==0 and (not n in nexts):
			nexts.append(n)
	nexts.sort(key=lambda x: int(x[2]))
	drawc()
	print(f"next: {nexts}")
	if len(nexts)==0:
		return
	coord=nexts.pop(0)
	cost(coord[0],coord[1])

cost(0,0)

