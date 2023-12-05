# 2023-10-17, 2023-12-04
#Start	18:30 		
#Part1	19:03		33min, stopped
#Part2	12:10-12:30	40min
#Total	74min
import re

with open('input') as f:
	lista=f.read().strip()

def decompress(s):
	answer=''
	while len(s)!=0:
		first=re.match(r'\w+', s)
		if first !=None:
			answer+=first[0]
			s=s[len(first[0]):]
		else:
			bracket=re.match(r'\((\d+)x(\d+)\)',s)
			n=int(bracket.groups()[1])
			i=int(bracket.groups()[0])
			bracket=bracket[0]
			s=s[len(bracket):]
			repeated=s[:i]
			answer+=repeated*n
			s=s[i:]
	return answer

def decompress2(s):
	occ=[1]*len(s)
	test=list(re.finditer(r'\((\d+)x(\d+)\)',s))
	# multiply counts of characters after parentheses
	for p in test:
		n,j=p.groups()
		s1,s2=p.span()[1],p.span()[1]+int(n)
		for j2 in range(s1,s2):
			occ[j2]*=int(j)
	# all parentheses counts are 0 because they're unpacked
	for p in test:
		s1,s2=p.span()
		for j2 in range(s1,s2):
			occ[j2]=0
	return sum(occ)

# Silver:
print('Silver:',len(decompress(lista)))
print('Gold:',decompress2(lista))