# 2023-11-29
# Start	20:57
# Part1	21:41	44min
# Part2	X
# Total
import re
with open('input') as f:
	lista=f.read().splitlines()

# print(lista)
test='1 + ( 2 * 3) + (4 * (5 + 6) )'
test='((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
test=test.replace(' ','')
test=list(test)

def solve(s, i=0):
	result=0
	sign='+'
	# print('################## START PAR ##############')
	while i<len(s):
		# print(s[i:])
		entry=s[i]
		# print(f'\ti={i}, value={entry}')
		if entry in ['+','*']:
			# print('\tchanged sign to',entry)
			sign=entry
			i+=1
		elif entry=='(':
			base,i2=solve(s,i+1)
			# print(f'\t parentheses result = {base}')
			if sign=='+':
				result+=base
			else:
				result*=base
			i=i2+1
		elif entry==')':
			# print('############# END PAR ##############')
			return result,i 
		else:
			base=int(entry)
			if sign=='+':
				result+=base
				# print('\tadded', entry)
			else:
				result*=base
				# print('\tmultiplied by', entry)
			i+=1
		# print(f'\tTotal = {result}')
	return i, result

solve(test)

silver=0
for test in lista:
	# print(test)
	test=test.replace(' ','')
	test=list(test)
	i,result=solve(test)
	silver+=result

print(silver)

## wrong order
# test='1 + ( 2 * 3) + (4 * (5 + 6) )'
# test='2 * 3 + (4 * 5)'
# test=test.replace(' ','')
# test=list(test)
# def solve2(s):
# 	signs=['+','*','(',')']
# 	while len(s)!=1:
# 		# do all additions
# 		print('ADDITIONS')
# 		while True:
# 			l_old=len(s)
# 			for i in range(l_old-2):
# 				entry=s[i:i+3]
# 				if entry[1]=='+' and entry[0] not in signs and entry[2] not in signs:
# 					entry2=int(entry[0])+int(entry[2])
# 					print('\tto shorten',entry)
# 					s=s[:i]+[entry2]+s[i+3:]
# 					print('\t',s)
# 					break
# 			if len(s)==l_old:
# 				print('no more additions')
# 				break
# 		print()
# 		# do all multiplications
# 		print('MULTIPLICATIONS')
# 		while True:
# 			l_old=len(s)
# 			for i in range(l_old-2):
# 				entry=s[i:i+3]
# 				if entry[1]=='*' and entry[0] not in signs and entry[2] not in signs:
# 					entry2=int(entry[0])*int(entry[2])
# 					print('\tto shorten',entry)
# 					s=s[:i]+[entry2]+s[i+3:]
# 					print('\t',s)
# 					break
# 			if len(s)==l_old:
# 				print('no more mults')
# 				break
# 		print()
# 		# erase single item parentheses
# 		print('PARENTHESES')
# 		while True:
# 			l_old=len(s)
# 			for i in range(l_old-2):
# 				entry=s[i:i+3]
# 				if entry[1] not in signs and entry[0]=='(' and entry[2]==')':
# 					entry2=int(entry[1])
# 					print('\tto shorten',entry)
# 					s=s[:i]+[entry2]+s[i+3:]
# 					print('\t',s)
# 					break
# 			if len(s)==l_old:
# 				print('no more parentheses')
# 				break
# 		print()
# 	print(s)
# solve2(test)