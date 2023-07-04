# Start 8:39
# Part1 8:52
# Part2 9:00
# Total 21min
# 
with open('input') as f:
    lista=f.read().splitlines()

silver=0
for i in lista:
    half=int(len(i)/2)
    result=list(set(i[0:half])&set(i[half:]))[0]
    if result.islower():
        score=ord(result)-96
    else:
        score=ord(result)-38
    silver+=score
print(silver)

gold=0
for i in range(0, len(lista),3):
    result=list(set(lista[i])&set(lista[i+1])&set(lista[i+2]))[0]
    if result.islower():
        score=ord(result)-96
    else:
        score=ord(result)-38
    gold+=score
print(gold)

## First pass
# with open('input') as f:
#     lista=f.read().splitlines()

# silver=0
# for i in lista:
#     half=int(len(i)/2)
#     for x in i[0:half]:
#         for y in i[half:]:
#             if x==y:
#                 result=x
#     if result.islower():
#         score=ord(result)-96
#     else:
#         score=ord(result)-38
#     silver+=score
# print(silver)

# gold=0
# for i in range(0, len(lista),3):
#     for x in lista[i]:
#         for y in lista[i+1]:
#             for z in lista[i+2]:
#                 if x==y==z:
#                     result=x
#     if result.islower():
#         score=ord(result)-96
#     else:
#         score=ord(result)-38
#     gold+=score
# print(gold)