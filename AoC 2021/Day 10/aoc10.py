#Start	11;40	211210	
#Part1	12:16	36min
#Part2	12:30	14min
#Total	50min
with open('input') as f:
	lista=f.read().strip().splitlines()

score_silver={')': 3,']': 57,'}': 1197,'>': 25137}
score_gold={')': 1,']': 2,'}': 3,'>': 4}
chunks=["()", "[]", "<>", "{}"]
silver, gold,=[], []

for n in lista:
	len1, len2= 0,1
	while len1!=len2:
		len1=len(n)
		for c in chunks:
			n=n.replace(c, "")
		len2=len(n)
	n_stripped=n
	for c in chunks:
		n_stripped=n_stripped.replace(c[0],"")
	if len(n_stripped)!=0:
		silver.append(n_stripped[0])
	else:
		n=n[::-1]
		for c in chunks:
			n=n.replace(c[0], c[1])
		score=0
		for i in n:
			score=score*5+score_gold[i]
		gold.append(score)

print(sum([silver.count(s)*score_silver[s] for s in score_silver]))
print(sorted(gold)[len(gold)//2])