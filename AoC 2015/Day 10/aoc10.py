#2022-12-26
#Part1	20:23-20:40	(17min)
#Part2	20:40-20:41 (1min)
#Total	18min
import re

lista='1113222113'

def lns(n):
	new=''
	result=re.findall(r'1+|2+|3+', n)
	for r in result:
		new+=str(len(r))
		new+=r[0]
	return new

for i in range(40):
	lista=lns(lista)

print("Silver:",len(lista))
for i in range(10):
	lista=lns(lista)
print("Gold:",len(lista))
