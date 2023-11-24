# 2023-11-24
#Start	18:27
#Part1	19:00	33min
#Part2	19:05	5min
#Total	38min
with open('input') as f:
	lista=f.read().splitlines()

# lista=['swap position 4 with position 0','swap letter d with letter b','reverse positions 0 through 4','rotate left 1 step','move position 1 to position 4','move position 3 to position 0','rotate based on position of letter b','rotate based on position of letter d']

# list version
def solve(s):
	s=list(s)
	for l in lista:
		l=l.split()
		# print(l)
		if l[0]=='swap' and l[1]=='position':
			i1=int(l[2])
			i2=int(l[5])
			temp=s[i1]
			s[i1]=s[i2]
			s[i2]=temp
		elif l[0]=='swap' and l[1]=='letter':
			i1=s.index(l[2])
			i2=s.index(l[5])
			temp=s[i1]
			s[i1]=s[i2]
			s[i2]=temp
		elif l[0]=='rotate' and len(l)==4:
			d=l[1]
			n=int(l[2])
			for _ in range(n):
				if d=='right':
					temp=s.pop()
					s=[temp]+s
				else:
					temp=s.pop(0)
					s=s+[temp]
		elif l[0]=='rotate' and len(l)==7:
			n=s.index(l[6])
			if n>=4:
				n+=1
			n+=1
			for _ in range(n):
				temp=s.pop()
				s=[temp]+s
		elif l[0]=='reverse':
			i1=int(l[2])
			i2=int(l[4])
			temp=s[i1:i2+1][::-1]
			s=s[:i1]+temp+s[i2+1:]
		elif l[0]=='move':
			i1=int(l[2])
			i2=int(l[5])
			temp=s.pop(i1)
			s=s[:i2]+[temp]+s[i2:]
		# print(s)
	return ''.join(s)
import itertools


# fuck reverse engineering, i'm bruteforcing this since it's only ~40k permutations
s='abcdefgh'
print('Silver: ',solve(s))

test=itertools.permutations('fbgdceah',8)
test=list(test)
test=[''.join(t) for t in test]
for t in test:
	answer=solve(t)
	if answer=='fbgdceah':
		print('Gold: ', t)
		break