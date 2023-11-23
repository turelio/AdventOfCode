# 2023-11-23
#Start	11:31
#Part1	12:14	43min
#Part2	12:15	1min
#Total	44min
with open('input') as f:
	lista=f.read().splitlines()


def solve(a,b, lista):
	skip=0
	i=0
	r={'a':a,'b':b}
	while i<len(lista):
		# print(i, lista[i])
		instr=lista[i][:3]
		data=lista[i][4:]

		if instr=='hlf':
			r[data]=r[data]//2
			i+=1
		elif instr=='tpl':
			r[data]*=3
			i+=1
		elif instr=='inc':
			r[data]+=1
			i+=1
		elif instr=='jmp':
			i+=int(data)
		elif instr=='jie':
			if r[data[0]]%2==0:
				i+=int(data[3:])
			else:
				i+=1
	# jio r, offset is like jmp, but only jumps if register r is 1 ("jump if one", not odd).
	# LEARN TO FUCKING READ
		elif instr=='jio':
			if r[data[0]]==1:
				i+=int(data[3:])
			else:
				i+=1
	print(r)
	return r['b']

print('Silver:', solve(0,0,lista))
print('Gold:', solve(1,0,lista))