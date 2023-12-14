# 2022-12-16, 2023-12-14
#Start	10:40, gave up
#Part1 2023-12-14 13:36, 80min + 180min
#Part2 2023-12-14 14:26, 50min	
#Total 310min
import re, copy, itertools
with open('input') as f:
	lista=f.read().splitlines()
# how many valves should you try to open, used for debugging
max_open=6

near={}
flow={}
# parse connections and flows
for l in lista:
	r=re.match(r'Valve (.*) has flow rate=(\d*); tunnels? leads? to valves? (.*)', l)
	r=list(r.groups())
	flow[r[0]]=int(r[1])
	near[r[0]]=r[2].split(', ')

# pathfinding to find distances between valves
def shortest(start):
	visited=set()
	traverse={}
	for k in near:
		traverse[k]=10000
	traverse[start]=0
	queue=[start]
	while len(queue)!=0:
		c=queue.pop(0)
		visited.add(c)
		moves=near[c]
		for m in moves:
			if traverse[c]<traverse[m]:
				traverse[m]=traverse[c]+1
		moves=[m for m in moves if m not in visited and m not in queue]
		queue+=moves
	return traverse
dist={k:shortest(k) for k in near}

def solve(order):
	c='AA'
	done=False
	on=len(order)
	t=1
	total=0
	rate=0
	opened=[]
	n=order.pop(0)
	steps=dist[c][n]
	while t!=31:
		# print(f'== Minute {t} ==')
		if len(opened)==0:
			pass
			# print('No valves are open.')
		else:
			total+=rate
			# print(f'Valves {opened} are open, releasing {rate} pressure. (total {total})')
		if done:
			pass
			# print('Waiting')
			# t+=1
		elif steps!=0:
			# print(f'You move to valve {n}.')
			steps-=1
			# t+=1
		else:
			# print(f'You open valve {n}.')
			opened.append(n)
			rate+=flow[n]
			if len(opened)==on:
				done=True
			else:
				c=n
				n=order.pop(0)
				steps=dist[c][n]
		if t==26:
			total2=total
		t+=1		
	return total,total2

viable=set([k for k,v in flow.items() if v!=0])
test=list(itertools.permutations(viable, max_open))
silver=set()
best={}
for i,t in enumerate(test):
	if i%100000==0:
		print(i,t)
	entry,entry2=solve(list(t))
	silver.add(entry)
	# group same valves with different order together to find the best order
	general=tuple(sorted(t))
	if general not in best:
		best[general]=set()
	best[general].add(entry2)

# Part 2 is finding the 2 sets of moves that do not interest, adding their
best={k:max(v) for k,v in best.items()}
gold=set()
for route1 in best:
	# find remaining viable valve combinations and their best value
	rest=viable-set(route1)
	candidates=list(itertools.combinations(rest,max_open))
	for c in candidates:
		route2=tuple(sorted(c))
		total=best[route1]+best[route2]
		gold.add(total)

print(max(silver),max(gold))