# 2022-12-02
#Start	10:39
#Part1	10:53
#Part2	11:00
#Total	21min
import hashlib
lista='yzbqklnj'

i=0
#silver
while True:
	entry=f'{lista}{i}'
	encoded=hashlib.md5(entry.encode()).hexdigest()
	if encoded[0:5]=='00000' and encoded[5]!=0:
		print(entry, encoded)
		break
	i+=1

#gold
i=0
while True:
	entry=f'{lista}{i}'
	encoded=hashlib.md5(entry.encode()).hexdigest()
	if encoded[0:6]=='000000' and encoded[6]!=0:
		print(entry, encoded)
		break
	i+=1