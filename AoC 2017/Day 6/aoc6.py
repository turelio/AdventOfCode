#2023-10-17
#Start	19:46	
#Part1	20:07	21min
#Part2	20:08	1min
#Total	22min
x = [0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11]
# x = [0,2,7,0]
configurations=[]
configurations.append(str(x))
while True:
	highest=max(x)
	pos=x.index(highest)
	x[pos]=0
	i=(pos+1)%len(x)
	while highest>0:
		x[i]+=1
		highest-=1
		i=(i+1)%len(x)
	if str(x) not in configurations:
		configurations.append(str(x))
	else:

		print(len(configurations))
		print(len(configurations)-configurations.index(str(x)))
		break



