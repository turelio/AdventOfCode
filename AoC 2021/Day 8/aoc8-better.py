# 211208
# Got the idea from anon on /g/
with open('input') as f:
	lista=f.read().splitlines()
lista=[[k.split(' ') for k in l.split(' | ')] for l in lista]
chars=["a","b","c","d","e","f","g"]
unique=[2,3,4,7]
# got cipher_values by comparing occurences with example answer
cipher_values={"49":8,"37":5,"34":2,"39":3,"25":7,"45":9,"41":6,"30":4,"42":0,"17":1}
gold, silver=0, 0
for l in lista:
	for j in l[1]:
		if len(j) in unique:
			silver+=1

	occurences={}
	for c in chars:
		occurences[c]=''.join(l[0]).count(c)
	score=[cipher_values[str(sum(list(map(lambda n: occurences[n], list(i)))))] for i in l[1]]
	score=list(map(str, score))
	score=int(''.join(score))
	gold+=score
print(silver, gold)