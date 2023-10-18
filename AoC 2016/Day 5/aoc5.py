# 2023-10-17
#Start	15:20
#Part1	15:34	14min
#Part2	15:49	15min
#Total	29min
import hashlib

x='ugkcyxxp'
test='abc'

def silver(door):
	result=[]
	i=0
	while True:
		n=f'{door}{i}'
		n=str(hashlib.md5(n.encode('utf-8')).hexdigest())
		# print(i, n[:5], n[5])
		if n[:5]=='00000':
			if len(result)!=8:
				print(i, n[5])
				result.append(n[5])
			else:
				return ''.join(result)
		i+=1

def gold(door):
	result=[None,None,None,None,None,None,None,None]
	i=0
	while True:
		if not None in result:
			return ''.join(result)
		n=f'{door}{i}'
		n=str(hashlib.md5(n.encode('utf-8')).hexdigest())
		if n[:5]=='00000':
			try:
				j=int(n[5])
			except:
				i+=1
				continue

			if j in range(8):
				if result[j]!=None:
					i+=1
					continue
				result[j]=n[6]
				print(i, n[5], n[6], result)

		i+=1
# print(silver(x))
print(gold(x))