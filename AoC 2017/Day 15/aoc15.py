# 2023-12-04
#Start	10:15
#Part1	10:25	10min
#Part2	10:32	7min
#Total	17min

a=289
b=629
# a=65
# b=8921
fa=16807
fb=48271
d=2147483647
# silver=0
# for i in range(40000000):
# 	if i%1000000==0:
# 		print(i)
# 	a=(a*fa)%d
# 	b=(b*fb)%d
# 	if a&0xffff==b&0xffff:
# 		silver+=1

# print(silver)
gold=0
i=0
while i<5000000:
	if i%100000==0:
		print(i)
	a=(a*fa)%d
	while a%4!=0:
		a=(a*fa)%d
	b=(b*fb)%d
	while b%8!=0:
		b=(b*fb)%d
	if a&0xffff==b&0xffff:
		gold+=1
	i+=1
print(gold)