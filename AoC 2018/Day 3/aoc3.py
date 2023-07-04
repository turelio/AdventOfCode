# 2022-12-03
#Start	9:35
#Part1	9:58
#Part2	10:14
#Total	39min
import re
with open('input') as f:
	lista=f.read().splitlines()

## Second pass, 132s -> 16s
ids={}

for k,v in enumerate(lista):
	test=v
	result = re.search(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", test)
	coords={'id':int(result[1]), 'x':int(result[2]), 'y':int(result[3]), 'width':int(result[4]), 'height':int(result[5])}
	ids[coords['id']]=set()
	overlaps=False
	for i in range(coords['height']):
		for j in range(coords['width']):
			ids[k+1].add((coords['x']+j,coords['y']+i))

gold=0
silver=set()
for i in ids:
	overlaps=0
	for j in ids:
		if i==j:
			continue
		if len(ids[i]&ids[j])>0:
			overlaps=1
			silver.update(ids[i]&ids[j])
	if not overlaps:
		gold=i
print(len(silver),gold)

# # First pass
# grid=[[[] for j in range(0,2000)] for i in range(0,2000)]

# for l in lista:
# 	test=l
# 	result = re.search(r"#(\d+) @ (\d+),(\d+): (\d+)x(\d+)", test)
# 	coords={'id':int(result[1]), 'x':int(result[2]), 'y':int(result[3]), 'width':int(result[4]), 'height':int(result[5])}
# 	print(test,coords)
# 	overlaps=False
# 	for i in range(coords['height']):
# 		for j in range(coords['width']):
# 			grid[coords['y']+i][coords['x']+j].append(coords['id'])
# print(len(lista))

# silver=0
# for i in grid:
# 	for j in i:
# 		if len(j)>1:
# 			silver+=1

# for x in range(1,len(lista)+1):
# 	overlaps=False
# 	print(f'checking {x}')
# 	for i in grid:
# 		if overlaps:
# 			break
# 		for j in i:
# 			if len(j)>1 and x in j:
# 				overlaps=True
# 				break
# 	if not overlaps:
# 		print(f'gold {x}')
# 		break

# print(f'silver {silver}')