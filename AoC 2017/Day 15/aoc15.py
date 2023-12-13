# 2023-12-04
#Start	10:15
#Part1	10:25	10min
#Part2	10:32	7min
#Total	17min
# accidently deleted
a=289
b=629
fa=16807
fb=48271
d=2147483647
silver=0
for i in range(40000000):
	if i%10000000==0:
		print(i)
	a=(a*fa)%d
	b=(b*fb)%d
	if a&0xffff==b&0xffff:
		silver+=1
print('Silver:',silver)

gold=0
i=0
a=289
b=629
while i<5000000:
	if i%1000000==0:
		print(i)
	a=(a*fa)%d
	while a%4!=0:
		a=(a*fa)%d
	b=(b*fb)%d
	while b%8!=0:
		b=(b*fb)%d
	#0xffff is 65535 decimal or 16 1bits, using & returns only lowest 16 bits of value or value if it's lower than that
	if a&0xffff==b&0xffff:
		gold+=1
	i+=1
print('Gold:',gold)