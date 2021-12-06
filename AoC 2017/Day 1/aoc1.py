
#Start	15:10 211206
#Part1	15:20 10min
#Part2	15:42 22min
#Total	32min
with open('input') as f:
	lista=f.read().strip()
#1
total=0
for c,v in enumerate(lista):
	c2=c+1 if c<len(lista)-1 else 0 
	if lista[c]==lista[c2]:
		#print(f"{lista[c]}={lista[c2]}")
		total+=int(v)
print(total)


#2
total=0
for c,v in enumerate(lista):
	half=int(len(lista)/2)
	c2=c+half if c<half else c-half 
	if lista[c]==lista[c2]:
		#print(f"{lista[c]}={lista[c2]}")
		total+=int(v)
print(total)