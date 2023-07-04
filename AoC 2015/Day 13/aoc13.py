#2022-12-28
#Part1	11:43-11:58	(15min)
#Part2	11:58-12:03 (5min)
#Total	20min
import itertools

with open('input') as f:
	lista=f.read().splitlines()

h={}
for l in lista:
	l=l.split(' ')
	print(l[0], l[2], l[3], l[-1])
	start=l[0]
	end=l[-1][:-1]
	if l[2]=='lose':
		val=-1*int(l[3])
	else:
		val=int(l[3])
	if start not in h:
		h[start]={}
	h[start][end]=val

guests=list(h.keys())

print(h)
def check(n):
	suma=0
	for i,v in enumerate(n):
		if v=='Me':
			continue
		left=(i-1)%len(n)
		right=(i+1)%len(n)
		# print(n[left],v,n[right])
		if  n[left]!='Me':
			suma+=h[v][n[left]]
		if n[right]!='Me':
			suma+=h[v][n[right]]
	return suma
print(guests)
print(check(guests))

guests2=itertools.permutations(guests)
silver=[]
for i in guests2:
	silver.append(check(i))

print(max(silver))

guests.append('Me')
print(guests)
guests3=itertools.permutations(guests)

gold=[]
for i in guests3:
	gold.append(check(i))

print(max(gold))
