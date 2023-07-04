#2012-12-26
#Part1	18:26-19:16 (50min)
#Part2	19:17-19:19 (2min)
#Total	52min
with open('input') as f:
	lista=f.read().splitlines()

import re

w={}

def resolve(n):
	# print(n, type(n))
	if re.match(r'\d+', n):
		return int(n)
	elif n in w.keys():
		return w[n]
	else:
		op(k[n])
		return w[n]

def op(l):
	l=l.split(' ')
	if 'AND' in l:
		result=resolve(l[0]) & resolve(l[2])
		w[l[4]]=result
	elif 'OR' in l:
		result=resolve(l[0]) | resolve(l[2])
		w[l[4]]=result
	elif 'LSHIFT' in l:
		result=resolve(l[0])<<int(l[2])
		w[l[4]]=result
	elif 'RSHIFT' in l:
		result=resolve(l[0])>>int(l[2])
		w[l[4]]=result
	elif 'NOT' in l:
		result=~resolve(l[1])
		while result<0:
			result=65536+result
		w[l[3]]=result
	else:
		result=resolve(l[0])
		w[l[2]]=result
	# print(f'\t{l[-1]} is now {result}')
	return result

k={}
for l in lista:
	k[l.split(' ')[-1]]=l

print('Silver:',op(k['a']))

w={}
w['b']=46065
print('Gold:',op(k['a']))
