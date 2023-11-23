# 2023-11-23
#Start	13:36
#Part1	14:04	28min
#Part2	N/A 	1min
#Total	29min

y=2978
x=3083

def order(x,y):
	return 1+sum(range(1,y))+sum(range(1+y,y+x))

def resolve(n):
	current=20151125
	for i in range(2,n+1):
		current=(current*252533)%33554393
	return current

silver=order(x,y)
print(silver,resolve(silver))