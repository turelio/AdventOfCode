# 2023-12-14
# Start	09:00	
# Part1	09:17	17min
# Part2	09:56	39min
# Total	56min
with open('input') as f:
	lista=f.read().splitlines()
lista=[list(l) for l in lista]

def tilt(lista,d):
	#transpose so the rocks always go up and from the top row
	if d=='U':
		pass
	elif d=='D':
		lista=lista[::-1]
	elif d=='L':
		lista=list(zip(*lista))
		lista=[list(l) for l in lista]
	elif d=='R':
		lista=list(zip(*lista))[::-1]
		lista=[list(l) for l in lista]

	for y in range(1,len(lista)):
		for x in range(len(lista[0])):
			if lista[y][x]=='O':
				y2=y
				while True:
					if (y2-1) in range(len(lista)):
						if lista[y2-1][x]=='.':
							y2-=1
						else:
							break
					else:
						break
				if y2!=y:
					lista[y2][x]='O'
					lista[y][x]='.'
	# revert transposition
	if d=='U':
		pass
	elif d=='D':
		lista=lista[::-1]
	elif d=='L':
		lista=list(zip(*lista))
		lista=[list(l) for l in lista]
	elif d=='R':
		lista=lista[::-1]
		lista=list(zip(*lista))
		lista=[list(l) for l in lista]
	return lista

silver=sum([l.count('O')*(len(lista)-i) for i,l in enumerate(tilt(lista,'U'))])
print('Silver:',silver)

# Part 2
states={}
dirs=['U','L','D','R']
for i in range(1,4000):
	for d in dirs:
		lista=tilt(lista,d)
	# print(f'after cycle {i}:')
	s=str(lista)
	if s not in states:
		states[s]=(i,i)
	else:
		states[s]=(i,i-states[s][0])
		# print('already happened',states[s])
		if (1000000000-i)%states[s][1]==0:
			gold=sum([l.count('O')*(len(lista)-i) for i,l in enumerate(lista)])
			break

print('Gold:',gold)