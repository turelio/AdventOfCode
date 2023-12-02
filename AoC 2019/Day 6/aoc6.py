# 2023-12-02
#Start	17:12
#Part1	16:34	22min
#Part2	17:53	19min
#Total	41min
with open('input') as f:
	lista=f.read().splitlines()

orbits={}
for l in lista:
	l=l.split(')')
	if l[0] not in orbits:
		orbits[l[0]]=[]
	orbits[l[0]].append(l[1])

silver=[]
def solve(p,indirect=0):
	if p=='COM':
		direct=0
	else:
		direct=1
	silver.append(direct+indirect)
	if p in orbits:
		for p2 in orbits[p]:
			solve(p2,indirect+direct)
solve('COM')


orbits={}
for l in lista:
	l=l.split(')')
	if l[0] not in orbits:
		orbits[l[0]]=[]
	if l[1] not in orbits:
		orbits[l[1]]=[]
	orbits[l[0]].append(l[1])
	orbits[l[1]].append(l[0])

visited=set()
dist={k:10000 for k in orbits.keys()}
dist['YOU']=0
queue=['YOU']
while len(queue)!=0:
	c=queue.pop(0)
	visited.add(c)
	for move in orbits[c]:
		if dist[c]+1<dist[move]:
			dist[move]=dist[c]+1
	moves=[m for m in orbits[c] if m not in visited and m not in queue]
	queue+=moves

print('Silver:',sum(silver))
print('Gold:', dist['SAN']-2)