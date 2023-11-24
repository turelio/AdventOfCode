# 2023-11-23
#Start	19:43
#Part1	20:00	17min
#Part2	20:01	1min
#Total	18min
with open('input') as f:
	lista=f.read().splitlines()

silver={'a':0,'b':0,'c':0,'d':0}
gold={'a':0,'b':0,'c':1,'d':0}

def solve(r):
	i=0
	while i<len(lista):
		op=lista[i][:3]
		data=lista[i][4:]
		if op=='cpy':
			data=data.split(' ')
			if data[0] in r.keys():
				r[data[1]]=r[data[0]]
			else:
				r[data[1]]=int(data[0])
		elif op=='inc':
			r[data]+=1
		elif op=='dec':
			r[data]-=1
		else:
			data=data.split(' ')
			if data[0] in r.keys():
				if r[data[0]]!=0:
					i+=int(data[1])
					continue
			else:
				if int(data[0])!=0:
					i+=int(data[1])
					continue
		i+=1
	return r

print(solve(silver))
print(solve(gold))