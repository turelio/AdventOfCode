# 2023-10-18
#Start	14:47
#Part1	14:54	7min
#Part2	15:19	25min
#Total	32min
# remember about deep copies
import copy
with open('input') as f:
	lista=f.read().splitlines()

lista2=lista.copy()
lista2=[l.split(' ') for l in lista2]
lista2=[[l[0], int(l[1])] for l in lista2]

def execute(lista):
	i=0
	acc=0
	tried=set()
	while True:
		if i in tried:
			return acc,0
		if i>=len(lista):
			return acc,1
		tried.add(i)
		op,n=lista[i]
		# print(op, n)
		if op=='nop':
			i+=1
		if op=='acc':
			acc+=n
			i+=1
		if op=='jmp':
			i+=n

# print(execute(lista2))

for i, l in enumerate(lista2):
	lista3=copy.deepcopy(lista2)
	if l[0]=='acc':
		print(i, lista3[:10])
		continue
	elif l[0]=='jmp':
		lista3[i][0]='nop'
	else:
		lista3[i][0]='jmp'
	print(i, lista3[:10])
	test=execute(lista3)
	if test[1]==1:
		gold=test
		print(i, lista2[i], test)
	# print(i,l)

print(gold)