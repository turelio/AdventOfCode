#2022-02-02
#Start	11:03
#Part1	11:20
#Part2	11:41
#Total	38min
with open('input') as f:
	lista=f.read().splitlines()

print(lista)
vowel=['a','e','i','o','u']
banned=['ab','cd','pq','xy']

silver=0
for i in lista:
	vowels=0
	c1,c2,c3=0,0,1
	for index, value in enumerate(i):
		if value in vowel:
			vowels+=1
		if vowels>=3:
			c1=1
		if index!=15:
			if i[index]==i[index+1]:
				print(i, i[index:index+2])
				c2=1
			if i[index:index+2] in banned:
				print(i, i[index:index+2])
				c3=0
	if all([c1,c2,c3]):
		print(i)
		silver+=1

print(silver)

gold=0
for i in lista:
	c1,c2=0,0
	pairs=[]
	triples=[]
	for index, value in enumerate(i):
		if index!=15:
			pairs.append(i[index:index+2])
		if index<14:
			triples.append(i[index:index+3])
	for index, value in enumerate(pairs):
		current=pairs.copy()
		if index>0:
			current[index-1]='0' 
		if index<14:
			current[index+1]='1'
		if current.count(value)>1:
			c1=1
	for j in triples:
		if j[0]==j[2]:
			c2=1
			print(j)
			break
	if all([c1,c2]):
		print(i)		
		gold+=1
print(gold)