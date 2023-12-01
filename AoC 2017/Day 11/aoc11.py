# 2023-12-01
#Start	12:47
#Part1	13:01 	14min
#Part2	13:03	2min
#Total	16min
with open('input') as f:
	lista=f.read().strip().split(',')

# redblob guide, cube coordinates
moves={'n':(0,-1,1),"ne":(1,-1,0),'se':(1,0,-1),"s":(0,1,-1),"sw":(-1,1,0),'nw':(-1,0,1)}

def distance(q,r,s):
	# manhattan distance but 3d
	return (abs(q)+abs(r)+abs(s))//2

q,r,s=0,0,0
gold=0

for l in lista:
	m=moves[l]
	q+=m[0]
	r+=m[1]
	s+=m[2]
	silver=distance(q,r,s)
	if silver>gold:
		gold=silver

print(silver, gold)
