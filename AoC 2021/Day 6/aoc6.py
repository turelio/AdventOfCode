with open('input') as f:
	lista=list(map(int, f.read().strip().split(',')))

def count_fish(lista, n):
	fish=[lista.count(i) for i in range(9)]
	for i in range(n):
		fish.append(fish.pop(0))
		fish[6]+=fish[8]
	return sum(fish)

print(count_fish(lista, 80), count_fish(lista, 256))


# wrong and unused

# for c, v in enumerate(lista):
# 	lista[c]={"start":6, "current":int(v)}

# #print(lista)

# lista2=[]
# for l in [3,4,3,1,2]:
# 	lista2.append({"start":6, "current":int(l)})


# def tick(lista):
# 	lista_add=[]
# 	for c, v in enumerate(lista):
# 		lista[c]['current']-=1
# 		if lista[c]['current']<0:
# 			lista[c]['current']=6
# 			lista_add.append({"start":lista[c]['current']+2, "current":8})
# 	if lista_add:
# 		lista=lista+lista_add

# 	return lista

# def display(lista):
# 	res=[]
# 	for l in lista:
# 		res.append(l['current'])
# 	return res


# def iterate(lista, n):
# 	print(f"initial state: {lista}")
# 	for i in range(1,n):
# 		lista=tick(lista)
# 		print(f"after day {i}:")
# 		print(*display(lista))
# 		i+=1
# 	print(len(lista))
# iterate(lista2, 19)


# def tick(lista):
# 	lista_add=[]
# 	for c, v in enumerate(lista):
# 		lista[c]-=1
# 		if lista[c]<0:
# 			lista[c]=6
# 			lista_add.append(8)
# 	if lista_add:
# 		lista=lista+lista_add
# 	return lista
