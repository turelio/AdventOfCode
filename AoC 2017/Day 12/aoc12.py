# 2023-12-01
#Start	13:06
#Part1	13:16	10min
#Part2	13:26	10min
#Total	20min
with open('input') as f:
	lista=f.read().splitlines()

group={}
for l in lista:
	program, pipes=l.split(' <-> ')
	pipes=pipes.split(', ')
	group[program]=set(pipes)

silver=set()
gold=[]
found=set()
for program,pipes in group.items():
	while True:
		d1=len(pipes)
		pipes2=pipes.copy()
		for p in pipes:
			for p2 in group[p]:
				pipes2.add(p2)
		pipes=pipes2
		if len(pipes)==d1:
			if pipes not in gold:
				gold.append(pipes)
			if '0' in pipes:
				silver=pipes
			break
print(len(silver),len(gold))