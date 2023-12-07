# 2023-12-07
# Start	06:00	
# Part1	07:41	101min
# Part2	08:15	34min
# Total	135min
import itertools
with open('input') as f:
	lista=f.read().splitlines()
# print(read)
lista=[l.split(' ') for l in lista]
tiers=['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
tiers2=['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
# [5,0,0,0,0] is 5 singles, [2,0,1,0,0] is a triple and 2 singles etc.
figures=[[5,0,0,0,0],[3,1,0,0,0],[1,2,0,0,0],[2,0,1,0,0],[0,1,1,0,0],[1,0,0,1,0],[0,0,0,0,1]]

def solve(tiers, part2=False):
	result=[]
	for i,l in enumerate(lista):
		value_order=[tiers.index(t) for t in l[0]]
		bet=int(l[1])

		# group consecutive and sort by group length
		hand=[list(g) for k, g in itertools.groupby(sorted(l[0]))]
		hand=sorted(hand, key=lambda x:(len(x)),reverse=True)
		
		# remove J group and add its length to the best figure
		if part2:
			for j in range(len(hand)):
				if 'J' in hand[j] and len(hand)!=1:
					to_add=len(hand.pop(j))
					hand=sorted(hand, key=lambda x:(len(x),tiers.index(x[0])),reverse=True)
					hand[0]+=[hand[0][0]]*to_add
					break
		# count multiples in hand and compare to figure strength
		counts=[len(x) for x in hand]
		counts=[counts.count(x) for x in range(1,6)]
		tier=figures.index(counts)
		result.append((tier,value_order,bet))

	result=sorted(result, key=lambda x:(x[0],x[1]))
	win=0
	for i,s in enumerate(result):
		win+=(i+1)*s[2]
	return win

print('Silver:',solve(tiers))
print('Gold:',solve(tiers2,True))