#Start	12:06	20121218
#Part1	12:20 	14min
#Part2	12:31	11min
#Total	25min
with open('input') as f:
	lista=f.read()

lista=lista.split(',')
lista=[int(l) for l in lista]
code=lista.copy()


def intcomp(ex,noun,verb):
	ex=code.copy()
	ex[1]=noun
	ex[2]=verb
	i=0
	while ex[i]!=99:
		if ex[i]==1:
			ex[ex[i+3]]=ex[ex[i+1]]+ex[ex[i+2]]
		elif ex[i]==2:
			ex[ex[i+3]]=ex[ex[i+1]]*ex[ex[i+2]]
		i+=4
	return ex[0]

for i in range(100):
	for j in range(100):
		if intcomp(code,i,j)==19690720:
			print(i*100+j)
#intcomp(code,12,2)