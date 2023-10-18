# 2023-10-17
#Start	22:42
#Part1	23:00	18min
#Part2	23:22	22min
#Total	40min
# very fun and fast after refactoring to reduce cycles (~70s -> 200ms)

with open('input') as f:
	lista=f.read().strip()

silver=lista

def react(lista):
	i=0
	while True:
		# print(f'polymer {len(lista)}')
		entry=lista[i:i+2]
		if len(entry)==1:
			break
		if abs(ord(entry[0])-ord(entry[1]))==32:
			lista=lista.replace(entry,'',1)
			if i!=0:
				i-=1
		else:
			i+=1
	return len(lista)

cases=set(lista.lower())
gold=len(lista)

for case in cases:
	reduced=lista.replace(case,'').replace(case.upper(),'')
	reduced=react(reduced)
	print(case, reduced)
	if reduced<gold:
		gold=reduced

print('Silver: ',react(silver))
print('Gold: ',gold)
