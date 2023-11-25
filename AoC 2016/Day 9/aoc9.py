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

# too slow to work
current='(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
x=0
while True:
	new=decompress(current)
	print(x, len(current),len(new))
	if len(current)==len(new):
		break
	else:
		current=new

print(len(new))
