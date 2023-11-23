# 2023-11-23
#Start	12:20
#Part1	12:55	35min
#Part2	13:36	41min
#Total	76min

import itertools, math
with open('input') as f:
	lista=f.read().splitlines()

lista=[int(l) for l in lista]
print(lista, sum(lista))

target=sum(lista)//3
print(target)
rest=set(lista)


def possibles(rest, n):
	search=itertools.combinations(rest,n)
	found=[]
	for s in search:
		if sum(s)==target:
			
			found.append([set(s), rest-set(s), math.prod(set(s))])
	# print(len(found))
	return found


# lowest count is 6
g=possibles(rest,6)

silver=[]

g=sorted(g,key=lambda x:x[2])



for g1, rest2, prod in g:
	print(g1,rest2, prod)
	for i in range(1,len(rest)):
		test=possibles(rest2,i)
		if len(test)==0:
			continue
		else:
			for g2, rest3, prod2 in test:
				if sum(rest3)==target:
					# print('FOUND')
					silver.append([g1,g2,rest3])
	if len(silver)!=0:
		print('Silver: ', prod)
		break


# redundant code
# GOLD
target=sum(lista)//4
print(target)
rest=set(lista)


def possibles(rest, n):
	search=itertools.combinations(rest,n)
	found=[]
	for s in search:
		if sum(s)==target:
			
			found.append([set(s), rest-set(s), math.prod(set(s))])
	# print(len(found))
	return found


# lowest count is 6
for  i in range(1, 6):
	g=possibles(rest,i)
	print(i, len(g))
	if len(g)!=0:
		break

silver=[]

g=sorted(g,key=lambda x:x[2])


for g1, rest2, prod in g:
	print(g1,rest2, prod)
	for i in range(1,len(rest)):
		test=possibles(rest2,i)
		if len(test)==0:
			continue
		else:
			for g2, rest3, prod2 in test:
				for j in range(1,len(rest3)):
					test2=possibles(rest3, j)
					if len(test2)==0:
						continue
					else:
						for g3, rest4, prod3 in test2:
							if sum(rest4)==target:
								# print('FOUND')
								silver.append([g1,g2,rest3])
	if len(silver)!=0:
		print('Gold: ', prod)
		break

