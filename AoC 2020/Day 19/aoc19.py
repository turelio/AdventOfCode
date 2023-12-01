# 2023-12-01
#Start	10:28
#Part1	X
#Part2	
#Total
import itertools
with open('input') as f:
	lista=f.read().split('\n\n')

test='''0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb'''.split('\n\n')

lista=test

codes=lista[1].splitlines()
rules=lista[0].splitlines()

rules2={}
for r in rules:
	i,v=r.split(':')
	v=v.split('|')
	v=[v2.strip().replace('"','').split(' ') for v2 in v]

	rules2[i]=v

# sovle rules
poss={}
for k,v in rules2.items():
	if v==[['a']]:
		poss[k]='a'
	elif v==[['b']]:
		poss[k]='b'

for k in poss:
	if k in rules2:
		del rules2[k]


print(poss)
n=0
while '0' not in poss:
	print('loop',n)
	print(rules2)
	for k,v in rules2.items():
		rules_remaining=False
		if k in poss:
			continue
		for i, option in enumerate(v):
			for j, option2 in enumerate(option):
				if isinstance(option2, list):
					continue
				if option2 in rules2.keys():
					rules_remaining=True
				if option2 in poss.keys():
					rules2[k][i][j]=poss[option2]
		if not rules_remaining:
			print('\t',v, 'solved')
			if k not in poss:
				entry=rules2[k]
				poss[k]=entry
	print(poss)
	for k in poss:
		if k in rules2:
			del rules2[k]


	n+=1

print('#################')
print(rules2)
print(poss)
print()
def flatten(s,c='',n=0):
	print('\t'*n,f'list has {len(s) elements}')
	branches=itertools.product(*s)
	for b in branches:
		c2=c
		print(b)
		flatten(b)


x=poss['0'][0]
print(x)
flatten(poss['0'][0])