# 2023-10-17
#Start	16:40
#Part1	17:00	20min
#Part2	17:10	10min
#Total	30min
import re

with open('input') as f:
	lista=f.read().splitlines()


def abba(s):
	for i in range(len(s)-3):
		x=s[i:i+4]
		if x[0]==x[-1] and x[1]==x[2] and x[0]!=x[1]:
			return True
	return False

def aba(s,reverse=False):
	result=[]
	for i in range(len(s)-2):
		x=s[i:i+3]
		if x[0]==x[-1] and x[0]!=x[1]:
			if reverse:
				result.append(x[1]+x[:2])
			else:
				result.append(x)
	return result


silver=0
gold=0
for l in lista:
	outside=re.split(r'\[.*?\]',l)
	inside=re.findall(r'\[(.*?)\]',l)
	silver1=[abba(x) for x in outside]
	silver2=[abba(x) for x in inside]

	gold1,gold2=[],[]
	for x in outside:
		gold1+=aba(x)

	for x in inside:
		gold2+=aba(x,True)

	if set(gold1)&set(gold2):
		gold+=1

	if any(silver1) == True and any(silver2)==False:
		silver+=1

print(silver, gold)