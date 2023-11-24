# 2023-11-24
#Start	11:25
#Part1	11:40	15min
#Part2	12:51	71min
#Total	86min

s='10111100110001111'
n=272
n=35651584

# expand
while True:
	s2=s[::-1]
	s2=s2.replace('1','x').replace('0','1').replace('x','0')
	# print(s,s2)
	s=s+'0'+s2
	if len(s)>=n:
		s=s[:n]
		break

# faster with ints
s=list(s)
s=[int(s1) for s1 in s]


# bitwise might be faster?
def nxor(x):
	if x[0]==x[1]:
		return 1
	else:
		return 0

while True:
	print(len(s))
	# two off-by-one lists, zipped together to form consecutive pairs
	x1=s[::2]
	x2=s[1::2]
	hash=list(zip(x1,x2))

	hash=[nxor(x) for x in hash]
	# print(hash)
	s=hash
	if len(hash)%2!=0:
		break

print(''.join([str(_) for _ in s]))
