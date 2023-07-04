#Start	9:18
#Part1	9:59
#Part2	10:53
#Total	95min

# Second pass, ~130s
import re
with open('input') as f:
	lista=f.read().splitlines()

area=4000000

def manhattan(x,y,n):
	positions=set()
	for i in range(n+1):
		if y+i==2000000 or y-i==2000000:
			for j in range(x-n+i, x+n-i+1):
				if y+i==2000000:
					positions.add((j, y+i))
				else:	
					positions.add((j, y-i))
	return(positions)

def isoverlap(x0,y0,x,y):
	for s in sensors:
		if s[0]==x0 and s[1]==y0:
			continue
		if (abs(x-s[0])+abs(y-s[1]))<=s[2]:
			return False
	if x in range(area+1) and y in range(area+1):
		return True


def outer_ring(x,y,n):
	for i in range(n+1):
			if isoverlap(x,y,x-n+i, y+i):
				return x-n+i, y+i
			elif isoverlap(x,y,x-n+i, y-i):
				return x-n+i, y-i
			elif isoverlap(x,y,x+n-i, y+i):
				return x+n-i, y+i
			elif isoverlap(x,y,x+n-i, y-i):
				return x+n-i, y-i			
	return False

silver=set()
sensors=[]
sb=[]
for l in lista:
	# print(l)
	result=re.search(r'Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)', l)
	sx,sy=int(result[1]),int(result[2])
	bx,by=int(result[3]),int(result[4])
	sb.append((sx,sy))
	sb.append((bx,by))
	distance=abs(sx-bx)+abs(sy-by)
	sensors.append((sx,sy,distance))
	silver.update(manhattan(sx,sy,distance))

for i in sb:
	if i in silver:
		silver.remove(i)
print('Silver:',len(silver))

found=False
for s1 in sensors:
	print(f'check outer ring of {s1}')
	result=outer_ring(s1[0],s1[1],s1[2]+1)
	if result!=False:
		print(result)
		break
print(f'Gold: {result[0]*4000000+result[1]} ({result[0]} * 4000000 + {result[1]})')

# # First pass, ~4min
# import re
# with open('input') as f:
# 	lista=f.read().splitlines()

# def manhattan(x,y,n):
# 	positions=set()
# 	for i in range(n+1):
# 		if y+i==2000000 or y-i==2000000:
# 			for j in range(x-n+i, x+n-i+1):
# 				if y+i==2000000:
# 					positions.add((j, y+i))
# 				else:	
# 					positions.add((j, y-i))
# 	return(positions)

# def outer_ring(x,y,n):
# 	positions=set()
# 	for i in range(n+1):
# 			positions.add((x-n+i, y+i))
# 			positions.add((x+n-i, y-i))
# 			positions.add((x-n+i, y-i))
# 			positions.add((x+n-i, y+i))
# 	return(positions)

# silver=set()
# sensors=[]
# sb=[]
# for l in lista:
# 	# print(l)
# 	result=re.search(r'Sensor at x=(.*), y=(.*): closest beacon is at x=(.*), y=(.*)', l)
# 	# print(result.groups())
# 	sx,sy=int(result[1]),int(result[2])
# 	bx,by=int(result[3]),int(result[4])
# 	sb.append((sx,sy))
# 	sb.append((bx,by))
# 	distance=abs(sx-bx)+abs(sy-by)
# 	sensors.append((sx,sy,distance))
# 	print(sx,sy,bx,by,distance)
# 	silver.update(manhattan(sx,sy,distance))

# for i in sb:
# 	if i in silver:
# 		silver.remove(i)
# print(len(silver))

# # 3138881, 3364986
# area=4000000
# # print(len(sensors))
# print((3138881*4000000)+3364986)
# found=False
# for s1 in sensors:
# 	print(f'check outer ring of {s1}')
# 	if found:
# 		break
# 	edge=outer_ring(s1[0],s1[1],s1[2]+1)
# 	for e in edge:
# 		# print(f'\tcheck {e} for overlaps')
# 		overlap=False
# 		for s2 in sensors:
# 			if s2[0]==s1[0] and s2[1]==s1[1]:
# 				continue
# 			if (abs(e[0]-s2[0])+abs(e[1]-s2[1]))<=s2[2]:
# 				overlap=True
# 				break
# 		if not overlap:
# 			if e[0] in range(area+1) and e[1] in range(area+1):
# 				print(e)
# 				found=True
# 				break