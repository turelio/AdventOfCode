#Start	18:24	211209	
#Part1	18:57	33min
#Part2	20:53	116min
#Total	149min
with open('input') as f:
	lista=f.read().splitlines()


def get_corners(y,x):
	up = [lista[y-1][x],y-1,x] if 99>=y-1>=0 else [9, y,x]
	down = [lista[y+1][x],y+1,x] if 99>=y+1>=0 else [9, y,x]
	left = [lista[y][x-1],y,x-1] if 99>=x-1>=0 else [9, y,x]
	right = [lista[y][x+1],y,x+1] if 99>=x+1>=0 else [9, y,x]
	return [up,down,left,right]

def find_basin(y,x):
	finds=[]
	for d in get_corners(y,x):
		if int(d[0])==9:
			continue
		else:
			finds.append([d[1], d[2]])
	return finds

def islowpoint(y,x):
	for d in get_corners(y,x):
		if int(d[0])<=int(lista[y][x]):
			return 0
	return int(lista[y][x])+1

def isbasin(y,x):
	if int(lista[y][x])==9:
		return 0
	basinlist=[[y,x]]
	counter1,counter2=0,1
	while counter1!=counter2:
		counter1=len(basinlist)
		for b in basinlist:
			for i in find_basin(b[0], b[1]):
				if not i in basinlist:
					basinlist.append(i)
		counter2=len(basinlist)

		return(len(basinlist))


#print(islowpoint(0,0))
silver=0
gold=[]
for y,v1 in enumerate(lista):
	for x,v2 in enumerate(v1):
		silver+=islowpoint(int(y),int(x))
		res=isbasin(int(y),int(x))
		gold.append(res)
		#print(f"pos {y} - {x} - {lista[y][x]} - {res}")
print(silver)

gold=sorted(list(set(gold)))
print(gold[-3]*gold[-2]*gold[-1])
