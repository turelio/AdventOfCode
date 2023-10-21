# 2023-10-21
#Start	16:23
#Part1	16:38	15min
#Part2	16:45	7min
#Total	22min
with open('input') as f:
	lista=f.read().splitlines()

lista=[int(l) for l in lista]

# print(lista[:25], lista[25:])

prev=lista[:25]
test=lista[25:]
for l in test:
	valid=False
	for i,v in enumerate(prev):
		rest=l-v
		if rest in prev:
			if prev.count(rest)==1 and prev[i]==rest:
				continue
			else:
				valid=True
				break
	if not valid:
		print(l, 'invalid')
		silver=l
		break
	prev.pop(0)
	prev.append(l)

print(l)
n=2

# might break b/c of ranges but worked
while True:
	found=False
	for i,v in enumerate(lista):
		entry=lista[i:i+n]
		if sum(entry)==silver:
			found=True

			print(sum(entry), min(entry)+max(entry))
			break
	if found:
		break
	n+=1