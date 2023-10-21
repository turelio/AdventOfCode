# 2023-10-21
#Start	16:48
#Part1	16:58	10min
#Part2	stopped
#Total
with open('input') as f:
	lista=f.read().splitlines()

lista=sorted(map(int, lista))
lista.append(max(lista)+3)
print(lista)
silver=[0,0,0]
prev=0
for i,v in enumerate(lista):
	jump=v-prev
	silver[jump-1]+=1
	prev=v

print(silver, silver[0]*silver[2])	