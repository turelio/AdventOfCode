# 2022-12-26
#Part1	20:43-21:23	(40min)
#Part2	21:23-21:24	(1min)
#Total	41min
lista='vzbxkghb'
test='caaaaaaz'
cons='abcdefghijklmnopqrstuvwxyz'
cons=[cons[i: i+3] for i in range(len(cons) - 3 + 1)]
print(cons)
cons=set(cons)

def check(n):
	triples=set([n[i: i+3] for i in range(len(n) - 3 + 1)])
	if len(triples&cons)>0:
		pass
		# print('C1 pass')
	else:
		# print('C1 fail')
		return False
	c2=True 
	for i in ['i','o','l']:
		if i in n:
			c2=False
			break
	if not c2:
		# print('C2 fail')
		return False
	# print('C2 pass')

#    Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
	c3=0
	i=0
	while i<len(n)-1:
		if n[i]==n[i+1]:
			c3+=1
			i+=1
		i+=1
	# print(c3)
	if c3>=2:
		# print('C3 pass')
		return True
	else:
		# print('C3 fail')
		return False

def inc(n):
	new=''
	leftover=True
	for i in n[::-1]:
		if leftover:
			val=ord(i)
			if val==122:
				new+=chr(97)
			else:
				new+=chr(val+1)
				leftover=False
			# print(i, val, chr(val+1))
		else:
			new+=i
	new=new[::-1]
	# print(n,'=>',new)
	return new

# inc(lista)

# check('abcdffaa')
# lista='ghijklmn'
while True:
	lista=inc(lista)
	if check(lista):
		print(lista)
		break

while True:
	lista=inc(lista)
	if check(lista):
		print(lista)
		break