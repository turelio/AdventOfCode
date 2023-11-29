# 2023-11-29
#Start	11:22
#Part1	11:29 	7min
#Part2	X
#Total
n=1002578
x=None
t=[19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,751,x,29,x,x,x,x,x,x,x,x,x,x,13,x,x,x,x,x,x,x,x,x,23,x,x,x,x,x,x,x,431,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17]


bus1=[t2 for t2 in t if t2!=None]
print(bus1)


n2=n
found=False
while True:
	for b in bus1:
		if n2%b==0:
			print(n2, n2-n, b, (n2-n)*b)
			found=1
			break
	if found:
		break
	n2+=1

t2=[7,13,x,x,59,x,31,19]
t=t2
bus2=[(i,v) for i,v in enumerate(t) if v!=None]
print(bus2)
n3=0

# something with lowest common divisors
while True:
	if n3%1000000==0:
		print(n3)
	found=True
	for i,v in bus2:
		if (n3+i)%v!=0:
			found=False
			break
	if found:
		print('found',n3)
		for i,v in bus2:
			print(i,v, n3%v)
		break
	n3+=t2[0]

# n3=0
# while True:
# 	if n3%1000000==0:
# 		print(n3)
# 	found=True
# 	for i,v in enumerate(t2):
# 		if v==None:
# 			continue
# 		elif (n3+i)%v!=0:
# 			found=False
# 			break
# 	if found:
# 		print('found',n3)
# 		break
# 	n3+=t2[0]


# n=0
# increment=1
# max_sync=0
# while True:
# 	print(n)
# 	sync=0
# 	for i,v in bus2:
# 		if (n+i)%v==0:
# 			sync+=1
# 			if sync>max_sync and n>increment:
# 				increment=n
# 				max_sync=sync
# 				print('\t new increment',increment,sync)
# 		else:
# 			found=False
# 			break
# 	if found:
# 		print('found',n3)
# 		break
# 	n+=increment