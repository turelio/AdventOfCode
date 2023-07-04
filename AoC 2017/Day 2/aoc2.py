#Start	11:40	20211218
#Part1	11:43	3min
#Part2	11:46	3min	
#Total	6min
with open('input') as f:
	lista=f.read().splitlines()

lista=[[int(k) for k in l.split('\t')] for l in lista]

silver=[]
gold=[]
for l in lista:
	silver.append(max(l)-min(l))
	for i in l:
		for j in l:
			if i%j==0 and i!=j:
				gold.append(i/j)

print(sum(silver))
print(sum(gold))