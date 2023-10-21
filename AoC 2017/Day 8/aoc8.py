# 2023-10-21
#Start	18:43
#Part1	18:54	11min
#Part2	18:56	2min
#Total	13min
with open('input') as f:
	lista=f.read().splitlines()

# registers
r={}
gold=0
for l in lista:
	l=l.split()
	if l[0] not in r:
		r[l[0]]=0
	if l[-3] not in r:
		r[l[-3]]=0
	statement=f'r["{l[4]}"]{l[-2]}int({l[-1]})'
	if eval(statement):
		if l[1]=='inc':
			r[l[0]]+=int(l[2])
		else:
			r[l[0]]-=int(l[2])
		if r[l[0]]>gold:
			gold=r[l[0]]

	print(l, r)
	# print(statement)
	# print(eval(statement))

print(gold)