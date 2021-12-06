#Start	15:47	2021-12-06
#Part1	15:50	3min
#Part2	16:26	36min
#Total	39min
with open('input') as f:
	lista=f.read().strip().splitlines()


freq=[0]
for l in lista:
	if l[0]=="+":
		res=freq[-1]+int(l[1:])
		if res in freq:
			print(res)
		freq.append(res)
		#print(f"{freq[-2]}\t+\t{int(l[1:])}\t=\t{freq[-1]}")
	elif l[0]=="-":
		res=freq[-1]-int(l[1:])
		if res in freq:
			print(res)	
		freq.append(res)
		#print(f"{freq[-2]}\t-\t{int(l[1:])}\t=\t{freq[-1]}")

print(freq[-1])

#part 2
freq=[0]
i=0
while True:
	if i>len(lista)-1:
		i=0
	if lista[i][0]=="+":
		res=freq[-1]+int(lista[i][1:])
		if res in freq:
			print(res)
			break
		freq.append(res)
	elif lista[i][0]=="-":
		res=freq[-1]-int(lista[i][1:])
		if res in freq:
			print(res)
			break	
		freq.append(res)
	print(len(freq))
	i+=1