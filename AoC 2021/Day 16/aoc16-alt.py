#Start	10:41	20211216
#Part1	12:03	82min przerwa
#Part2	12:13-12:53	40min
#Total	122min
with open('input') as f:
	lista=f.read().strip()

code=''.join([bin(int(l, 16))[2:].zfill(4) for l in lista])
silver=[]

def get_value(val_list, p_type):
	if p_type==0:
		return sum(val_list)
	elif p_type==1:
		product=1
		for v in val_list:
			product*=v
		return product
	elif p_type==2:
		return min(val_list)
	elif p_type==3:
		return max(val_list)
	elif p_type==5:
		if val_list[0]>val_list[1]:
			return 1
		else:
			return 0
	elif p_type==6:
		if val_list[0]<val_list[1]:
			return 1
		else:
			return 0
	elif p_type==7:
		if val_list[0]==val_list[1]:
			return 1
		else:
			return 0

def decipher(code, i):
	version=int(code[i:i+3],2)
	silver.append(version)
	p_type=int(code[i+3:i+6],2)
	i+=6
	if p_type==4:
		packet_values=[]
		while True:
			packet=code[i:i+5]
			packet_values.append(packet[1:])
			i+=5
			if packet[0]=='0':
				break
		packet_values=''.join(packet_values)
		val=int(packet_values,2)
		return i,val
	else:
		val_list=[]
		if code[i]=="0":
			i+=1
			number=code[i:i+15]
			number=int(number,2)
			i+=15
			j=i
			while i-j!=number:
				deciphered=decipher(code,i)
				i=deciphered[0]
				val_list.append(deciphered[1])
		else:
			i=i+1
			number=code[i:i+11]
			number=int(number,2)
			i+=11
			num=0
			while num in range(number):
				deciphered=decipher(code,i)
				i=deciphered[0]
				val_list.append(deciphered[1])
				num+=1
		val=get_value(val_list, p_type)
		return i,val

print(decipher(code,0)[1])
print(sum(silver))