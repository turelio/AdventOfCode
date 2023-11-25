# 2023-11-25
#Start	13:32
#Part1	13:54	22min
#Part2	N/A
#Total

with open('input') as f:
	lista=f.read().splitlines()
import copy
silver={'a':7,'b':0,'c':0,'d':0}
gold={'a':12,'b':0,'c':0,'d':0}

# lista=test
# print(test)
lista2=copy.deepcopy(lista)


def solve(r):
	i=0
	c=0
	signal=''
	mark1='01'*10
	mark2='10'*10
	# print()
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
				elif op2 in ['tgl','dec','out']:
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
		elif op=='out':
			if data[0] in r.keys():
				# out value of register
				signal+=str(r[data[0]])
			else:
				# out integer
				signal+=str(data[0])
			if len(signal)>=20:
				test2=signal[-20:]
				# print(len(test2),test2, len(mark1),mark1, mark2)
				if test2==mark1 or test2==mark2:
					print('FOUND')
					return True
		# print('\t',r)
		i+=1
		c+=1
		if c>=100000:
			# print('too long')
			return False
	return False

lista=copy.deepcopy(lista2)

x=0
while True:
	if x%10==0:
		print(x)		
	# print('trying',x)
	test={'a':x,'b':0,'c':0,'d':0}
	answer=solve(test)
	if answer:
		print(x)
		break
	x+=1