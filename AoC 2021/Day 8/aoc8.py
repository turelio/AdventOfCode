#Start	10:57 20211208
#Part1	11:13 16min
#Part2	13:33 130min
#Total	146min
with open('input') as f:
	lista=f.read().splitlines()
lista=[[k.split(' ') for k in l.split(' | ')] for l in lista]
unique=[2,3,4,7]
chars=["a","b","c","d","e","f","g"]
cipher_values={"abcefg":0, "cf":1, "acdeg":2, "acdfg":3, "bcdf":4, "abdfg":5, "abdefg":6, "acf":7, "abcdefg":8, "abcdfg":9}

# 1. find potential cipher values, put into cand{}
# 2. find all sure cipher values
# 3. decipher second part and find score
def find_cipher(test):
	cand={"a":[], "b":[], "c":[], "d":[], "e":[], "f":[], "g":[]}
	sure={"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0 }
	diff6=[]
	# candidates for b,c,d,f
	for t in test[0]:
		if len(t)==2:
			for i in range(2):
				cand["c"].append(t[i])
				cand["f"].append(t[i])
		elif len(t)==4:
			for i in range(4):
				cand["b"].append(t[i])
				cand["d"].append(t[i])
		elif len(t)==3:			
			for i in range(3):
				cand["a"].append(t[i])
	
		elif len(t)==6:
			diff6.append(t)

	#remove false candidates
	cand["b"]=[c for c in cand["b"] if not c in cand["c"]]
	cand["d"]=cand["b"].copy()

	# find characters that don't repeat in 6char long words  (it's always c, d and e)
	poss_cde=[]
	for c in chars:
		if not all([c in d for d in diff6]):
			poss_cde.append(c)
	# find a
	for i in cand["a"]:
		if not i in cand["c"]: 
			sure["a"]=i
	# find c, d and e
	for i in poss_cde:
		if i in cand["c"]:
			sure["c"]=i
		elif i in cand["d"]:
			sure["d"]=i
		else:
			sure['e']=i
	# find f
	for i in cand["f"]:
		if i != sure["c"]:
			sure["f"]=i
	# find b
	for i in cand["b"]:
		if i != sure["d"]:
			sure["b"]=i
	# find g
	for i in chars:
		if not i in sure.values():
			sure["g"]=i
	# invert dictionary
	sure = dict(zip(sure.values(), sure.keys()))

	# decipher second part
	deciphered_list=[]
	for t1 in test[1]:
		word=[]
		for i in range(len(t1)):
			word.append(sure[t1[i]])
		deciphered_list.append(''.join(word))
	deciphered_list=[''.join(sorted(n)) for n in deciphered_list]
	
	# calculate score
	score=[]
	for n in deciphered_list:
		score.append(str(cipher_values[n]))
	score=''.join(score)
	return int(score)


# Part 1
silver=0
for c1,v1 in enumerate(lista):
	for c2,v2 in enumerate(v1[1]):
		if len(lista[c1][1][c2]) in unique:
			silver+=1

# Part 2
gold=0
for l in lista:
	gold+=find_cipher(l)

print(silver, gold)
