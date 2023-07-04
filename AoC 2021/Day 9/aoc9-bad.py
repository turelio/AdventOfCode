#Start	18:24	211209	
#Part1	18:57	33min
#Part2	
#Total
with open('input') as f:
	lista=f.read().splitlines()

# print(lista[0])
# print(lista[1])
# print(lista[2])
# print(lista[3])
def islowpoint(y,x):
	up = lista[y-1][x] if 99>=y-1>=0 else 10
	down = lista[y+1][x] if 99>=y+1>=0 else 10
	left = lista[y][x-1] if 99>=x-1>=0 else 10
	right = lista[y][x+1] if 99>=x+1>=0 else 10
	#print(f"X{up}X\n{left}{lista[y][x]}{right}\nX{down}X")
	for d in [up, down, left, right]:
		if int(d)<=int(lista[y][x]):
			return 0
	return int(lista[y][x])+1

def get_corners(y,x):
	up = [lista[y-1][x],y-1,x] if 99>=y-1>=0 else 0
	down = [lista[y+1][x],y+1,x] if 99>=y+1>=0 else 0
	left = [lista[y][x-1],y,x-1] if 99>=x-1>=0 else 0
	right = [lista[y][x+1],y,x+1] if 99>=x+1>=0 else 0
	return [up,down,left,right]

def find_basin(y,x):
	finds=[]
	for d in get_corners(y,x):
		if d==0:
			continue
		if int(d[0])==9:
			continue
		if (int(d[0])==int(lista[y][x])+1) or (int(d[0])==int(lista[y][x])-1):
			finds.append([d[1], d[2]])
	return finds

def isbasin(y,x):
	if int(lista[y][x])==9:
		return 0
	#print(f"\t{up[0]}\t\n{left[0]}\t{lista[y][x]}\t{right[0]}\n\t{down[0]}\t")
	basinlist=[[y,x]]
	counter1=0
	counter2=10
	counter3=0
	while counter1!=counter2:
		counter1=len(basinlist)
		for b in basinlist:
			for i in find_basin(b[0], b[1]):
				if not i in basinlist:
					basinlist.append(i)
		counter2=len(basinlist)
		counter3+=1
	print("{counter3} loops")
	#print(basinlist, len(basinlist))
	return(len(basinlist))


#print(islowpoint(0,0))
silver=0
gold=[]
for y,v1 in enumerate(lista):
	for x,v2 in enumerate(v1):
		silver+=islowpoint(int(y),int(x))
		res=isbasin(int(y),int(x))
		gold.append(res)
		print(f"pos {y} - {x} - {lista[y][x]} - {res}")
#print(silver)

gold=list(set(gold))
print(sorted(gold))
