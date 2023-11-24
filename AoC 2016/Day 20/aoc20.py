# 2023-11-24
#Start	17:26
#Part1	17:59	33min
#Part2	18:03	4min
#Total	37min
with open('input') as f:
	lista=f.read().splitlines()

bans=[]
for l in lista:
	l=l.split('-')
	bans.append([int(l[0]),int(l[1])])

# print(bans)

while True:
	start=len(bans)
	# print(start)
	reduced=False
	for i,v1 in enumerate(bans):
		for j, v2 in enumerate(bans):
			new=None
			if v1==v2:
				continue
			# extend lower range:
			if v2[0]<=v1[0] and v1[0]<=v2[1]<=v1[1]-1:
				# print('lower range')
				new=[v2[0],v1[1]]
			elif v1[1]+1>=v2[0]>=v1[0] and v2[1]>=v1[1]:
				# print('higher range')
				new=[v1[0],v2[1]]
			elif v2[0]<=v1[0] and v2[1]>=v1[1]:
				# print('encapsulates')
				new=[v2[0],v2[1]]
			elif v2[0]>v1[0] and v2[1]<v1[1]:
				# print('within')
				new=v1
			else:
				continue
			if new!=None:
				# print(f'merged {v1} with {v2} into {new}')
				bans[i]=new
				bans.pop(j)
				reduced=True
				break
		if reduced:
			break
	if len(bans)==start:
		break

silver=sorted(bans)
print('Silver: ',silver[0][1]+1)
bans=[x[1]-x[0]+1 for x in bans]
print('Gold: ',4294967296-sum(bans))