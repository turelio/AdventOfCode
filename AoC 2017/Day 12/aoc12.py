# 2023-12-01
#Start	13:06
#Part1	13:16	10min
#Part2	13:26	10min
#Total	20min
with open('input') as f:
	lista=f.read().splitlines()

test='''0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5'''.splitlines()
# lista=test
group={}
for l in lista:
	program, pipes=l.split(' <-> ')
	pipes=pipes.split(', ')
	print(program,pipes)
	group[program]=set(pipes)

print(group)
silver=0
gold=[]
for program,pipes in group.items():
	# print(program)
	found=False
	while not found:
		d1=len(pipes)
		if '0' in pipes:
			found=1
		for p in pipes:
			pipes=pipes.union(group[p])
		if len(pipes)==d1:
			# only groups without 0, so result is +1
			print(program, len(pipes))
			if pipes not in gold:
				gold.append(pipes)
			break
	if found:
		silver+=1
print(len(group),silver)
print(gold, len(gold)+1)
print(len(lista))