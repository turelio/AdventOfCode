# 2023-11-24
#Start	15:17
#Part1	15:55	38min
#Part2	17:22 	87min
#Total	125min
# n=5


def solve(n):
	e=[[i,1] for i in range(1,n+1)]
	while True:
		# print(e)
		# print(e)
		if len(e)==2:
			print(e)
			print(e[0][0],e[0][1]+e[1][1])
			break
		odd=False
		if len(e)%2!=0:
			odd=True
		if odd:
			last=e.pop()
		x1=e[::2]
		x2=e[1::2]
		test=list(zip(x1,x2))
		test=[[t[0][0],t[0][1]+t[1][1]] for t in test]
		# print(test)
		if odd:
			e=[last]+test
		else:
			e=test
		print()
solve(5)

# takes 70 blasted minutes to solve, can't figure out another solution
def solve2(n):
	e=[[i,1] for i in range(1,n+1)]

	while len(e)!=1:
		if len(e)%1000==0:
			print(len(e))
		current=e[0]
		d=len(e)//2
		opposite=e.pop(d)
		current=[current[0],current[1]+opposite[1]]
		e.pop(0)
		e.append(current)
	print(e)

solve2(3017957)