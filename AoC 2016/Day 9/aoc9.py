# 2023-10-17
#Start	18:30
#Part1	19:03 33min stopped
#Part2	
#Total
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

# Silver:
print(len(decompress(lista)))