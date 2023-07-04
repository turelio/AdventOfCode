#Start	10:37
#Part1	11:54 (87min)
#Part2	
#Total
with open('input') as f:
	lista=f.read().splitlines()

def snafu(l):
	result=l[::-1]
	suma=0
	for i,r in enumerate(result):
		if r=='=':
			value=-2
		elif r=='-':
			value=-1
		else:
			value=int(r)
		suma+=(5**i)*value
	return suma

coded={2:'2',1:'1',0:'0',-1:'-',-2:'='}
def reverse_snafu(n):
	snafu=[]
	while n>0:
		rest=n%5
		snafu.append(rest)
		n=n//5
	print(snafu)
	for p,v in enumerate(snafu):
		if v>2:
			snafu[p]=v-5
			snafu[p+1]+=1
	print(snafu)
	snafu=snafu[::-1]
	snafu=list(map(lambda x:coded[x], snafu))

	print(''.join(snafu))

silver=0
for l in lista:
	silver+=snafu(l)

print(snafu('2=-1=0'))
print(silver)

reverse_snafu(33078355623611)
reverse_snafu(221)
