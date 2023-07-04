# 8:37
# 8:51
# 8:59
# 22min

# Third pass
with open('input') as f:
    lista=f.read().splitlines()
win={'A X':(4,3),'A Y':(8,4),'A Z':(3,8), 
     'B X':(1,1),'B Y':(5,5),'B Z':(9,9),
     'C X':(7,2),'C Y':(2,6),'C Z':(6,7)}
     
silver, gold = 0,0
for i in lista:
    silver+=win[i][0]
    gold+=win[i][1]

print(silver, gold)

## Second pass
# hand={'X':'R','Y':'P','Z':'S','A':'R','B':'P','C':'S'}
# code={'X':{'A':'Z','B':'X','C':'Y'}, 'Y':{'A':'X','B':'Y','C':'Z'}, 'Z':{'A':'Y','B':'Z','C':'X'}}
# win={'R':{'P':8,'R':4,'S':3},'P':{'P':5,'R':1,'S':9},'S':{'P':2,'R':7,'S':6}}

# lista=[(hand[i[0]],hand[i[2]],hand[code[i[2]][i[0]]]) for i in lista]

# silver, gold = 0,0
# for i in lista:
#     silver+=win[i[0]][i[1]]
#     gold+=win[i[0]][i[2]]

# print(silver, gold)

## Initial code
# with open('input') as f:
#     lista=f.read().splitlines()
# lista=[(i[0],i[2]) for i in lista]

# score={'X':1,'Y':2,'Z':3}
# hand={'X':'Rock','Y':'Paper','Z':'Scissors','A':'Rock','B':'Paper','C':'Scissors'}

# print(lista)

# code={'X':{'A':'Z','B':'X','C':'Y'}, 'Y':{'A':'X','B':'Y','C':'Z'}, 'Z':{'A':'Y','B':'Z','C':'X'}}

# hand_points, win_points=0,0
# for i in lista:
#     if i[0]=='A':
#         if i[1]=='X':
#             hand_points+=1
#             win_points+=3
#         elif i[1]=='Y':
#             hand_points+=2
#             win_points+=6
#         else:
#             hand_points+=3
#             win_points+=0
#     elif i[0]=='B':
#         if i[1]=='X':
#             hand_points+=1
#             win_points+=0
#         elif i[1]=='Y':
#             hand_points+=2
#             win_points+=3
#         else:
#             hand_points+=3
#             win_points+=6
#     else:
#         if i[1]=='X':
#             hand_points+=1
#             win_points+=6
#         elif i[1]=='Y':
#             hand_points+=2
#             win_points+=0
#         else:
#             hand_points+=3
#             win_points+=3

# print(hand_points+win_points)

# hand_points, win_points=0,0
# for i in lista:
#     player=i[1]
#     player=code[i[1]][i[0]]
#     if i[0]=='A':
#         if player=='X':
#             hand_points+=1
#             win_points+=3
#         elif player=='Y':
#             hand_points+=2
#             win_points+=6
#         else:
#             hand_points+=3
#             win_points+=0
#     elif i[0]=='B':
#         if player=='X':
#             hand_points+=1
#             win_points+=0
#         elif player=='Y':
#             hand_points+=2
#             win_points+=3
#         else:
#             hand_points+=3
#             win_points+=6
#     else:
#         if player=='X':
#             hand_points+=1
#             win_points+=6
#         elif player=='Y':
#             hand_points+=2
#             win_points+=0
#         else:
#             hand_points+=3
#             win_points+=3
# print(hand_points+win_points)
