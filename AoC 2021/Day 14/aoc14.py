#Start	9:52	20211214	
#Part1	10:53	61min
#Part2	11:47	54min
#Total	115min
import copy
with open('input') as f:
	lista=f.read().split('\n\n')
template=lista[0]
rules=lista[1].splitlines()
rules=[r.split(' -> ') for r in rules]
print(rules, template)
template2=template

def insertpoly(template):
	newtemplate=[]
	while template:
		newtemplate.append(template[:2])
		template=template[1:]
	#print(newtemplate)
	for c,t in enumerate(newtemplate):
		if len(t)==1:
			break
		for r in rules:
			if t==r[0]:
				#print(f"replace {t} with {t[0]}{r[1]}")
				newtemplate[c]=f"{t[0]}{r[1]}"
				#print(newtemplate)
				break
		# if replaced==False:
		# 	newtemplate[c]=newtemplate[c][:-1]


	return ''.join(newtemplate)

for i in range(10):
	#print(f"{i}")
	template=insertpoly(template)

print(len(template))
characters=list(set(template))
print(characters)
silver=[]
for c in characters:
	silver.append(template.count(c))

print(max(silver)-min(silver))

def doublecounts(template):
	counts={}
	print(template)
	charcounts={}
	for r in rules:
		if r[0] in template:
			counts[r[0]]=template.count(r[0])
		charcounts[r[1]]=0	
	characters=list(set(template))
	print(characters)
	for c in characters:
		charcounts[c]=template.count(c)

	return [charcounts, counts]

def expand2(counts):
	charcounts=counts[0]
	counts=counts[1]
	newcounts=copy.deepcopy(counts)
	for c in counts:
		if counts[c]==0:
			continue
		for r in rules:
			if r[0]==c:
				charcounts[r[1]]+=counts[c]
				newcounts[c]-=counts[c]
				try:
					newcounts[f"{c[0]}{r[1]}"]+=counts[c]
				except:
					newcounts[f"{c[0]}{r[1]}"]=counts[c]
				try:
					newcounts[f"{r[1]}{c[1]}"]+=counts[c]
				except:
					newcounts[f"{r[1]}{c[1]}"]=counts[c] 
				break

	return charcounts, newcounts
			


counts=doublecounts(template2)
#print(counts)
for i in range(40):
	#print(f"{i}: {counts}")
	counts=expand2(counts)
	#print('')

print(counts)
print(max(counts[0].values())-min(counts[0].values()))