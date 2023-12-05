# 2023-11-25
#Start	10:34
#Part1	11:02	32min
#Part2	stopped
#Total
import re
with open('input') as f:
	lista=f.read().splitlines()

nodes=lista[2:]

mx=0
my=0
nodes2={}
for n in nodes:
	# print(n)
	n=re.match(r'.*x(\d+)-y(\d+)\s+(\d+)T\s+(\d+)T\s+(\d+)T\s+(\d+)%',n)
	n=[int(n2) for n2 in n.groups()]
	print(n)
	x,y,size,used,avai,usep=n
	mx=max(mx,x)
	my=max(my,y)
	nodes2[(x,y)]=[size,used,avai,usep]

# print(nodes2)

print(mx,my)

silver=set()
for k,v in nodes2.items():
	for k2,v2 in nodes2.items():
		if k==k2:
			continue
		if v[1]<=v2[2] and v[1]!=0:
			silver.add((k,k2))

print(len(silver))

gy=0
gx=mx
print(gx,gy)
print(nodes2)