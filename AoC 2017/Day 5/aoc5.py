# 2023-10-17
#Start	19:33
#Part1	19:41 8min 
#Part2	19:45 4min
#Total	12min
with open('input') as f:
	lista=f.read().splitlines()

test=[0,3,0,1,-3]

lista=[int(l) for l in lista]

def escape(l):
	l=l.copy()
	answer=0
	pos=0
	while pos in range(len(l)):
		newpos=pos+l[pos]
		l[pos]+=1
		pos=newpos
		answer+=1
	return answer

def escape2(l):
	l=l.copy()
	answer=0
	pos=0
	while pos in range(len(l)):
		newpos=pos+l[pos]
		if l[pos]>=3:
			l[pos]-=1
		else:
			l[pos]+=1
		pos=newpos
		answer+=1
	return answer


print(escape(lista))

print(escape2(lista))