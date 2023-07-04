#2022-12-26
#Part1	21:27-21:34 (7min)
#Part2	21:34-22:30	(56min)
#Total	63min
import json
with open('input') as f:
	lista=json.load(f)

silver=[]

def inspect(n):
	if isinstance(n, dict):
		for i in n.values():
			inspect(i)
	elif isinstance(n, list):
		for i in n:
			inspect(i)
	elif isinstance(n, int):
		silver.append(n)
	else:
		return

def inspect2(n,j=0):
	if isinstance(n, dict):
		vals=0
		reds=[]
		for i in n.values():
			val,red=inspect2(i,j+1)
			vals+=val
			reds.append(red)
		if True in reds:
			return 0, False
		else:
			return vals, False
	elif isinstance(n, list):
		vals=0
		for i in n:
			val,red=inspect2(i,j+1)
			if not red:
				vals+=val
		return vals, False
	elif isinstance(n, int):
		return n, False
	elif isinstance(n,str):
		if n=='red':
			return 0,True
		else:
			return 0,False

inspect(lista)
print('Silver:',sum(silver))
print('Gold:', inspect2(lista)[0])

