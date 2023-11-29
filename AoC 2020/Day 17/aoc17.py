# 2023-11-29
#Start	15:03
#Part1	15:25	18min
#Part2	15:32 	7min
#Total	25min
import itertools, copy
with open('input') as f:
	lista=f.read().splitlines()

test='''.#.
..#
###'''.splitlines()
# lista=test
print(lista)


active=set()
active3=set()
for y,v1 in enumerate(lista):
	for x, v2 in enumerate(list(v1)):
		if v2=='#':
			active.add((x,y,0))
			active3.add((x,y,0,0))


def near(c):
	x,y,z=c
	result=set()
	mods=itertools.product([-1,0,1], repeat=3)
	for m in mods:
		result.add((x+m[0],y+m[1],z+m[2]))
	result.remove((x,y,z))
	# print(result,len(result))
	return result

def near2(c):
	x,y,z,w=c
	result=set()
	mods=itertools.product([-1,0,1], repeat=4)
	for m in mods:
		result.add((x+m[0],y+m[1],z+m[2],w+m[3]))
	result.remove((x,y,z,w))
	# print(result,len(result))
	return result


i=1
while i!=7:
	active2=copy.deepcopy(active)
	print('Cycle',i)
	check=set()
	check=check|active
	for c in active:
		check=check|near(c)
	for  c in check:
		neighbors=near(c)
		if c in active:
			if len(neighbors&active) not in [2,3]:
				active2.remove(c)
		else:
			if len(neighbors&active)==3:
				active2.add(c)
	active=active2
	print(f'{len(active)} active, {len(check)} to check')
	i+=1

print()

#Gold
active=active3
i=1
while i!=7:
	active2=copy.deepcopy(active)
	print('Cycle',i)
	check=set()
	check=check|active
	for c in active:
		check=check|near2(c)
	for  c in check:
		neighbors=near2(c)
		if c in active:
			if len(neighbors&active) not in [2,3]:
				active2.remove(c)
		else:
			if len(neighbors&active)==3:
				active2.add(c)
	active=active2
	print(f'{len(active)} active, {len(check)} to check')
	i+=1