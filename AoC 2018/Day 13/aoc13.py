# 2023-12-02
#Start	X
#Part1	X
#Part2	
#Total
with open('input2') as f:
	lista=f.read().splitlines()
import copy
# lista=lista.replace('\\', 'O').replace('/', 'O').split()
print(lista)
for l in lista:
	print(len(l))

[print(l) for l in lista]
tick=1
roads=['-','+','|']
dirs=['>','v','<','^']
corners=['\\','/']
moves={'>':(1,0),'v':(0,-1),'<':(-1,0),'^':(0,1)}
carts=[]
for y in range(len(lista)):
	for x in range(len(lista[0])):
		if lista[y][x] in dirs:
			carts.append(((y,x), dirs.index(lista[y][x])))
			print(f'found cart at {x,y}')
while True:
	print(tick)
	carts2=[]
	carts=list(sorted(carts, key=lambda x:x[0]))
	print(f'cart queue: {carts}')

	tick+=1
	break