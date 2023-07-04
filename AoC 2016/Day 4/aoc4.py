# 2022-02-02
#Start	17:57
#Part1	18:44
#Part2	18:51
#Total	54min
import re

with open('input') as f:
	lista=f.read().splitlines()


def encrypt(text,s):
	result = ""
	for i in range(len(text)):
		char = text[i]
		result += chr((ord(char) + s - 97) % 26 + 97)
	return result


test=lista[0]
def check(x):
	result = re.search(r"(.*?)-(\d\d\d)\[(.*)\]", x)
	result=list(result.groups())
	result[0]=result[0].replace('-','')
	counts={}
	# print(type(result[0]))
	for i in result[0]:
		# print(i)
		counts[i]=result[0].count(str(i))
	# counts=[i*j for i, j in counts.items()]
	# print(counts)
	counts=''.join(list(reversed(list(zip(*sorted(counts.items(), key=lambda x: (-x[1], x[0]),reverse=1)))[0][-5:])))
	if result[2]==counts:
		print(result[1],counts, encrypt(result[0], int(result[1])))
		return int(result[1])
	else:
		return 0
check(test)
check('aaaaa-bbb-z-y-x-123[abxyz]')
check('a-b-c-d-e-f-g-h-987[abcde]')
check('not-a-real-room-404[oarel]')
check('totally-real-room-200[decoy]')
silver=0
for i in lista:
	silver+=check(i)

print(silver)
# Gold : zadftbaxq-anvqof-efadmsq-482[afqdb] afqdb  =  afqdb northpoleobjectstorage
