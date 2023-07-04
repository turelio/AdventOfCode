#Start	10:41	20211216
#Part1	12:03	82min przerwa
#Part2	
#Total
with open('input') as f:
	lista=f.read().strip()

print(len(lista))


hex=[0,1,2,3,4,5,6,7,8,9]
code=[]
#ex2="EE00D40C823060"
#ex="C0015000016115A2E0802F182340"
ex=lista
for e in ex:
	#print(f"{e} => {int(e, 16)} => {bin(int(e, 16))[2:].zfill(4)}")
	code.append(bin(int(e, 16))[2:].zfill(4))

code=''.join(code)
print(code)

version_list=[]
def decipher(code, i):
	print("new packet")
	version=code[i:i+3]
	version=int(version,2)
	version_list.append(version)
	p_type=code[i+3:i+6]
	p_type=int(p_type,2)
	print(f"version {version}, type {p_type}")
	i=i+6
	if p_type==4:
		print("type literal")
		packet_values=[]
		while True:
			packet=code[i:i+5]
			#print(packet, packet[0])
			packet_values.append(packet[1:])
			i+=5
			if packet[0]=='0':
				break
		#print(f"rest is {code[i:]}")
		packet_values=''.join(packet_values)
		print(f"{packet_values} => {int(packet_values, 2)}")
		return i
	else:
		print("type operator")
		if code[i]=="0":
			print("15 bits, total length in bits")
			i=i+1
			number=code[i:i+15]
			print(number, int(number,2))
			number=int(number,2)
			i+=15
			j=i
			while i-j!=number:
				i=decipher(code,i)
				print(i-j)
			return i
		else:
			print("11 bits, number of sub-packets immediately contained")
			i=i+1
			number=code[i:i+11]
			print(number, int(number,2))
			number=int(number,2)
			i+=11
			num=0
			while num in range(number):
				i=decipher(code,i)
				num+=1
			return i
decipher(code,0)

print(sum(version_list))