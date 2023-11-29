# 2023-11-29
#Start	12:06
#Part1	12:29	23min
#Part2	13:04	35min
#Total	58min
import re, itertools, copy
with open('input') as f:
	lista=f.read().splitlines()

test=lista

silver={}
for t in test:
	if t[:2]=='ma':
		entry=t[7:]
		mask = [(i,v) for i,v in enumerate(entry) if v!='X']

	elif t[:2]=='me':
		entry=re.match(r'mem\[(\d+)\] = (\d+)', t)
		entry=entry.groups()
		test2=bin(int(entry[1]))[2:]
		test2='0'*(36-len(test2))+test2
		test2=list(test2)
		for i,v in mask:
			test2[i]=v
		test2=''.join(test2)
		result=int(test2,2)
		silver[entry[0]]=result
print('Silver:',sum(silver.values()))

gold={}
for t in test:
	if t[:2]=='ma':
		entry=t[7:]
		mask = list(entry)

	elif t[:2]=='me':
		entry=re.match(r'mem\[(\d+)\] = (\d+)', t)
		entry=entry.groups()
		test2=bin(int(entry[0]))[2:]
		test2='0'*(36-len(test2))+test2
		test2=list(test2)
		floating=0
		for i,v in enumerate(mask):
			if v=='0':
				continue
			elif v=='1':
				test2[i]='1'
			elif v=='X':
				floating+=1
				test2[i]='x'+str(floating)
		poss=itertools.product([0,1], repeat=floating)
		for p in poss:
			address=copy.deepcopy(test2)
			for i2,v2 in enumerate(p):
				address[address.index(f'x{i2+1}')]=str(v2)
			address=''.join(address)
			address2=int(address,2)
			gold[address2]=int(entry[1])
print('Gold:',sum(gold.values()))