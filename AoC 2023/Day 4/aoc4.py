# 2023-12-03
# Start	06:00	
# Part1	06:08	8min
# Part2	06:23	15min
# Total	23min
import re
with open('input') as f:
	lista=f.read().splitlines()

silver=0
counts={i:1 for i,v in enumerate(lista)}
for i,l in enumerate(lista):
	entry=re.split('[:|]', l)
	n, win, candidates=entry
	win=re.split(r'\s+', win.strip())
	candidates=re.split(r'\s+', candidates.strip())
	x=len(set(candidates).intersection(set(win)))
	if x>0:
		i2=min(i+x+1, len(lista))
		for j in range(i+1,i2):
			counts[j]+=counts[i]
		silver+=2**(x-1)

print('Silver:',silver)
print('Gold:',sum(counts.values()))
