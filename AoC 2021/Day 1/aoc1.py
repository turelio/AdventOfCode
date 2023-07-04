# 14 min
with open('input') as f:
	lista=f.read().splitlines()

counter1 = 0
i=0
while i<(len(lista)-1):
	if (lista[i+1]>lista[i]):
		counter1+=1
	i+=1
print(counter1+1)

counter2=0
j=1
while (j<(len(lista)-2)):
	if int(lista[j-1])<int(lista[j+2]):
		counter2+=1
	j+=1
print(counter2)

