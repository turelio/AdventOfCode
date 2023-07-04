#Start	11;40	211210	
#Part1	12:16	36min
#Part2	12:30	14min
#Total	50min
with open('input') as f:
	lista=f.read().strip().splitlines()

scoreboard={
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}
chunks=["()", "[]", "<>", "{}"]
chunks_open=["(", "[", "<", "{"]

def check_chunk1(n):
	len1, len2= 0,1
	while len1!=len2:
		len1=len(n)
		for c in chunks:
			n=n.replace(c, "")
		len2=len(n)
	n_converted=n
	for c in chunks_open:
		n=n.replace(c,"")
	if len(n)==0:
		return 0
	else:
		return n[0]

def check_chunk2(n):
	len1, len2= 0,1
	while len1!=len2:
		len1=len(n)
		n=n.replace("()", "")
		n=n.replace("[]", "")
		n=n.replace("<>", "")
		n=n.replace("{}", "")
		len2=len(n)
	n2=n[::-1]
	n2=n2.replace("(", ")")
	n2=n2.replace("{", "}")
	n2=n2.replace("<", ">")
	n2=n2.replace("[", "]")
	score=0
	for i in n2:
		score=score*5
		score+=scoreboard[i]
	return score

silver, lista2=[], []
for i in lista:
	silver.append(check_chunk1(i))
	if check_chunk1(i)==0:
		lista2.append(i)
print(silver.count(")")*3+silver.count("]")*57+silver.count("}")*1197+silver.count(">")*25137)

gold=[]
for j in lista2:
	gold.append(check_chunk2(j))
print(sorted(gold)[22])