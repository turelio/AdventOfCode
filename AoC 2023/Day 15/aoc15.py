# 2023-12-15
# Start	06:00	
# Part1	06:06	6min
# Part2	06:32	26min
# Total	32min
import re
with open('input') as f:
	lista=f.read().strip().split(',')

def hash(word):
	r=0
	for c in word:
		r+=ord(c)
		r*=17
		r%=256
	return r

silver=0
h={i:[] for i in range(256)}
for l in lista:
	# print(f'after {l}:')
	silver+=hash(l)
	s,v=re.split('[-=]',l)
	i=hash(s)
	if v!='':
		if len(h[i])==0:
			h[i].append([s,int(v)])
		else:
			found=None
			for j, lens in enumerate(h[i]):
				if lens[0]==s:
					found=j
					break
			if found!=None:
				h[i][found][1]=int(v)
			else:
				h[i].append([s,int(v)])

	else:
		found=None
		if len(h[i])!=0:
			for j, lens in enumerate(h[i]):
				if lens[0]==s:
					found=j
					break
			if found!=None:
				h[i].pop(found)
	# [print(k,v) for k,v in h.items() if len(v)!=0]
	# print()

gold=0
for k,v in h.items():
	for i,v2 in enumerate(v):
		entry=(k+1)*(i+1)*v2[1]
		gold+=entry

print('Silver:',silver)
print('Gold:', gold)