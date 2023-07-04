#Start	12:09
#Part1	13:22
#Part2	13:57
#Total	108min

# Secondd pass, 132ms
with open('input') as f:
	lista=f.read().split('\n\n')

lista[-1]=lista[-1][:-1]

def compare(left, right, nest=0):
	order=0
	# print('\t'*nest, f'Compare {left} vs {right}')
	nest+=1
	for i in range(max([len(left), len(right)])):
		if i>=len(left):
			# print('\t'*(nest+1),f'Left side ran out of items, so inputs are in the right order')
			order=1
		elif i>=len(right):
			# print('\t'*(nest+1),f'Right side ran out of items, so inputs are in the wrong order')
			order=2
		elif isinstance(left[i], int) and isinstance(right[i], int):
			# print('\t'*nest,f'Compare {left[i]} vs {right[i]}')
			if left[i] < right[i]:
				# print('\t'*(nest+1),f'Left side is smaller, so inputs are in the right order')
				order=1
			elif left[i] > right[i]:
				# print('\t'*(nest+1),f'Right side is smaller, so inputs are in the wrong order')
				order=2
		elif isinstance(left[i], list) or isinstance(right[i], list):
			if isinstance(left[i], int):
				order=compare([left[i]], right[i],nest+1)
			elif isinstance(right[i], int):
				order=compare(left[i], [right[i]],nest+1)
			else:
				order=compare(left[i], right[i],nest+1)
		if order>0:
			return order
	return order
silver=[]
gold=[]

for index, l in enumerate(lista):
	left, right=l.split('\n')
	left=eval(left)
	right=eval(right)
	gold.append(left)
	gold.append(right)
	# print(f'Pair {index+1}')
	correct=compare(left, right)
	if correct==1:
		silver.append(index+1)

print('Silver:',sum(silver))

gold.append([[2]])
gold.append([[6]])

sorting=[]
for i1,v1 in enumerate(gold):
	if len(sorting)==0:
		sorting.append(v1)
	else:
		put=0
		for i2,v2 in enumerate(sorting):
			if compare(v1,v2)==1:
				put=True
				sorting.insert(i2, v1)
				break

		if not put:
			sorting.append(v1)

first=sorting.index([[6]])
second=sorting.index([[2]])
# print(first, sorting[first], second, sorting[second])
print('Gold:',(first+1)*(second+1))


# # First pass, 2.6s
# with open('input') as f:
# 	lista=f.read().split('\n\n')

# test='''[1,1,3,1,1]
# [1,1,5,1,1]

# [[1],[2,3,4]]
# [[1],4]

# [9]
# [[8,7,6]]

# [[4,4],4,4]
# [[4,4],4,4,4]

# [7,7,7,7]
# [7,7,7]

# []
# [3]

# [[[]]]
# [[]]

# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]'''
# test=test.split('\n\n')

# lista[-1]=lista[-1][:-1]

# # lista=test

# wrong=set()
# right=set()

# def compare(left, right, nest=0):
# 	order=0
# 	# print('\t'*nest, f'Compare {left} vs {right}')
# 	nest+=1
# 	for i in range(max([len(left), len(right)])):
# 		if i>=len(left):
# 			# print('\t'*(nest+1),f'Left side ran out of items, so inputs are in the right order')
# 			order=1
# 		elif i>=len(right):
# 			# print('\t'*(nest+1),f'Right side ran out of items, so inputs are in the wrong order')
# 			order=2
# 		elif isinstance(left[i], int) and isinstance(right[i], int):
# 			# print('\t'*nest,f'Compare {left[i]} vs {right[i]}')
# 			if left[i] < right[i]:
# 				# print('\t'*(nest+1),f'Left side is smaller, so inputs are in the right order')
# 				order=1
# 			elif left[i] > right[i]:
# 				# print('\t'*(nest+1),f'Right side is smaller, so inputs are in the wrong order')
# 				order=2
# 		elif isinstance(left[i], list) or isinstance(right[i], list):
# 			# print('possible lists: ')
# 			if isinstance(left[i], int):
# 				order=compare([left[i]], right[i],nest+1)
# 			elif isinstance(right[i], int):
# 				order=compare(left[i], [right[i]],nest+1)
# 			else:
# 				order=compare(left[i], right[i],nest+1)
# 		# print(order)
# 		if order>0:
# 			return order
# 	return order
# silver=[]
# gold=[]
# for index, l in enumerate(lista):

# 	left, right=l.split('\n')
# 	left=eval(left)
# 	right=eval(right)
# 	gold.append(left)
# 	gold.append(right)
# 	# print(f'Pair {index+1}')
# 	correct=compare(left, right)
# 	# print(correct)
# 	if correct==1:
# 		silver.append(index+1)
# 	# print('')

# print(sum(silver))

# gold.append([[2]])
# gold.append([[6]])

# print(gold)

# sorting=[]
# for i1,v1 in enumerate(gold):
# 	print(f'taking {v1}')
# 	if len(sorting)==0:
# 		print('\tput first')
# 		sorting.append(v1)
# 	else:
# 		put=0
# 		for i2,v2 in enumerate(sorting):
# 			print(f'\tcompare {v1} with {v2}: {compare(v1,v2)}')
# 			if compare(v1,v2)==1:
# 				put=True
# 				print(f'\tput before {v2}')
# 				sorting.insert(i2, v1)
# 				break

# 		if not put:
# 			print('\tlist finished, put at end')
# 			sorting.append(v1)
# 	print('current list:')
# 	for i in sorting:
# 		print(i)

# first=sorting.index([[6]])
# second=sorting.index([[2]])
# print(first, sorting[first], second, sorting[second])
# print((first+1)*(second+1))