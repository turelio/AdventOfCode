# 2023-10-18
#Start	12:50
#Part1	13:40	50min
#Part2	13:50 	10min
#Total	60min
import re
with open('input') as f:
	lista=f.read().splitlines()

def decode2(n):
	rows=n[:7]
	cols=n[7:]
	rows=rows.replace('B','1').replace('F','0')
	cols=cols.replace('R','1').replace('L','0')
	rows=int(rows,2)
	cols=int(cols,2)
	ticket=rows*8+cols
	# print(n,' = ', rows,cols,ticket)
	return ticket

gold=[]
for l in lista:
	entry=decode2(l)
	gold.append(entry)

print('Silver: ', max(gold))
for i in range(85,891):
	if i not in gold:
		print('Gold: ',i)
