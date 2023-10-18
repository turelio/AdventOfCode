# 2023-10-17
#Start	15:52
#Part1	15:58	6min
#Part2	16:00	2min
#Total	8min
with open('input') as f:
	lista=f.read().splitlines()

lista=list(zip(*lista))

silver, gold='',''
for i in lista:
	unique=set(i)
	counts=[]
	for c in unique:
		counts.append([c, i.count(c)])

	counts=sorted(counts, key=lambda x:x[1], reverse=True)
	silver+=counts[0][0]
	gold+=counts[-1][0]

print(silver, gold)