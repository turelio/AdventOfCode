# 2023-10-21
#Start	18:56
#Part1	19:33	37min
#Part2	20:04	31min
#Total	68min
import re
with open('input') as f:
	lista=f.read()

test=lista
test=re.sub(r'!.', '', test)
# replace with length of captured group
test=re.sub(r'<(.*?)>',lambda x:str(len(x.groups()[0])),test)
test=test.replace('{','[').replace('}',']')
test=eval(test)

silver=[1]
gold=[]
def count(n, depth=1):
	for i in n:
		if isinstance(i,list):
			silver.append(depth+1)
			count(i,depth+1)
		else:
			gold.append(int(i))

count(test)
print(sum(silver), sum(gold))


