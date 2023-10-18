# 2023-10-18
#Start	12:26
#Part1	12:44	18min
#Part2	stopped
#Total
with open('input') as f:
	lista=f.read()

lista=[int(t) for t in lista.split()]
# print(lista)
test='2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2'
test=[int(t) for t in test.split()]
# print(test)
silver=[]
def decode(n,i=0):
	print('pos',i)
	nodes=n[i]
	meta=n[i+1]
	i=i+2
	for node in range(nodes):
		i=decode(n,i)
	for m in range(meta):
		silver.append(n[i+m])
	i=i+meta
	return i
	# print(f'{nodes} nodes, {meta} metadata')
decode(lista)
print(sum(silver))

