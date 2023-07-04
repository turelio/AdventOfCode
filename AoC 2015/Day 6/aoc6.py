# 2022-12-26
#Part1	18:05-18:18	13min
#Part2	18:21-18:25	4min
#Total	17min
import re
with open('input') as f:
	lista=f.read().splitlines()

grid=[[False for i in range(1000)] for j in range(1000)]

for l in lista:
	# print(l)
	if re.match(r'toggle (\d*),(\d*) through (\d*),(\d*)',l):
		result=re.search(r'toggle (\d*),(\d*) through (\d*),(\d*)',l)
		print(result.groups())
		x1,x2,y1,y2=int(result[1]),int(result[3]),int(result[2]),int(result[4])
		for x in range(x1,x2+1):
			for y in range(y1,y2+1):
				grid[y][x]=not grid[y][x]
	elif re.match(r'turn off (\d*),(\d*) through (\d*),(\d*)',l):
		result=re.search(r'turn off (\d*),(\d*) through (\d*),(\d*)',l)
		x1,x2,y1,y2=int(result[1]),int(result[3]),int(result[2]),int(result[4])
		for x in range(x1,x2+1):
			for y in range(y1,y2+1):
				grid[y][x]=False
	elif re.match(r'turn on (\d*),(\d*) through (\d*),(\d*)',l):
		result=re.search(r'turn on (\d*),(\d*) through (\d*),(\d*)',l)
		x1,x2,y1,y2=int(result[1]),int(result[3]),int(result[2]),int(result[4])
		for x in range(x1,x2+1):
			for y in range(y1,y2+1):
				grid[y][x]=True
	else:
		print('not found')

silver=0
for i in grid:
	for j in i:
		if j:
			silver+=1


grid=[[0 for i in range(1000)] for j in range(1000)]

for l in lista:
	# print(l)
	if re.match(r'toggle (\d*),(\d*) through (\d*),(\d*)',l):
		result=re.search(r'toggle (\d*),(\d*) through (\d*),(\d*)',l)
		print(result.groups())
		x1,x2,y1,y2=int(result[1]),int(result[3]),int(result[2]),int(result[4])
		for x in range(x1,x2+1):
			for y in range(y1,y2+1):
				grid[y][x]+=2
	elif re.match(r'turn off (\d*),(\d*) through (\d*),(\d*)',l):
		result=re.search(r'turn off (\d*),(\d*) through (\d*),(\d*)',l)
		x1,x2,y1,y2=int(result[1]),int(result[3]),int(result[2]),int(result[4])
		for x in range(x1,x2+1):
			for y in range(y1,y2+1):
				if grid[y][x]!=0:
					grid[y][x]-=1
	elif re.match(r'turn on (\d*),(\d*) through (\d*),(\d*)',l):
		result=re.search(r'turn on (\d*),(\d*) through (\d*),(\d*)',l)
		x1,x2,y1,y2=int(result[1]),int(result[3]),int(result[2]),int(result[4])
		for x in range(x1,x2+1):
			for y in range(y1,y2+1):
				grid[y][x]+=1
	else:
		print('not found')

gold=0
for y in grid:
	for x in y:
			gold+=x

print(silver,gold)
