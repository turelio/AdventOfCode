# 2023-11-29
#Start	13:23
#Part1	13:40	17min
#Part2	13:45	5min
#Total	22min

lista=[9,19,1,6,0,5,4]
lista=[0,3,6]
lista=[2,3,1]
lista=[9,19,1,6,0,5,4]
spoken={v:[i+1, None] for i,v in enumerate(lista)}
print(spoken)

i=len(lista)+1
last=lista[-1]
while i!=30000001:
	if i%100000==0:
		print(f'Round {i}')
	# print(f'\tconsider {last}')
	if spoken[last][1]==None:
		# print('\tFirst time, shout 0')
		shout=0
	else:
		shout=spoken[last][0]-spoken[last][1]
		# print(f'\tRepeat, last time {shout} rounds before')
	if shout not in spoken:
		spoken[shout]=[i,None]
	else:
		spoken[shout]=[i,spoken[shout][0]]
	last=shout
	# print('shouted',last)
	i+=1

print(last)