# 2023-10-18
#Start	10:11
#Part1	10:35	24min
#Part2	11:10	35min
#Total	59min
# inefficient bruteforce
with open('input') as f:
	lista=f.read().splitlines()

lista=[l.split(', ') for l in lista]
lista=[[int(l[0]), int(l[1])] for l in lista]

# lista=[[1, 1],[1, 6],[8, 3],[3, 4],[5, 5],[8, 9]]
print(lista)

def closest(y,x, lista):
	distances=[]
	for x2,y2 in lista:
		distance=(abs(x-x2)+abs(y-y2))
		distances.append(distance)
	return distances.index(min(distances))

# print(closest(5,4,lista))
# size=10
# while size<=1000:
# 	print('size ',size)
# 	results=[[l,0] for l in range(len(lista))]
# 	for y in range(-1*size, size):
# 		for x in range(-1*size, size):
# 			results[closest(y,x,lista)][1]+=1
# 	results=sorted(results, key=lambda x:x[1])
# 	print(results)
# 	size*=10

# Silver: 3882, deduced from infinite loop at size 1000

lista2=list(zip(*lista))
lista2=[sum(l)//len(l) for l in lista2]
print(lista2)


size=500
print('size ',size)
gold=0
for y in range(size):
	for x in range(size):
		result=0
		for x2,y2 in lista:
			distance=(abs(x-x2)+abs(y-y2))
			# print(f'\tfrom {x},{y} to {x2},{y2} is {distance}')
			result+=distance
		print(y, result)
		if result<10000:
			print('#####################################################')
			gold+=1
print(gold)
size*=10