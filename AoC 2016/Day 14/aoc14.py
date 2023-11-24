# 2023-11-24
#Start	08:41
#Part1	09:32	51min
#Part2	09:55	23min
#Total	74min
import hashlib, itertools

def solve(s,gold=False):
	c1=[]
	c2=set()
	i=0
	while True:
		initial=s+str(i)
		if gold:
			phrase=initial
			for _ in range(2017):
				phrase=hashlib.md5(phrase.encode()).hexdigest()
		else:
			phrase=hashlib.md5(initial.encode()).hexdigest()
		test=[list(g) for k, g in itertools.groupby(phrase)]
		# print(test)
		# first=False
		c5=[t[0] for t in test if len(t)>=5]
		if len(c5)>=0:
			for quint in c5:
				for c in c1:
					if i-1000<=c[0] and c[1]==quint[0]:
						c2.add(c)
						print(len(c2), c)
		for t in test:
			if len(t)>=3:
				c1.append((i,t[0]))
				break
		if len(c2)>=64:
			break
		i+=1

	print(sorted(list(c2))[63])

s='yjdafjpo'
# s='abc'
solve(s)
solve(s,True)
