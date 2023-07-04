# 9:04
# 9:13 silver
# 9:15 gold
# 11 min
with open('input') as f:
	lista=f.read().split('\n\n')

lista = [[int(j) for j in i.strip('\n').split('\n')] for i in lista]

silver=[sum(i) for i in lista]
print(max(silver))

gold=sum(sorted(silver)[-3:])
print(gold)


# original
# with open('input') as f:
# 	lista=f.read().split('\n\n')

# lista2=[]
# for i in lista:
# 	entry=[]
# 	for j in i.split('\n'):
# 		if j=='':
# 			continue
# 		entry.append(int(j))
# 	lista2.append(entry)

# print(lista2)

# silver=[]
# for i in lista2:
# 	silver.append(sum(i))

# print(max(silver))

# gold=sum(sorted(silver, reverse=True)[0:3])
# print(gold)