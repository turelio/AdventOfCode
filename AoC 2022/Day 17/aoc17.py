
#Start	8:30
#Part1	10:15 (105min)
# stopped at 13:20
#Part2	
#Total
with open('input') as f:
	lista=f.read()
import copy

# print(lista)

# print(len(lista))

area=[['.'for i in range(7)] for i in range(100000)]


def hori(y):
	coords=[(2,y),(3,y),(4,y),(5,y)]
	return coords, 1


def cross(y):
	coords=[(3,y),(2,y+1),(3,y+1),(4,y+1),(3,y+2)]
	return coords, 3


def edge(y):
	coords=[(2,y),(3,y),(4,y),(4,y+1),(4,y+2)]
	return coords, 3


def vert(y):
	coords=[(2,y),(2,y+1),(2,y+2),(2,y+3)]
	return coords, 4


def square(y):
	coords=[(2,y),(3,y),(2,y+1),(3,y+1)]
	return coords, 2

def check(i):
	return area[i[1]][i[0]]
shapes=[hori,cross,edge,vert,square]
y=3
d=0
count=0

heights=[0]

def move(rock, x,y):
	# print(rock)
	rock2=[]
	for i in rock:
		rock2.append((i[0]+x,i[1]+y))
	return rock2
leng=len(lista)

def draw(rock):
	area2=copy.deepcopy(area)
	for i in rock:
		area2[i[1]][i[0]]='@'
	for i in area2[:25][::-1]:
		print(''.join(i))
	print('')


while count<10000:
	# print(f'rock {count+1}, starting from height {y}')
	# for i in area[:20][::-1]:
	# 	print(''.join(i))
	rock, newheight=shapes[count%5](y)
	# draw(rock)
	while True:
		#horizontal
		added=0
		if lista[d%leng]=='>':
			# print(lista[d%leng],d)
			addedx=1
		else:
			# print(lista[d%leng],d)
			addedx=-1
		newrock=move(rock,addedx,0)
		overlap=False
		for i in newrock:
			if i[0] not in range(7):
				overlap=True
				# print("\tcan't move")
				break
			if check(i)=='#':
				overlap=True
				break

		if not overlap:
			rock=newrock
		d+=1

		# draw(rock)
		#vertical
		# print('\ttry to move down')
		newrock2=move(rock,0,-1)
		# print('new',newrock2)
		stay=False
		for i in newrock2:
			if i[1]<0:
				stay=True
				# print('\t\tbelow 0')
				break
			if check(i)=='#':
				# print('\t\toverlap')
				stay=True
				break
		if stay:
			for i in rock:
				area[i[1]][i[0]]='#'
			for i1,y1 in enumerate(area):
				if '#' not in y1:
					y=i1+3
					# print('height',i1)
					heights.append(i1)
					break
			break
		else:
			rock=newrock2
		# draw(rock)
	count+=1

test=area[:20000]

print('done')

print(heights[2022])
increases=[0]
for i,v in enumerate(heights[1:]):
	increases.append(v-heights[i])

print(heights[:10], increases[:10])

def repeats(h,n):
	lists=[]
	for i,v in enumerate(h):
		if i>len(test)-n:
			continue
		entry=tuple(test[i:i+n])
		lists.append(entry)
	return lists

def same(lists):
	repeats=0
	for i1,v1 in enumerate(lists):
		last=0
		for i2,v2 in enumerate(lists):
			if i1==i2 or i2<i1+len(v1)-1:
				continue
			if v1==v2:
				repeats+=1

				print(f'{len(v1)} increases at {i1} repeat at {i2}, diff {i2-last} (height {heights[i2]})')
				last=i2
				print('')


	return repeats

same(repeats(heights,2649*2))


# for i,v1 in enumerate(heights[:3665]):
# 	if i<1006:
# 		v2=v1
# 		print(f'{i}\t\t\t{v1}\t\t\t{v2}', end='')
# 	else:
# 		base=heights[1005]
# 		e0=((i-1005)//2650)+1
# 		e1=heights[(i-1005)%2650+1005]-heights[1005]
# 		v2=base+4130*(e0-1)+e1
# 		# v2=heights[1005]+sum(increases[1006:1006+(i-1005)%2649]*(((i-1005)//2649)+1))
# 		print(f'{i}\t\t\t{v1}\t\t\t{v2}\t\t\t({base} + (4130 * {(e0-1)}) + {e1})', end='')
# 	if v2==v1:
# 		print(' correct')
# 	else:
# 		print(' false')

# def repeats(test,n):
# 	lists=[]
# 	for i,v in enumerate(test):
# 		if i>len(test)-n:
# 			continue
# 		entry=test[i:i+n]
# 		entry=[''.join(j) for j in entry]
# 		entry='\n'.join(entry)
# 		lists.append(entry)
# 	return lists
# 	# for i in lists:
# 	# 	print(i)
# 	# 	print('')
# 	# print(len(lists))


# def same(lists):
# 	repeats=0
# 	for i1,v1 in enumerate(lists):
# 		for i2,v2 in enumerate(lists):
# 			if i1==i2:
# 				continue
# 			if v1==v2:
# 				repeats+=1
# 				# print(f'{v1} at {i1} repeats at {i2}')
# 				# print('')
# 	return repeats


# i=1
# while True:
# 	print(i,':',same(repeats(test,i)))
# 	i+=1
