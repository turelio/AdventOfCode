
#Start	13:24
#Part1	1347
#Part2	13:55
#Total	30min
import re
with open('input') as f:
	lista=f.read().splitlines()

# not gonna parse this shit lol
silver={'1':["F","H", "B", "V","R", "Q", "D", "P"],
'2':["L", "D", "Z",'Q','W','V'], 
'3':["H",'L','Z','Q','G','R','P','C'],
'4':['R', 'D', 'H', 'F', 'J', 'V', 'B'], 
'5':['Z', 'W', 'L', 'C'], 
'6':['J', 'R', 'P', 'N', 'T', 'G', 'V', 'M'], 
'7':['J', 'R', 'L', 'V', 'M', 'B', 'S'], 
'8':['D', 'P', 'J'], 
'9':['D', 'C', 'N','W','V']}

gold={'1':["F","H", "B", "V","R", "Q", "D", "P"],
'2':["L", "D", "Z",'Q','W','V'], 
'3':["H",'L','Z','Q','G','R','P','C'],
'4':['R', 'D', 'H', 'F', 'J', 'V', 'B'], 
'5':['Z', 'W', 'L', 'C'], 
'6':['J', 'R', 'P', 'N', 'T', 'G', 'V', 'M'], 
'7':['J', 'R', 'L', 'V', 'M', 'B', 'S'], 
'8':['D', 'P', 'J'], 
'9':['D', 'C', 'N','W','V']}

for i in lista[10:]:
	# 0 - count, 1 - start, 2 - end
	result=re.search(r'move (\d+) from (\d+) to (\d+)', i)
	result=list(result.groups())
	coords={'boxes':int(result[0]), 'start':result[1], 'end':result[2]}
	# print(coords)
	stack=[]
	for j in range(coords['boxes']):
		stack.append(gold[coords['start']].pop())
	# print(list(reversed(stack)))
	gold[coords['end']]+=list(reversed(stack))

	for j in range(coords['boxes']):
		silver[coords['end']].append(silver[coords['start']].pop())

for i in silver.keys():
	print(silver[i][-1],end='')
print('')
for i in gold.keys():
	print(gold[i][-1],end='')
print('')