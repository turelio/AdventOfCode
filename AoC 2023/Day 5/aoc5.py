# 2023-12-05
# Start	06:00	
# Part1	06:26	26min
# Part2	10:47	~244min
# Total	270min
# tried to do range splitting before giving up and bruteforcing from reverse
with open('input') as f:
	lista=f.read().strip().split('\n\n')
# parse
seeds=lista[0].split()[1:]
seeds=[int(l) for l in seeds]
maps=lista[1:]
maps=[m.split('\n') for m in maps]
maps=[m[1:] for m in maps]
maps=[[list(map(int,m2.split())) for m2 in m] for m in maps]

# seed to location
def to_location(seed):
	for layer in maps:
		for ranges in layer:
			if seed in range(ranges[1],ranges[1]+ranges[2]):
				seed=seed+(ranges[0]-ranges[1])
				break
	return seed

# location to seed
def to_seed(location):
	for layer in maps[::-1]:
		for ranges in layer:
			if location in range(ranges[0],ranges[0]+ranges[2]):
				location-=(ranges[0]-ranges[1])
				break
	return location

# Part 1
silver=[]
for s in seeds:
	silver.append(to_location(s))
print('Silver:',min(silver))

# Part 2 bruteforce
ranges=[range(seeds[i],seeds[i]+seeds[i+1]) for i in range(0,len(seeds),2)]
gold=10**10
mod=10000
i, end=0,0
while i>=end:
	test=to_seed(i)
	for g in ranges:
		if test in g:
			if i<gold:
				gold=i
			mod=-1
			end=i-10000
			break
	i+=mod
print('Gold:', gold)

