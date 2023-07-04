#2022-12-28
#Part1	12:34-13:16	(42min)
#Part2	13:16-13:21	(5min)
#Total	47min
with open('input') as f:
	lista=f.read().splitlines()

ing={}
for l in lista:
	l=l.split(' ')
	ing[l[0]]={'capacity':int(l[2][:-1]),'durability':int(l[4][:-1]),'flavor':int(l[6][:-1]),'texture':int(l[8][:-1]),'calories':int(l[10])}

def check(n):
	capacity, durability, flavor, texture=0,0,0,0
	calories=0
	for i,v in enumerate(list(ing.items())):
		# print(i,v)
		capacity+=n[i]*v[1]['capacity']
		durability+=n[i]*v[1]['durability']
		flavor+=n[i]*v[1]['flavor']
		texture+=n[i]*v[1]['texture']
		calories+=n[i]*v[1]['calories']

	properties=[capacity, durability, flavor, texture]
	result=1
	for i,v in enumerate(properties):
		if v<0:
			properties[i]=0
		result*=properties[i]
	return result, calories

def sums(n):
	result=[]
	for n1 in range(n+1):
		for n2 in range(n+1):
			if n1+n2>100:
				break
			for n3 in range(n+1):
				if n1+n2+n3>100:
					break
				n4=100-(n1+n2+n3)
				result.append((n1,n2,n3,n4))
	return result

proportions=sums(100)

silver=0
gold=0
for i in proportions:
	result,calories=check(i)
	if result>silver:
		silver=result
	if calories==500:
		if result>gold:
			gold=result

print(silver, gold)



