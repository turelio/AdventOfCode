
#Start	8:51
#Part1	8:57
#Part2	8:59
#Total	8min
with open('input') as f:
	lista=f.read()
print(len(lista))
def message_start(n):
	i=0
	while i<len(lista)-n:
		# print(i)
		if len(set(list(lista[i:i+n])))==n:
			# print(lista[i:i+n], i+n, len(set(list(lista[i:i+n]))))
			break
		i+=1
	return i+n

print('Silver:', message_start(4))
print('Gold:', message_start(14))