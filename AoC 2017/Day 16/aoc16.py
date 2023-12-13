# 2023-12-13
#Start	12:14
#Part1	12:28	14min
#Part2	12:55	-7 -> 20min
#Total	34min
with open('input') as f:
	lista=f.read().split(',')

p=''.join([chr(i) for i in range(97,113)])
def dance(p):
	p=list(p)
	for l in lista:
		instr=l[0]
		v=l[1:]
		if instr=='s':
			p=p[-1*int(v):]+p[:-1*int(v)]
		elif instr=='x':
			v=v.split('/')
			x1,x2=int(v[0]),int(v[1])
			temp=p[x1]
			p[x1]=p[x2]
			p[x2]=temp
		elif instr=='p':
			v=v.split('/')
			x1,x2=p.index(v[0]),p.index(v[1])
			temp=p[x1]
			p[x1]=p[x2]
			p[x2]=temp
	return ''.join(p)

print('Silver:',dance(p))
i=0
r={}
while True:
	# break
	if p not in r:
		r[p]=[i,i]
	else:
		r[p]=[i,i-r[p][0]]
		# print(p, r[p])
		# answers loop every r[p][1] transforms
		if (1000000000-i)%r[p][1]==0:
			print('Gold:',p)
			break
	p=dance(p)
	i+=1

