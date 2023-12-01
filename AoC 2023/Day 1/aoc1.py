# 2023-12-01
#Start	06:00
#Part1	06:04	4min
#Part2	06:15	11min
#Total	15min
with open('input') as f:
	lista=f.read().splitlines()

g1=['0','1','2','3','4','5','6','7','8','9']
g2=['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
silver,gold=0,0

def decode(n):
	if n in g2:
		return str(g2.index(n)+1)
	elif n in g1:
		return n

for l in lista:
	entry1,entry2=list(),list()
	for i in range(len(l)):
		if l[i] in g1:
			entry1.append(l[i])
			entry2.append(l[i])
		else:
			for num in g2:
				if l[i:].startswith(num):
					entry2.append(num)
					break
	gold+=int(decode(entry2[0])+decode(entry2[-1]))
	silver+=(int(entry1[0]+entry1[-1]))

print(silver,gold)