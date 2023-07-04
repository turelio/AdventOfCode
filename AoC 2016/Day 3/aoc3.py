# 2022-02-02
#Start	17:40
#Part1	17:45
#Part2	17:55
#Total	15min
with open('input') as f:
	lista=f.read().splitlines()

lista=[[int(j) for j in i.split()] for i in lista]
silver=0
for i in lista:
	if i[0]+i[1]>i[2] and i[0]+i[2]>i[1] and i[1]+i[2]>i[0]:
		silver+=1
print(silver)
print(len(lista))
lista2=list(zip(*lista))
lista3=[]
for i in lista2:
	lista3+=list(i)
print(len(lista3))

gold=0
for j in range(0,len(lista3),3):
	if lista3[j]+lista3[j+1]>lista3[j+2] and lista3[j]+lista3[j+2]>lista3[j+1] and lista3[j+1]+lista3[j+2]>lista3[j]:
		gold+=1
print(gold)