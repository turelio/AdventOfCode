# 2023-12-05
# Start	06:00	
# Part1	06:26	26min
# Part2	10:47	~244min
# Total	270min
with open('input') as f:
	lista=f.read().strip().split('\n\n')

seeds=lista[0].split()[1:]
seeds=[int(l) for l in seeds]
maps=lista[1:]
maps=[m.split('\n') for m in maps]
maps=[m[1:] for m in maps]
maps=[[m2.split() for m2 in m] for m in maps]
maps=[[list(map(int,m2)) for m2 in m] for m in maps]
maps2=maps[::-1]

#input to output
def tf1(seed):
	for i,map in enumerate(maps):
		seed2=seed
		for ranges in map:
			if seed in range(ranges[1],ranges[1]+ranges[2]):
				seed=seed+(ranges[0]-ranges[1])
				break
	return seed
# output to input
def tf2(seed):
	for map in maps2:
		seed2=seed
		for ranges in map:
			if seed in range(ranges[0],ranges[0]+ranges[2]):
				seed=seed-(ranges[0]-ranges[1])
				break
	return seed

silver=[]
for s in seeds:
	silver.append(tf1(s))

print('Silver:',min(silver))
gold=[]
for i in range(0,len(seeds),2):
	gold.append(range(seeds[i],seeds[i]+seeds[i+1]))
answer=False
i=0
mod=10000
answer=1000000000000
end=0
while i>=end:
	test=tf2(i)
	for g in gold:
		if test in g:
			if i<answer:
				answer=i
				# print('new lowest',i)
			mod=-1
			end=i-10000
			break
	i+=mod
print('Gold:',answer)

