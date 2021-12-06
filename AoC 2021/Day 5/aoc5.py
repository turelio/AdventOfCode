with open('input') as f:
	lista = f.read().splitlines()

lista=[l.split(' -> ') for l in lista]
for c1, v1 in enumerate(lista):
	for c2, v2 in enumerate(v1):
		lista[c1][c2]=v2.split(',')

overlap_map=[[0 for col in range(1000)] for row in range(1000)]
counter1=0
lista2=lista.copy()
for c, v in enumerate(lista):
	x1=int(v[0][0])
	x2=int(v[1][0])
	y1=int(v[0][1])
	y2=int(v[1][1])
	# diagonal
	if not(x1==x2 or y1==y2):
		#uncomment nex line for answer 1
		#continue
		# \
		if (x1<x2 and y1<y2):
			a,b=x1,y1
			while (a<=x2 and b<=y2):
				#print(f"[{a},{b}]")
				overlap_map[b][a]+=1
				a+=1
				b+=1
		# \
		elif (x1>x2 and y1>y2):
			a,b=x2,y2
			while (a<=x1 and b<=y1):
				overlap_map[b][a]+=1
				#print(f"[{a},{b}]")
				a+=1
				b+=1
		# /
		elif (x1>x2 and y1<y2):
			a,b=x2,y2
			while (a<=x1 and b>=y1):
				overlap_map[b][a]+=1
				#print(f"[{a},{b}]")
				a+=1
				b-=1
		# /
		elif (x1<x2 and y1>y2):
			a,b=x1,y1
			while (a<=x2 and b>=y2):
				overlap_map[b][a]+=1
				#print(f"[{a},{b}]")
				a+=1
				b-=1
	#vertical
	elif(x1==x2):
		if y1>y2:
			a=y2
			while y1>=a:
				overlap_map[a][x1]+=1
				a+=1
		elif y2>y1:
			a=y1
			while y2>=a:
				overlap_map[a][x1]+=1
				a+=1
		else:
			overlap_map[y1][x1]+=1
	#horizontal
	elif(y1==y2):
		if x1>x2:
			a=x2
			while x1>=a:
				overlap_map[y1][a]+=1
				a+=1
		elif x2>x1:
			a=x1
			while x2>=a:
				overlap_map[y1][a]+=1
				a+=1
		else:
			overlap_map[y1][x1]+=1

for i in overlap_map:
	for j in i:
		if j>1:
			#print(j)
			counter1+=1

# remove diagonal part for answer 1
print(counter1)

