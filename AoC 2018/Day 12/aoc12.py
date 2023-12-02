# 2023-12-02
#Start	13:48
#Part1	14:34	46min
#Part2	15:13	39min
#Total	85min
with open('input') as f:
	lista=f.read().split('\n\n')

rules=lista[1].splitlines()
state=lista[0].split(' ')[2]

pots=set([i for i,s in enumerate(state) if s=='#'])

ruleset={}
for rule in rules:
	entry=rule.split(' ')
	near=entry[0].replace('#','1').replace('.','0')
	near=tuple([int(n) for n in list(near)])
	if entry[2]=='#':
		ruleset[tuple(near)]=True
	else:
		ruleset[tuple(near)]=False


# You only need to run it until automata stabilize and the sum starts incrementing by constant amount
i=0
deltas=[None,None,None]
while True:
	pots2=set()
	for j in range(min(pots)-2,max(pots)+3):
		near=[j-2,j-1,j,j+1,j+2]
		near=[1 if n in pots else 0 for n in near]
		near=tuple(near)
		if ruleset[near]==True:
			pots2.add(j)	
	pot_sum=sum(pots2)
	delta=pot_sum-sum(pots)
	if i == 19:
		silver=pot_sum
	deltas=[delta]+deltas[:-1]
	pots=pots2
	if deltas[0]==deltas[1]==deltas[2]:
		gold=pot_sum+delta*(50000000000-i-1)
		print(f'stopped at generation {i+1}, {pot_sum}, constant increment {delta}\nSilver = {silver}, Gold= {gold}')
		break
	i+=1