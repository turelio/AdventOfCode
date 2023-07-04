#Start	09:18
#Part1	09:24
#Part2	09:30
#Total	12min
with open('input') as f:
	lista=f.read().splitlines()

lista=[[[int(k) for k in j.split('-')] for j in i.split(',')] for i in lista]
silver=gold=0

for l in lista:
	x=set(range(l[0][0], l[0][1]+1))
	y=set(range(l[1][0], l[1][1]+1))
	if x.issubset(y) or y.issubset(x):
		silver+=1
	if len(list(x&y))>0:
		gold+=1

print(silver, gold)