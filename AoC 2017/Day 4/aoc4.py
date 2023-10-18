# 2023-10-17
#Start	19:25
#Part1	19:28	3min
#Part2	19:32	4min
#Total	7min
with open('input') as f:
	lista=f.read().splitlines()

silver=0
gold=0
for l in lista:
	entry=l.split()
	if len(entry)==len(set(entry)):
		silver+=1
		entry2=[''.join(sorted(x)) for x in entry]
		if len(entry2)==len(set(entry2)):
			gold+=1
print(silver, gold)