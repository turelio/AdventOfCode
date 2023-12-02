# 2023-12-02
# Start	06:00
# Part1	06:15	15min
# Part2	06:21	6min
# Total	21min
with open('input') as f:
	lista=f.read().splitlines()

silver,gold=0,0

for l in lista:
	n, bags=l.split(': ')
	n=int(n[5:])
	rounds=[round.split(', ') for round in bags.split('; ')]
	valid=True
	cmax={'blue':0,'green':0,'red':0}
	for r in rounds:
		colors={'blue':0,'green':0,'red':0}
		for b in r:
			x,color=b.split(' ')
			colors[color]+=int(x)
		for k in cmax:
			if colors[k]>cmax[k]:
				cmax[k]=colors[k]
		if colors['red']>12 or colors['green']>13 or colors['blue']>14:
			valid=False
	if valid:
		silver+=n
	prod=1
	for y in cmax.values():
		prod*=y
	gold+=prod

print(silver,gold)