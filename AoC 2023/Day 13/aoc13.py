# 2023-12-13
# Start	07:48	
# Part1	08:42	54min
# Part2	08:54	12min
# Total	66min
# needed one more newline in input
with open('input') as f:
	lista=f.read().split('\n\n')
lista=[l.split('\n') for l in lista]

def diff(l1,l2):
	n=0
	for i in range(len(l1)):
		n+=sum([1 if l1[i][j]!=l2[i][j] else 0 for j in range(len(l1[i]))])
	return n

silver,gold=0,0
for l in lista:
	for i in range(len(l)-1):
		l1=l[:i+1][::-1]
		l2=l[i+1:]
		n=min(len(l1),len(l2))
		l1=l1[:n]
		l2=l2[:n]
		if diff(l1,l2)==1:
			gold+=100*(i+1)
		if l1==l2:
			silver+=100*(i+1)
	l=[list(l2) for l2 in l]
	l=list(zip(*l))
	for i in range(len(l)-1):
		l1=l[:i+1][::-1]
		l2=l[i+1:]
		n=min(len(l1),len(l2))
		l1=l1[:n]
		l2=l2[:n]
		if diff(l1,l2)==1:
			gold+=i+1
		if l1==l2:
			silver+=i+1
print('Silver:',silver)
print('Gold:',gold)
