#Start	9:22
#Part1	9:40
#Part2	9:58
#Total	36min

# Second pass
with open('input') as f:
	lista=f.read().splitlines()

lista=[l.split() for l in lista]

silver=[]
gold=[]

def check(cycle, x):
	if cycle%40==20:
		silver.append(cycle*x)

def draw_pixel(pos, x):
	if pos%40 in [x-1,x,x+1]:
		gold.append('#')
	else:
		gold.append('.')

cycle=1
x=1
for l in lista:
	if l[0]=='noop':
		check(cycle,x)
		draw_pixel(len(gold), x)
		cycle+=1
	else:
		val=int(l[1])
		check(cycle,x)
		draw_pixel(len(gold), x)
		cycle+=1
		check(cycle,x)
		draw_pixel(len(gold), x)
		cycle+=1
		x+=val

print('silver:',sum(silver))

for k,v in enumerate(gold):
	if k%40==0:
		print('')
		print(v,end='')
	else:
		print(v,end='')
print('')


## First pass, 26ms
# with open('input') as f:
# 	lista=f.read().splitlines()

# lista=[l.split() for l in lista]
# # print(lista)

# test='''addx 15
# addx -11
# addx 6
# addx -3
# addx 5
# addx -1
# addx -8
# addx 13
# addx 4
# noop
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx 5
# addx -1
# addx -35
# addx 1
# addx 24
# addx -19
# addx 1
# addx 16
# addx -11
# noop
# noop
# addx 21
# addx -15
# noop
# noop
# addx -3
# addx 9
# addx 1
# addx -3
# addx 8
# addx 1
# addx 5
# noop
# noop
# noop
# noop
# noop
# addx -36
# noop
# addx 1
# addx 7
# noop
# noop
# noop
# addx 2
# addx 6
# noop
# noop
# noop
# noop
# noop
# addx 1
# noop
# noop
# addx 7
# addx 1
# noop
# addx -13
# addx 13
# addx 7
# noop
# addx 1
# addx -33
# noop
# noop
# noop
# addx 2
# noop
# noop
# noop
# addx 8
# noop
# addx -1
# addx 2
# addx 1
# noop
# addx 17
# addx -9
# addx 1
# addx 1
# addx -3
# addx 11
# noop
# noop
# addx 1
# noop
# addx 1
# noop
# noop
# addx -13
# addx -19
# addx 1
# addx 3
# addx 26
# addx -30
# addx 12
# addx -1
# addx 3
# addx 1
# noop
# noop
# noop
# addx -9
# addx 18
# addx 1
# addx 2
# noop
# noop
# addx 9
# noop
# noop
# noop
# addx -1
# addx 2
# addx -37
# addx 1
# addx 3
# noop
# addx 15
# addx -21
# addx 22
# addx -6
# addx 1
# noop
# addx 2
# addx 1
# noop
# addx -10
# noop
# noop
# addx 20
# addx 1
# addx 2
# addx 2
# addx -6
# addx -11
# noop
# noop
# noop'''
# test=[l.split() for l in test.split('\n')]
# # lista=test
# silver=[]
# def check(cycle, x):
# 	if cycle in [20, 60, 100, 140, 180,220]:
# 		print(f'cycle {cycle} strength: {cycle*x}')
# 		silver.append(cycle*x)

# cycle=1
# x=1
# for l in lista:
# 	if l[0]=='noop':
# 		check(cycle,x)
# 		cycle+=1
# 	else:
# 		val=int(l[1])
# 		check(cycle,x)
# 		cycle+=1
# 		check(cycle,x)
# 		cycle+=1
# 		x+=val

# print(sum(silver))


# gold=[]
# cycle=1
# x=1
# for l in lista:
# 	if l[0]=='noop':
# 		if len(gold)%40 in [x-1,x,x+1]:
# 			gold.append('#')
# 		else:
# 			gold.append('.')
# 		cycle+=1
# 	else:
# 		val=int(l[1])
# 		if len(gold)%40 in [x-1,x,x+1]:
# 			gold.append('#')
# 		else:
# 			gold.append('.')
# 		cycle+=1
# 		if len(gold)%40 in [x-1,x,x+1]:
# 			gold.append('#')
# 		else:
# 			gold.append('.')
# 		cycle+=1
# 		x+=val
# 		print(x)

# # print(gold)
# for k,v in enumerate(gold):
# 	if k%40==0:
# 		print('')
# 		print(v,end='')
# 	else:
# 		print(v,end='')

# print(1, 41%40, )