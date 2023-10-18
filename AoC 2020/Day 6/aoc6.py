# 2023-10-18
#Start	13:58
#Part1	14:11	13min
#Part2	14:16	5min
#Total	18min
with open('input') as f:
	lista=f.read().strip().split('\n\n')

lista=[l.split('\n') for l in lista]
lista=[[set(m) for m in l] for l in lista]
silver=[]
gold=[]

for l in lista:
	combined=set.union(*l)
	common=set.intersection(*l)
	gold.append(len(common))
	silver.append(len(combined))

print(sum(silver), sum(gold))