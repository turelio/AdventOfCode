#Start	10:13	20211212	
#Part1	11:39	86min 13:12 break
#Part2	15:35	
#Total	~270min
import copy
with open('input') as f:
	lista=f.read().strip().splitlines()
lista=[l.split('-') for l in lista]

paths={}
for l in lista:
	if not l[0] in paths:
		paths[l[0]]=[l[1]]
	elif not l[1] in paths[l[0]]:
		paths[l[0]].append(l[1])
	if not l[1] in paths:
		paths[l[1]]=[l[0]]
	elif not l[0] in paths[l[1]]:
		paths[l[1]].append(l[0])

routes=[]
routes2=[]
print(paths)
path=copy.deepcopy(paths)

def nextstep(route, path, twice):
	if route[-1]=='end':
		if not route in routes2 and twice:
			routes2.append(route)
		if not route in routes:
			routes.append(route)
			print(len(routes))
			return

	path2=copy.deepcopy(path)

	if route[-1].islower():
		for p in path2:
			if route[-1] in path2[p]:
				path2[p].remove(route[-1])

	for choice in paths[route[-1]]:
		if choice in path2[route[-1]]:
			path3=copy.deepcopy(path2)
			twice2=twice
			route2=route.copy()
			route2.append(choice)
			nextstep(route2, path3, twice2)
		elif not choice in path2[route[-1]] and twice and choice!='start' and choice!='end':
			path3=copy.deepcopy(path2)
			twice2=False
			route3=route.copy()
			route3.append(choice)
			nextstep(route3, path3, twice2)
		elif path2[route[-1]]==[] and twice==False:
		 	#print("dead end")
		 	return

route=['start']
nextstep(route, path, True)
print(len(routes), len(routes2))

# Part 1
# with open('input2') as f:
# 	lista=f.read().strip().splitlines()
# lista=[l.split('-') for l in lista]

# paths={}
# for l in lista:
# 	if not l[0] in paths:
# 		paths[l[0]]=[l[1]]
# 	elif not l[1] in paths[l[0]]:
# 		paths[l[0]].append(l[1])
# 	if not l[1] in paths:
# 		paths[l[1]]=[l[0]]
# 	elif not l[0] in paths[l[1]]:
# 		paths[l[1]].append(l[0])

# routes=[]
# routes2=[]
# print(paths)
# path=copy.deepcopy(paths)

# def nextstep(route, path):
# 	print(f'{route[-1]}')
# 	if route[-1]=='end':
# 		if not route in routes:
# 			routes.append(route)
# 			print('finished\n')
# 			return

# 	path2=copy.deepcopy(path)
# 	if path2[route[-1]]==[]:
# 		print("dead end")
# 		return
# 	if route[-1].islower():
# 		for p in path2:
# 			if route[-1] in path2[p]:
# 				path2[p].remove(route[-1])

# 	for choice in path2[route[-1]]:
# 		route2=route.copy()
# 		route2.append(choice)
# 		nextstep(route2, path2)

# route=['start']
# nextstep(route, path)
# print(len(routes))
