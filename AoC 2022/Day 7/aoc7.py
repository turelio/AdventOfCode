#Start	7:34
# stopped at 10:56, restarted 13:15 (-139min)
#Part1	13:33
#Part2	13:46
#Total	202min+31min=233min

# Second pass, ~30ms
with open('input') as f:
	lista=f.read().splitlines()

directory=['home']
silver={}
for i in lista:
	test=i.split()
	if test[1]=='cd':
		if test[2]=='..':
			if len(directory)>1:
				directory.pop()
		elif test[2]=='/':
			directory==directory[0:1]
		else:
			directory.append(test[2])
	elif test[0] not in ['$', 'dir']:
		for x in range(len(directory), 0, -1):
			if "/".join(directory[:x]) not in silver.keys():
				silver["/".join(directory[:x])]=0
			silver["/".join(directory[:x])]+=int(test[0])

silver2=sum([i for i in silver.values() if i<100000])
print('Silver:\t',silver2)

gold=dict(sorted(silver.items(), key=lambda x: x[1]))
for v in gold.values():
	if v>=30000000-(70000000-silver['home']):
		print('Gold:\t', v)
		break		


## First pass, ~600ms
# import re
# import copy
# with open('input') as f:
# 	lista=f.read().splitlines()

# lista2='''$ cd /
# $ ls
# dir a
# 14848514 b.txt
# 8504156 c.dat
# dir d
# $ cd a
# $ ls
# dir e
# 29116 f
# 2557 g
# 62596 h.lst
# $ cd e
# $ ls
# 584 i
# $ cd ..
# $ cd ..
# $ cd d
# $ ls
# 4060174 j
# 8033020 d.log
# 5626152 d.ext
# 7214296 k'''

# lista2=lista2.split('\n')

# testdir2={'/':{}}
# testdir=['/','a','b']
# def insert(value, name, tree, directory):
# 	# print(f'now at {directory}')
# 	directory=copy.deepcopy(directory)
# 	if len(directory)==1:
# 		if directory[0]=='home':
# 			tree[directory[0]][name]=value
# 			return copy.deepcopy(tree)
# 		else:
# 			print('')
# 			# tree[current][directory[0]][name]=value
# 	else:
# 		print(len(directory))
# 		current=directory.pop(0)
# 		# if directory[0] not in tree[current].keys():
# 		# 	# print(f'{directory[0]} not in {tree[current]}')
# 		# 	tree[current][directory[0]]={}
# 		if len(directory)>1:
# 			insert(value, name, tree[current], directory)
# 		else:
# 			tree[current][directory[0]][name]=value
# 		return copy.deepcopy(tree)
# # testdir2=insert(1, 'aa', testdir2, testdir)
# # print(testdir2)
# # testdir2=insert(dict(), 'gv', testdir2, ['/','g','c'])
# # print(insert(2, 'ab', testdir2, ['/','a','c']))

# directory3={}
# test=lista
# # for l in lista:
# # 	print(l)
# print(len(lista))
# directory2={'home':{}}
# directory=['home']
# silver={}
# for i in test:
# 	print(i)
# 	print('# ', end='')
# 	if re.search(r'cd (.*)', i):
# 		result=re.search(r'\$ cd (.*)', i)
# 		if result[1]=='..':
# 			if len(directory)>1:
# 				print(directory)
# 				directory.pop()
# 				print(directory)
# 			print(f'moving 1 up to {"/".join(directory)}')
# 		elif result[1]=='/':
# 			directory==directory[0:1]
# 		else:
# 			directory.append(result[1])
# 		print(f'changed directory to {"/".join(directory)}')
# 	elif i=='$ ls':
# 		print(f'listed directory {"/".join(directory)}')

# 	else: 
# 		if re.search(r'(\d+) (.*)', i):
# 			result=re.search(r'(\d+) (.*)', i)
# 			print(f'file at {"/".join(directory)}, adding:')
# 			for x in range(len(directory), 0, -1):
# 				print('\t',"/".join(directory[:x]))
# 				if "/".join(directory[:x]) not in silver.keys():
# 					silver["/".join(directory[:x])]=0
# 				silver["/".join(directory[:x])]+=int(result[1])
# 			directory2=insert(result[1],result[2],directory2,directory)
# 		else:
# 			result=re.search(r'dir (\w+)', i)
# 			print('directory, adding:')
# 			directory2=insert(dict(),result[1],directory2,directory)

# 	# print(''.join(directory))

# print(directory2)
# silver2=0
# for k,v in silver.items():
# 	if v<100000:
# 		silver2+=v
# print(silver['home'])
# print(silver2)

# occupied=46090134
# free=70000000-occupied
# print(occupied, free, 30000000-free)
# gold=dict(sorted(silver.items(), key=lambda x: x[1]))
# print(gold)
# for k,v in gold.items():
# 	print(v,'\t', k)
# 	if v>=30000000-free:
# 		break		
