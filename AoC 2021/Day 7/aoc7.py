#Start	10:38 20211207
#Part1	10:49 11min
#Part2	11:12 23min-4min outage
#Total	30min
with open('input') as f:
	lista=list(map(int, f.read().strip().split(',')))


fuel_list1=[]
fuel_list2=[]

for i in range(max(lista)):
	fuel1, fuel2=0,0
	for l in lista:
		distance=abs(i-l)
		fuel1+=distance
		fuel2+=distance*(distance+1)//2
	fuel_list1.append(fuel1)
	fuel_list2.append(fuel2)

print(min(fuel_list1), min(fuel_list2))
