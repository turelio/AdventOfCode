# 2023-10-18
#Start	14:18
#Part1	14:30	12min
#Part2	14:44	14min
#Total	26min
with open('input') as f:
	lista=f.read().splitlines()

data={}
for l in lista:
	l=l.split()
	print(l)
	bag=l[0]+'-'+l[1]
	rest=' '.join(l[4:])
	rest=rest.split(', ')
	print(rest)
	data[bag]=[]
	for r in rest:
		r=r.split()
		if 'no' in r:
			continue
		else:
			amount=int(r[0])
			bag2=r[1]+'-'+r[2]
			data[bag].append([bag2, amount])
			print(bag2, amount)

	print(bag, rest)

for k,v in data.items():
	print(k,v)

print(len(data))

contains=[]
def search(n):
	if len(data[n])==0:
		return
	for child in data[n]:
		child_id=child[0]
		child_n=child[1]
		if child_id == 'shiny-gold':
			contains.append(1)
			return
		search(child_id)

silver=0
for k in data:
	search(k)
	if len(contains)>0:
		print(k)
		silver+=1
	contains=[]
print(silver)

gold=[]
def search2(n, mult=1):
	children=data[n]
	if len(children)==0:
		return
	for child in children:
		child_id=child[0]
		child_n=child[1]
		gold.append(mult*child_n)
		search2(child_id,mult*child_n)

search2('shiny-gold')
print(gold)
print(sum(gold))
