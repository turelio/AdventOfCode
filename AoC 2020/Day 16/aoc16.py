# 2023-11-29
#Start	13:47
#Part1	14:10	23min
#Part2	14:55	45min
#Total	68min
import re
with open('input') as f:
	lista=f.read().split('\n\n')

test='''class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12'''.split('\n\n')

test='''class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9'''.split('\n\n')

# lista=test
data=lista[0].splitlines()
fields={}
for d in data:
	entry=re.match(r'(.*?): (\d+)-(\d+) or (\d+)-(\d+)', d)
	name, x1,x2,y1,y2=entry.groups()
	fields[name]=[range(int(x1),int(x2)+1), range(int(y1),int(y2)+1)]


ticket=[int(i) for i in lista[1].splitlines()[1].split(',')]
nearby=lista[2].splitlines()[1:]
nearby=[[int(j) for j in i.split(',')] for i in nearby]

# Silver
silver=[]
nearby2=[]
for i, entry in enumerate(nearby):
	# print('check row ',i,entry)
	validrow=True
	for n in entry:
		valid=False
		for v in fields.values():
			for v2 in v:
				if n in v2:
					valid=True
		if not valid:
			if validrow==True:
				validrow=False
			silver.append(n)
	if validrow:
		nearby2.append(entry) 

# Gold
nearby2+=[ticket]
possible=[]
nearby2=list(zip(*nearby2))
for i,column in enumerate(nearby2):
	poss=[]
	for n in column:
		entry=set()
		for k,v in fields.items():
			if n in v[0] or n in v[1]:
				entry.add(k)
		poss.append(entry)
	possible.append([i,poss])

answer=set()
gold={}
candidates=[]

for i, p in possible:
	common=p[0].intersection(*p)
	candidates.append([i,common])


while len(gold)!=len(nearby2):
	for i, p in candidates:

		if len(p)==0:
			continue
		if len(p)==1:
			test=min(p)
			gold[test]=i
			answer.add(test)
		candidates[i][1]-=answer
	print(f'{len(answer)}/{len(nearby2)} certain')

gold2=1
for k,v in gold.items():
	if k.startswith('departure'):
		print(k,v, ticket[v])
		gold2*=ticket[v]

print('Silver:',sum(silver))
print('Gold:',gold2)