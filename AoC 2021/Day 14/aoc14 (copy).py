#Start	9:52	20211214	
#Part1	10:53	61min
#Part2	11:47	54min
#Total	115min
import copy
with open('input') as f:
	lista=f.read().split('\n\n')
template=lista[0]
rules=lista[1].splitlines()
rules=[r.split(' -> ') for r in rules]
rules2={}
for r in rules:
	rules2[r[0]]=r[1]

count_char, count_pair={},{}
for v in set(rules2.values()):
	count_char[v]=template.count(v)
for k in set(rules2.keys()):
	count_pair[k]=template.count(k)
counts=[count_char, count_pair]

def expand(counts):
	count_pair=counts[1]
	count_new=copy.deepcopy(count_pair)
	count_char=copy.deepcopy(counts[0])
	for c in count_pair:
		for r in rules2:
			if r==c:
				count_char[rules2[r]]+=count_pair[c]
				count_new[c]-=count_pair[c]
				count_new[f"{c[0]}{rules2[r]}"]+=count_pair[c]
				count_new[f"{rules2[r]}{c[1]}"]+=count_pair[c]
				break
	return count_char, count_new
			
def result(counts, n):
	for i in range(n):
		#print(f"{i}: {counts[0]}")
		counts=expand(counts)
	return max(counts[0].values())-min(counts[0].values())

silver=result(counts, 10)
gold=result(counts,40)
print(silver, gold)