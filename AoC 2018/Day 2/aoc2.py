#Start	11:47	20211218
#Part1	11:55	8min
#Part2	12:04	9min
#Total	17min
with open('input') as f:
	lista=f.read().splitlines()


count_2=0
count_3=0
for l in lista:
	count2=0
	count3=0
	unique=set(list(l))
	for u in unique:
		if l.count(u)==2:
			count2+=1
		if l.count(u)==3:
			count3+=1
	if count3>0:
		count_3+=1
	if count2>0:
		count_2+=1

silver=count_2*count_3
print(silver)

gold=[]
for l in lista:
	for i in lista:
		if l==i:
			continue
		errors=0
		for j in range(len(l)):
			if l[j]!=i[j]:
				if errors<=1:
					errors+=1
				else:
					errors+=1
					break
		if errors<=1:
			gold.append([l,i])
print(gold)
