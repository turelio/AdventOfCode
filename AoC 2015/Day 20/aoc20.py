#2022-12-29
#Part1	10:12-10:25 (13min)
#Part2	10:25-10:55 (30min)
#Total	43min

lista=36000000.0

import math

# copied for optimization
def divisorGenerator(n):
	large_divisors = []
	for i in range(1, int(math.sqrt(n) + 1)):
		if n % i == 0:
			yield i
			if i*i != n:
				large_divisors.append(n / i)
	for divisor in reversed(large_divisors):
		yield divisor

i=0
silver=0
gold=0
while True:
	if i%100000==0:
		print(i)
	divisors=list(divisorGenerator(i))
	n2=0
	for d in divisors:
		if d*50>=i:
			n2+=d
	n=sum(divisors)*10
	n2=n2*11

	if n>=lista and silver==0:
		print(i,n)
		silver=i
	if n2>=lista and gold==0:
		print(i,n2)
		gold=i
		break
	i+=1

print(silver, gold)