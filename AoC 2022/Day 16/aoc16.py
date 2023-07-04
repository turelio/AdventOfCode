
#Start	10:40
# gave up, ~3h?
#back 22-12-24 for 
#Part1	
#Part2	
#Total
import re, copy, itertools
with open('input') as f:
	lista=f.read().splitlines()

max_flow=0
neighbors={}
for l in lista:
	result=re.search(r'Valve (.*) has flow rate=(\d*); tunnels? leads? to valves? (.*)', l)
	neighbors[result[1]]={}
	neighbors[result[1]]['flow']=int(result[2])
	neighbors[result[1]]['val']=0
	max_flow+=int(result[2])
	neighbors[result[1]]['near']=list(result[3].split(', '))

def shortest(start,end):
	visited=set()
	traverse={}
	for k in neighbors:
		traverse[k]=10000
	traverse[start]=0
	while True:
		traverse=dict(sorted(traverse.items(), key=lambda item: item[1]))
		for k,v in traverse.items():
			if k not in visited:
				c=k
				break
		if c==end:
			# print(f'from {start} to {end} in {traverse[c]} steps')
			steps=traverse[c]
			break
		visited.add(c)
		moves=neighbors[c]['near']
		for m in moves:
			if traverse[c]+1<traverse[m]:
				traverse[m]=traverse[c]+1
	return steps, traverse

closest={}
for k1 in neighbors:
	closest[k1]={}
	for k2 in neighbors:
		# if k1==k2:
		# 	continue
		closest[k1][k2]=shortest(k1,k2)[0]

print(len(neighbors), len(closest), len(closest['AA']))
# print(closest)

neighbors=dict(sorted(neighbors.items(), key=lambda item: item[1]['flow'], reverse=True))
common=list(neighbors.keys())[:9]
# for k,v in neighbors.items():
	# print(k,v['flow'])
# print(closest)
print(common)
# print('')
possible=list(itertools.permutations(common))
# print(len(possible))

test=possible
silver=set()
for road in test:
	c='AA'
	m=1
	value=0
	for i in road:
		m+=closest[c][i]+1
		if m>30:
			break
		value+=(30-m-(closest[c][i]-1))*neighbors[i]['flow']
		c=i
	print(value)
	silver.add(value)

print(max(silver))
#1627?