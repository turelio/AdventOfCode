# 2023-11-24
#Start	10:03
#Part1	10:39	36min
#Part2	10:43	4min
#Total	40min
import copy

with open('input') as f:
	lista=f.read().splitlines()

slots=[]
for l in lista:
	l=l.split()
	slots.append([int(l[-1][:-1]),int(l[3])-1])

# move all slots forward
def increment(slots):
	for i,s in enumerate(slots):
		slots[i][0]=(slots[i][0]+1)%(slots[i][1]+1)
	return slots

# configuration where slots fall in line one by one
def desired(slots):
	slots2=[]
	for i, v in enumerate(slots):
		desired=([v[1]-i%(v[1]+1),v[1]])
		slots2.append(desired)
	return slots2

def solve(slots,gold=False):
	# lists fuck up otherwise
	slots=copy.deepcopy(slots)
	if gold:
		slots.append([0,10])
	slots2=desired(slots)
	
	j=0
	while True:
		if slots==slots2:
			print(j)
			break
		else:
			increment(slots)
			j+=1

solve(slots)
solve(slots,True)