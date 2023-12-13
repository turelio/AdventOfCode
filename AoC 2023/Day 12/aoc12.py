# 2023-12-12
# Start	06:00	
# Part1	06:17	17min	
# Part2	X	+53min +100min
# Total	
import itertools,copy
with open('input') as f:
	lista=f.read().splitlines()
test='''???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1'''.splitlines()
lista=test

n=1000
answers=[0]
# works well on test Part 2 but chokes on real input, needs DP/memoization/cache
def bf(f,e,i=0,c=[None]):
	# print('\t',i,c)
	if c[-1]==None:
		if c[:-1] !=counts[:len(c)-1]:
			return
	if i==n:
		if c[-1]==None:
			c=c[:-1]
		if c==counts:
			answers[0]+=1
		return
	# probably unnecessary
	if f<0 or e<0:
		return
	# force full
	if i in filled:
		if f>0:
			if c[-1]==None:
				bf(f-1,e,i+1,c[:-1]+[1])
			else:
				bf(f-1,e,i+1,c[:-1]+[c[-1]+1])
	# force empty
	elif i in empty:
		if e>0:
			if c[-1]==None:
				bf(f,e-1,i+1,c)
			else:
				bf(f,e-1,i+1,c+[None])
	else:
		# try full
		if f>0:
			if c[-1]==None:
				# print('yeah')
				bf(f-1,e,i+1,c[:-1]+[1])
			else:
				bf(f-1,e,i+1,c[:-1]+[c[-1]+1])
		# try empty
		if e>0:
			if c[-1]==None:
				bf(f,e-1,i+1,c)
			else:
				bf(f,e-1,i+1,c+[None])
				# c2.append(None)

import time
lista2=[]
for j,l in enumerate(lista):
	entry,counts=l.split(' ')
	entry=list(entry)
	entry=[1 if e=="#" else 0 if e=="." else None for e in entry]
	counts=counts.strip().split(',')
	counts=[int(c) for c in counts]
	lista2.append((entry,counts))

lista2=sorted(lista2, key=lambda x:x[0].count(None),reverse=0)
from datetime import datetime
start=datetime.now()
last=datetime.now()
n2=len(lista2)
gold=0
for j,l in enumerate(lista2):
	entry,counts=l
	counts=counts*5
	entry2=[None]+entry
	entry+=entry2*4
	empty=set([i for i,v in enumerate(entry) if v==0])
	filled=set([i for i,v in enumerate(entry) if v==1])
	n=len(entry)
	print(f'[{j+1:03d}/{n2:03d}], {entry.count(None)} unknown, {sum(counts)-entry.count(1)} missing, {len(counts)} groups')
	answers=[0]
	bf(sum(counts),len(entry)-sum(counts))
	gold+=answers[0]
	print(f'\t',answers[0],gold)
	print(f'\tTook {(datetime.now()-last).seconds}s, {(datetime.now()-start).seconds}s total')
	last=datetime.now()

print(gold)



