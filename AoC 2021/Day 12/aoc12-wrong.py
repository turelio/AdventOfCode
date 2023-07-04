#Start	10:13	20211212	
#Part1	11:39	86min 13:12 break 1337 compiling
#Part2	
#Total
import time
import random
import copy
with open('input') as f:
	lista=f.read().strip().splitlines()
lista=[l.split('-') for l in lista]

connections={}
for l in lista:
	if not l[0] in connections:
		connections[l[0]]=[l[1]]
	elif not l[1] in connections[l[0]]:
		connections[l[0]].append(l[1])
	if not l[1] in connections:
		connections[l[1]]=[l[0]]
	elif not l[0] in connections[l[1]]:
		connections[l[1]].append(l[0])


connections2=copy.deepcopy(connections)
print(connections2)
for c in connections2:
	if 'start' in connections2[c]:
		connections2[c].remove('start')
print(connections2)


routes=[]
j=1
while True:
	i=1
	route=['start']
	currentc='start'
	connection=copy.deepcopy(connections2)
	connection2=copy.deepcopy(connections2)
	twice=True
	#print(connection)
	while currentc != 'end':
		if currentc.islower():
			for c in connection:
				if currentc in connection[c]:
					connection[c].remove(currentc)

		while True:
			nextc=random.choice(connection2[currentc])
			if nextc in connection[currentc]:
				break
			elif twice:
				twice=False
				break
			elif connection[currentc]==[] and twice==False:
				nextc=0
				break
		if nextc==0:
			break

		currentc=nextc
		
		route.append(currentc)
		i+=1
	if not route in routes and route[-1]=='end':
		routes.append(route)
	print(f"loop {j}", len(routes))

	j+=1

print(len(routes))

ex='''start,A,b,A,b,A,c,A,end
start,A,b,A,b,A,end
start,A,b,A,b,end
start,A,b,A,c,A,b,A,end
start,A,b,A,c,A,b,end
start,A,b,A,c,A,c,A,end
start,A,b,A,c,A,end
start,A,b,A,end
start,A,b,d,b,A,c,A,end
start,A,b,d,b,A,end
start,A,b,d,b,end
start,A,b,end
start,A,c,A,b,A,b,A,end
start,A,c,A,b,A,b,end
start,A,c,A,b,A,c,A,end
start,A,c,A,b,A,end
start,A,c,A,b,d,b,A,end
start,A,c,A,b,d,b,end
start,A,c,A,b,end
start,A,c,A,c,A,b,A,end
start,A,c,A,c,A,b,end
start,A,c,A,c,A,end
start,A,c,A,end
start,A,end
start,b,A,b,A,c,A,end
start,b,A,b,A,end
start,b,A,b,end
start,b,A,c,A,b,A,end
start,b,A,c,A,b,end
start,b,A,c,A,c,A,end
start,b,A,c,A,end
start,b,A,end
start,b,d,b,A,c,A,end
start,b,d,b,A,end
start,b,d,b,end
start,b,end'''
ex=ex.splitlines()
ex=[e.split(',') for e in ex]
print("not found:")
for e in ex:
	if not e in routes:
		print(e)

print('found: ')
for l in routes:
	print(l)