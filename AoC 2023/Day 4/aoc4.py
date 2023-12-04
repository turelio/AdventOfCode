# 2023-12-03
# Start	06:00	
# Part1	06:08	8min
# Part2	06:23	15min
# Total	23min
with open('input') as f:
	lista=f.read().splitlines()

silver=0
counts=[1]*len(lista)
for i,l in enumerate(lista):
	test=l.replace('  ',' ')
	test=test.split(':')[1]
	win, candidates=test.split('|')
	win=set(win.strip().split(' '))
	candidates=set(candidates.strip().split(' '))
	x=len(win&candidates)
	if x>0:
		i2=min(i+x+1, len(lista))
		for j in range(i+1,i2):
			counts[j]+=counts[i]
		silver+=2**(x-1)

print('Silver:',silver)
print('Gold:',sum(counts))
