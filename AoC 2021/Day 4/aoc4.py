#now it's wrong
with open('input') as f:
	bingo=f.read().split('\n\n')

order=list(map(int, bingo.pop(0).split(',')))
bingo=[list(map(int, b.replace('\n', ' ').strip().split())) for b in bingo]
bingo_check=[[0 for col in range(25)] for row in range(100)]
winner_list=[]
score_list=[]

def score(n, number, bingo_check):
	suma=0
	for c, v in enumerate(bingo_check[n]):
		if v==0:
			suma+=bingo[n][c]
	return suma*number


def check_winner(bingo, number):
	win_cond=[[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24],[0,5,10,15,20],[1,6,11,16,21],[2,7,12,17,22],[3,8,13,18,23],[4,9,14,19,24]]
	for c, v in enumerate(bingo):
		for w in win_cond:
			if all([v[w[i]]==1 for i in range(5)]):			
				if not c in winner_list:
					winner_list.append(c)
					score_list.append(score(c, number, bingo_check))
					#print(f"bingo {c} wins") 

for number in order:
	for c1,v1 in enumerate(bingo):
		for c2,v2 in enumerate(v1):
			if v2==number:
				bingo_check[c1][c2]=1
	check_winner(bingo_check,number)

silver=score_list[0]
gold=score_list[-1]
print(silver,gold)


# OLD
#print(score(winner_list[0], bingo_check), score(winner_list[-1], bingo_check))
# for o in order:
# 	#o=int(o)
# 	print(f"looking for {o}:\n")
# 	for count1, value1 in enumerate(bingo_list):
# 		for count2, value2 in enumerate(value1):
# 			#print(type(value2))
# 			if value2==o:
# 				#print(f"found {bingo_list[count1][count2]} in bingo {count1}")
# 				bingo_check[count1][count2]=1
# 	check_winner(o)
# 	if check_winner(o)==1:
# 		break




# bingo_list=[]
# for b in bingo:

# 	b=b.replace('\n', ' ')
# 	b=b.strip()
# 	b=re.split(r'\s+',b)
# 	bingo_list.append(b)
# # print(bingo_list)

# print("Part 1\n#############################")
# bingo_check=[[0 for col in range(25)] for row in range(100)]

# def score(number, bingo_id):
# 	suma=0
# 	for count, value in enumerate(bingo_check[bingo_id]):
# 		if value==0:
# 			suma+=int(bingo_list[bingo_id][count])
# 	return suma*int(number)

# def check_winner(n):
# 	n=int(n)
# 	win_cond=[[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24],[0,5,10,15,20],[1,6,11,16,21],[2,7,12,17,22],[3,8,13,18,23],[4,9,14,19,24]]
# 	for c, b in enumerate(bingo_check):
# 		for w in win_cond:
# 			if (b[w[0]]==1 and b[w[1]]==1 and b[w[2]]==1 and b[w[3]]==1 and b[w[4]]==1):
# 				print(f"bingo {c} wins")
# 				print(score(n, c))
# 				return 1
# 	print("no winner yet")
# 	return 0

# for o in order:
# 	#o=int(o)
# 	print(f"looking for {o}:\n")
# 	for count1, value1 in enumerate(bingo_list):
# 		for count2, value2 in enumerate(value1):
# 			#print(type(value2))
# 			if value2==o:
# 				#print(f"found {bingo_list[count1][count2]} in bingo {count1}")
# 				bingo_check[count1][count2]=1
# 	check_winner(o)
# 	if check_winner(o)==1:
# 		break

# print("Part 2\n#############################")
# bingo_check=[[0 for col in range(25)] for row in range(100)]

# bingo_winners=[0 for x in range(100)]

# def check_winner2(n):
# 	n=int(n)
# 	win_cond=[[0,1,2,3,4],[5,6,7,8,9],[10,11,12,13,14],[15,16,17,18,19],[20,21,22,23,24],[0,5,10,15,20],[1,6,11,16,21],[2,7,12,17,22],[3,8,13,18,23],[4,9,14,19,24]]
# 	for c, b in enumerate(bingo_check):
# 		if bingo_winners[c]==1:
# 			continue
# 		for w in win_cond:
# 			if (b[w[0]]==1 and b[w[1]]==1 and b[w[2]]==1 and b[w[3]]==1 and b[w[4]]==1):
# 				print(f"bingo {c} wins")
# 				#print(score(n, c))
# 				bingo_winners[c]=1
# 				if bingo_winners.count(1)==99:
# 					print(f"{bingo_winners.count(0)} winners, {bingo_winners.count(1)} last")
# 					print(bingo_winners)
# 					print(bingo_winners.index(0))
# 				## i know it's this from the imputs
# 				print(score(56, 45))




# for o in order:
# 	#o=int(o)
# 	print(f"looking for {o}:\n")
# 	for count1, value1 in enumerate(bingo_list):
# 		for count2, value2 in enumerate(value1):
# 			#print(type(value2))
# 			if value2==o:
# 				#print(f"found {bingo_list[count1][count2]} in bingo {count1}")
# 				bingo_check[count1][count2]=1
# 	check_winner2(o)


