#2022-12-28
#Part1	15:29-15:58 (29min)
#Part2	15:58-16:20 (22min)
#Total	51min
with open('input') as f:
	lista,code=f.read().split('\n\n')

code=code.strip()
t={}
for l in lista.splitlines():
	l=l.split(' ')
	if not l[0] in t.keys():
		t[l[0]]=[]
	t[l[0]].append(l[2])

silver=set()
for k,v in t.items():
	n=code.count(k)
	if n==0:
		continue
	else:
		for i in range(1,n+1):
			for j in v:
				test=code.replace(k, "0", i-1).replace(k, j, 1).replace("0", k)
				silver.add(test)

print(len(silver))

t2={}
for k,v in t.items():
	for i in v:
		t2[i]=k

print(t2)
gold=[]
def pack(code, x=1):
	for t in t2:
		n=code.count(t)
		if n==0:
			continue
		else:
			for i in range(1,n+1):
				for j in v:
					code2=code.replace(k, "0", i-1).replace(t, t2[t], 1).replace("0", k)
					if code2=='e' and x not in gold:
						gold.append(x)
						print(code2,x)
					pack(code2, x+1)

#infinite loop
pack(code)