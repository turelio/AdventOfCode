# 2023-12-04
#Start	11:20
#Part1	11:29	9min
#Part2	11:47	18min
#Total	27min
from textwrap import wrap
with open('input') as f:
	lista=f.read().strip()

x,y=25, 6
# wrap splits every nth character
layers=wrap(lista,(x*y))
silver=[1000000,None]

for l in layers:
	if l.count('0')<silver[0]:
		silver=[l.count('0'),l]

layers=[wrap(l,x) for l in layers]
screen=[[None]*x for _ in range(y)]

for y1 in range(y):
	for x1 in range(x):
		for layer in layers:
			if layer[y1][x1] in ['0','1']:
				screen[y1][x1]=layer[y1][x1]
				break

print('Silver:',silver[1].count('1')*silver[1].count('2'))
print('Gold:')
for s in screen:
	s=['█' if s2=='1' else ' ' for s2 in s]
	print(''.join(s))