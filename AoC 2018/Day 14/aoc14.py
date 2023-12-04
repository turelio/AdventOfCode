# 2023-12-03
#Start	16:18
#Part1	16:36	18min
#Part2	16:57	21min
#Total	39min
# Pretty slow, 8s
n=598701
scores=[3,7]
e1,e2=0,1

n2=[int(l) for l in list(str(n))]
found=False
while True:
	if len(scores)%100000==0:
		print(len(scores))
	entry=scores[e1]+scores[e2]
	if entry>=10:
		entry=[entry//10,entry%10]
	else:
		entry=[entry]
	for e in entry:
		scores.append(e)
		if len(scores)>20000000:
			if scores[-1*len(n2):]==n2:
				print('Gold: ',len(scores)-len(n2))
				found=True
				break
	if found:
		break
	e1=(e1+(scores[e1]+1))%(len(scores))
	e2=(e2+(scores[e2]+1))%(len(scores))

print('Silver:',''.join(map(str,scores[n:n+10])))
