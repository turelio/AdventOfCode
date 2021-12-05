with open('input') as f:
	lista=f.read().splitlines()

# PART 1
#print(lista)
	for i in lista:
		for j in lista:
			if int(i)+int(j)==2020:
				print(f"{i}+{j}={int(i)+int(j)}, answer is {int(i)*int(j)}")

# PART 2
	for i in lista:
		for j in lista:
			for k in lista:
				if int(i)+int(j)+int(k)==2020:
					print(f"{i}+{j}+{k}={int(i)+int(j)+int(k)}, answer is {int(i)*int(j)*int(k)}")
