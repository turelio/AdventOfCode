#Start	9:24
#Part1	10:00
#Part2	10:11
#Total	47min

# ~9s
import re,copy
with open('input') as f:
	lista=f.read().split('\n\n')

monkeys=[]
prod=1
for l in lista:
	monkey={}
	l=l.split('\n')
	monkey['items']=[int(i) for i in l[1][18:].split(', ')]
	monkey['operation']=l[2][19:]
	monkey['divisible']=int(l[3][21:])
	monkey['istrue']=int(l[4][29:])
	monkey['isfalse']=int(l[5][30:])
	monkey['inspected']=0
	monkeys.append(monkey)
	prod*=monkey['divisible']

monkeys2=copy.deepcopy(monkeys)

print('Silver: ', end='')
# part 1
for x in range(20):
	# print(f'round {x+1}')
	for num, monkey in enumerate(monkeys):
		if len(monkey['items'])==0:
			continue
		else:
			while len(monkey['items'])>0:
				monkey['inspected']+=1
				old=monkey['items'].pop(0)
				old=eval(monkey['operation'])
				old=old//3
				if old%monkey['divisible']==0:
					monkeys[monkey['istrue']]['items'].append(old)
				else:
					monkeys[monkey['isfalse']]['items'].append(old)

silver=sorted([i['inspected'] for i in monkeys])
print(silver[-1]*silver[-2])


# Part 2
# Had to look up hint for division by product :(

print('Gold: ', end='')
for x in range(10000):
	# print(f'round {x+1}')
	for num, monkey in enumerate(monkeys2):
		if len(monkey['items'])==0:
			continue
		else:
			while len(monkey['items'])>0:
				monkey['inspected']+=1
				old=monkey['items'].pop(0)
				old=eval(monkey['operation'])
				old=old%prod
				if old%monkey['divisible']==0:
					monkeys2[monkey['istrue']]['items'].append(old)
				else:
					monkeys2[monkey['isfalse']]['items'].append(old)

gold=sorted([i['inspected'] for i in monkeys2])
print(gold[-1]*gold[-2])
