# 2023-12-09
# Start	06:25	
# Part1	06:40	15min	
# Part2	06:49	4min
# Total	19min
with open('input') as f:
	lista=f.read().splitlines()
silver,gold=0,0
for l in lista:
	l=[int(l2) for l2 in l.split()]
	s=[l]
	while True:
		l2=[s[-1][i]-s[-1][i-1] for i in range(1,len(s[-1]))]
		s.append(l2)
		if l2==[0]*len(s[-1]):
			break
	result,result2=0,0
	for s2 in s[::-1]:
		result+=s2[-1]
		result2=s2[0]-result2
	silver+=result
	gold+=result2
print(silver,gold)