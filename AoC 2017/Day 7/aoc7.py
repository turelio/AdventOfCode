# 2023-10-17
#Start	20:10
#Part1	20:34	24min
#Part2	21:45	71min
#Total	95min
with open('input') as f:
	lista=f.read().splitlines()

entries={}
for l in lista:
	l=l.split()
	# print(l)
	name=l.pop(0)
	weight=int(l.pop(0)[1:-1])
	if name not in entries:
		entries[name]={'parent':None}
	entries[name]['weight']=weight
	if len(l)>0:
		l.pop(0)
		children=''.join(l)
		children=children.split(',')
		# print(children)
		entries[name]['children']=children
		for c in children:
			if c not in entries:
				entries[c]={}
			entries[c]['parent']=name
	# print()

# Silver
for k,v in entries.items():
	if v['parent']==None:
		print(k,v)
		silver=k

print(k)
print(entries)

def validate(block, indent=0):
	print(indent*'\t',block)
	if 'children' not in entries[block].keys():
		entries[block]['total']=entries[block]['weight']
		return entries[block]['total']
	else:
		elements=[]
		for c in entries[block]['children']:
			elements.append(validate(c, indent+1))
		entries[block]['total']=sum(elements)+entries[block]['weight']
		print(indent*'\t',elements)
		return entries[block]['total']
validate(silver)


def validate2(block, indent=0):
	if 'children' not in entries[block].keys():
		return
	else:
		elements=[[c, entries[c]['total']] for c in entries[block]['children']]
		elements2=[x[1] for x in elements]
		if len(set(elements2))!=1:
			print(f'block {block}: {elements}, entries unbalanced')
		else:
			return
		for e in elements:
			validate2(e[0], indent+1)

validate2(silver)

#deduction, error +6, gold is 305->299
print(entries['fabacam'])