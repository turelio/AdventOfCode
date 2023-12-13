# 2023-12-01
#Start	12:06
#Part1	12:42	36min
#Part2	X
#Total
lengths=[88,88,211,106,141,1,78,254,2,111,77,255,90,0,54,205]
# lengths=[3, 4, 1, 5]

lista=list(range(256))

n=1
i=0
skip=0
ls=len(lista)
for l in lengths:

	print(f'#####{n}')
	print(lista)
	if l==0:
		i=(i+l+skip)%ls
		skip+=1
		print(lista)
		n+=1
		continue
	j=(i+l-1)%(ls)
	print(f'at {i}={lista[i]}, length={l}, next is {j}={lista[j]}')
	i2=i
	test=[]
	while len(test)!=l:
		test.append([i2,lista[i2]])
		i2=(i2+1)%(ls)
	test=list(zip(*test))
	test[1]=test[1][::-1]
	test=list(zip(*test))
	print(test)
	for t in test:
		lista[t[0]]=t[1]
	i=(i+l+skip)%ls
	skip+=1
	print(lista)
	n+=1
	# test=list(zip(*test))

# i=0
# for x in range(50):
# 	print(i)
# 	i=(i+2)%len(lista)
print(len(lista))
print(lista[0]*lista[1])