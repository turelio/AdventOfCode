# 2023-12-13
#Start	13:14
#Part1	13:21	7min
#Part2	14:14	53min - 20min = 33min
#Total	40min

n=363
lock=[0]
pos=0
print(lock)
for i in range(1,2018):
	print('step %s' % i)
	pos=(pos+n)%len(lock)+1
	lock=lock[:pos]+[i]+lock[pos:]
	lock.insert(pos,i)
print (lock[pos+1])

# bruteforce too slow, guessed right after over 1m repeats
lock=[0]
for i in range(1,50000001):
	pos=(pos+n)%len(lock)+1
	lock.insert(pos,i)
	# lock=lock[:pos]+[i]+lock[pos:]
	# print('\t',lock,pos)
	if i%10000==0:
		z=lock.index(0)
		print('step %s' % i)
		print(z, lock[z], z+1,lock[z+1])
print (lock[z+1])



