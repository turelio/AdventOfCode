# 2023-11-25
#Start	11:09
#Part1	11:50	41min
#Part2	12:30	40min
#Total	81min
with open('input') as f:
	lista=f.read().splitlines()
import copy
silver={'a':7,'b':0,'c':0,'d':0}
gold={'a':12,'b':0,'c':0,'d':0}
test='''cpy 2 a
tgl a
tgl a
tgl a
cpy 1 a
dec a
dec a'''.splitlines()
# lista=test
print(test)
lista2=copy.deepcopy(lista)
def solve(r):
	i=0
	# instructions to be skipped until next time
	marked=set()
	while i<len(lista):
		op=lista[i][:3]
		data=lista[i][4:]
		# print(i, op, data)
		if op=='cpy':
			data=data.split(' ')
			if data[0] not in r.keys() and data[1] not in r.keys():
				pass
			elif data[0] in r.keys():
				# copy value of register
				r[data[1]]=r[data[0]]
			else:
				# copy integer
				r[data[1]]=int(data[0])
		elif op=='inc':
			r[data]+=1
		elif op=='dec':
			r[data]-=1
		elif op=='jnz':
			data=data.split(' ')
			d=data[1]
			if d in r.keys():
				d=r[d]
			else:
				d=int(d)
			if data[0] in r.keys():
				# condition is register value
				if r[data[0]]!=0:
					i+=d
					continue
			else:
				# condition is integer
				if int(data[0])!=0:
					i+=d
					continue
		elif op=='tgl':
			j=i+int(r[data])
			if j not in range(len(lista)):
				pass
			else:
				print(f'\tchecking {lista[j]} at {j}')
				op2=lista[j][:3]
				data2=lista[j][4:]
				if i==j:
					if i not in marked:
						marked.add(i)
					else:
						lista[j]='inc'+lista[j][3:]
				elif op2 in ['tgl','dec']:
					lista[j]='inc'+lista[j][3:]
				elif op2 =='cpy':
					lista[j]='jnz'+lista[j][3:]
				elif op2 == 'jnz':
					lista[j]='cpy'+lista[j][3:]				
				elif op2 =='inc':
					lista[j]='dec'+lista[j][3:]
				else:
					print('\tunknown')
					return
		# print('\t',r)
		i+=1
	return r

print(solve(silver))
lista=lista2
# inefficient, took half an hour
print(solve(gold))