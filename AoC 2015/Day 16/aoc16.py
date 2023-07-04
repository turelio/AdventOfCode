#2022-12-28
#Part1	13:27-13:34	(7min)
#Part2	13:34-13:48	(14min)
#Total	21min
with open('input') as f:
	lista=f.read().splitlines()

sample={
'children': 3,
'cats': 7,
'samoyeds': 2,
'pomeranians': 3,
'akitas': 0,
'vizslas': 0,
'goldfish': 5,
'trees': 3,
'cars': 2,
'perfumes': 1
}


for l in lista:
	l=l.split(' ')
	i1,v1=l[2][:-1], int(l[3][:-1])
	i2,v2=l[4][:-1], int(l[5][:-1])
	i3,v3=l[6][:-1], int(l[7])
	info=[(l[2][:-1], int(l[3][:-1])),(l[4][:-1], int(l[5][:-1])),(l[6][:-1], int(l[7]))]
	silver=True
	gold=True
	for i in info:
		if sample[i[0]]!=i[1]:
			silver=False
		if i[0] in ['cats', 'trees']:
			if sample[i[0]]>i[1]:
				gold=False
		elif i[0] in ['pomeranians', 'goldfish']:
			if sample[i[0]]<=i[1]:
				gold=False
		else:
			if sample[i[0]]!=i[1]:
				gold=False

	if silver:
		print('Silver: Sue', l[1][:-1])
	if gold:
		print('Gold: Sue', l[1][:-1])