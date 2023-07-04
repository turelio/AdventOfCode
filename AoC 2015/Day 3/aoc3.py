# 2022-02-02
#Start	10:15	
#Part1	10:30
#Part2	10:37
#Total	22min
with open('input') as f:
	lista=f.read()
print(lista, len(lista))

gifts=['0-0']
x=0
y=0
for i in lista:
	if i=='>':
		x+=1
	elif i=='<':
		x-=1
	elif i =='v':
		y-=1
	else:
		y+=1
	gifts.append(f'{x}-{y}')

print(len(set(gifts)))

gold=['0-0', '0-0']
x1=0
y1=0
y2=0
x2=0
odd=True
for i in lista:
	if odd:
		if i=='>':
			x1+=1
		elif i=='<':
			x1-=1
		elif i =='v':
			y1-=1
		else:
			y1+=1
		gold.append(f'{x1}-{y1}')
	else:
		if i=='<':
			x2-=1
		elif i=='>':
			x2+=1
		elif i =='^':
			y2+=1
		else:
			y2-=1
		gold.append(f'{x2}-{y2}')
	odd=not odd

print(len(set(gold)))

