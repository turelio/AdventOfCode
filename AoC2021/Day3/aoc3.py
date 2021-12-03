with open('input') as f:
    lista=f.read().splitlines()

# Part 1
gamma, epsilon, j=[],[], 0
while j<12:
	counter=0
	for i in lista:
		if i[j]=='0':
			counter+=1
	if counter>500:
		gamma.append('0')
		epsilon.append('1')
	else:
		gamma.append('1')
		epsilon.append('0')
	j+=1

gamma=int(''.join(gamma), 2)
epsilon=int(''.join(epsilon), 2)
print(f"gamma rating = {gamma}, epsilon rate = {epsilon}, power consumption = {gamma*epsilon}")

# Part 2
print('\ncalculating oxygen rating:')
lista2=lista.copy()
j=0
while len(lista2)>1:
	lista_1=[]
	lista_0=[]
	print(len(lista2))
	counter_0=0
	counter_1=0
	for i in lista2:
		if i[j]=='0':
			counter_0+=1
			lista_0.append(i)
		else:
			counter_1+=1
			lista_1.append(i)
	if counter_0>counter_1:
		lista2=lista_0
	else:
		lista2=lista_1
	#print(lista2)
	j+=1
oxygen=int(lista2[0],2)
print (f"{lista2} -> {oxygen}")

print("\ncalculating scrubber rating:")
lista2=lista.copy()
j=0
while len(lista2)>1:
	lista_1=[]
	lista_0=[]
	print(f"{len(lista2)} lines")
	counter_0=0
	counter_1=0
	for i in lista2:
		if i[j]=='0':
			counter_0+=1
			lista_0.append(i)
		else:
			counter_1+=1
			lista_1.append(i)
	
	if counter_0>counter_1:
		lista2=lista_1
	else:
		lista2=lista_0
	j+=1

scrubber=int(lista2[0],2)
print (f"{lista2} -> {scrubber}")

print(f"\noxygen generator rating = {oxygen}, scrubber generator rating = {scrubber}, life support rating = {oxygen*scrubber}")
