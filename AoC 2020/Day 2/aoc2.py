with open('input') as f:
    lista0=f.read().splitlines()

lista=[]
for l in lista0:
    lista.append(l.split(' '))

counter1, counter2=0,0
for l in lista:

    p_min=int(l[0].split('-')[0])
    p_max=int(l[0].split('-')[1])
    p_key=l[1][0]
    p_pass=l[2]
    print(p_min, p_max, p_key, p_pass)
    if (p_max >= p_pass.count(p_key) >= p_min):
        counter1+=1
        print('valid')
    # pattern match and XOR gate
    if ((p_pass[p_min-1]==p_key or p_pass[p_max-1]==p_key) and (p_pass[p_min-1] != p_pass[p_max-1])):
        counter2+=1
print(counter1, counter2)

# first try, 2020
# j=0
# count1=0
# count2=0
# for i in list:
#     list[j]=i.split(" ")
#     list[j][1]=list[j][1][:-1]
#     list[j][0]=list[j][0].split('-')
#     if list[j][2].count(list[j][1])>=int(list[j][0][0]) and list[j][2].count(list[j][1])<=int(list[j][0][1]):
#         count1+=1
#     char1=str(list[j][2])[int(list[j][0][0])-1]==list[j][1]
#     char2=str(list[j][2])[int(list[j][0][1])-1]==list[j][1]
#     if ((char1 and not char2) or (not char1 and char2)):
#         count2+=1
#     j+=1

# print(count1+"\n"+count2)
