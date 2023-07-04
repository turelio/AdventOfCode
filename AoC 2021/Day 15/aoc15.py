#Start	11:17	20211215	
#Part1	
#Part2	
#Total

with open('input2') as f:
	lista=f.read().splitlines()

lista=[[int(i) for i in l] for l in lista]
print(len(lista), len(lista[0]))
risks=[]
#routes=[]
#route=[]
def step(y,x,suma):
	#route2=route.copy()
	#route2.append([y,x])
	y2,x2=y,x
	suma2=suma
	if not (y==0 and x==0):
		suma2+=lista[y][x]
	if (y==4 and x==4):
		risks.append(suma)
		print(f"found {suma}")
		return
	if x+1<len(lista):
		x3=x+1
		step(y2,x3,suma2)
	if y+1<len(lista):
		y3=y+1
		step(y3,x2,suma2)

step(0,0,0)

print(min(risks)+1)

