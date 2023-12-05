# 2023-12-04
#Start	18:20 	130min stopped
#Part1	
#Part2	
#Total
with open('input') as f:
	lista=f.read()
lista=lista.split(',')
lista=[int(l) for l in lista]
# print(lista)

def valmode(ex,ip,mode):
	if mode==1:
		# print('immediate')
		return ex[ip]
	else:
		return ex[ex[ip]]
def intcomp(ex, inp):
	out=[]
	print('executing with input', inp)
	test2=[(i,v) for i,v in enumerate(ex)]
	print(test2)
	i=0
	while ex[i]!=99:
		print(f'looking at value {ex[i]} at {i}')
		opcode=ex[i]%100
		modes=list(str(ex[i]//100))
		modes=[int(m) for m in modes][::-1]+[0]*(3-len(modes))
		if opcode==99:
			break

		# opcode=ex[i]
		# valmode(i,modes,ex)
		print(f'\topcode {opcode}, modes {modes}')
		# val=valmode(i,modes,ex)
		if opcode==1:
			paras=ex[i+1:i+4]
			val1=valmode(ex,i+1,modes[0])
			val2=valmode(ex,i+2,modes[1])
			result=val1+val2
			val3=ex[i+3]
			print('\t',modes)
			print('\t',paras)
			print('\t',[val1,val2])
			print(f'\t{result} ({val1}+{val2}) written to {val3} (prev {ex[val3]})')
			ex[val3]=result
			i+=4
		# mult
		elif opcode==2:
			val1=valmode(ex,i+1,modes[0])
			val2=valmode(ex,i+2,modes[1])
			result=val1*val2
			val3=ex[i+3]
			ex[val3]=result
			print(f'\t{result} written to i {val3}')

			i+=4
		# save input to i+1
		elif opcode==3:
			print(f'\tinput {inp} written to {ex[i+1]} (prev {ex[ex[i+1]]})')
			ex[ex[i+1]]=inp
			i+=2
		# output value at i+1
		elif opcode==4:
			# print(i+1)
			val1=valmode(ex,i+1,modes[0])
			out.append(val1)
			print(f'\toutput value: {val1}')
			i+=2
		# print(ex)
		#jump-if-true
		elif opcode==5:
			paras=ex[i+1:i+3]
			val1=valmode(ex,i+1,modes[0])
			val2=valmode(ex,i+2,modes[1])
			# val2=ex[i+2]
			print('\t',modes)
			print('\t',paras)
			print('\t',[val1,val2])
			if val1!=0:
				print(f'\t{val1}!=0, jumping to i={val2}')
				i=val2
			else:	
				print(f'\t{val1}=0, moving normally')
				i+=3
		# jump-if-false
		elif opcode==6:
			val1=valmode(ex,i+1,modes[0])
			val2=valmode(ex,i+2,modes[1])
			# val1=ex[i+1]
			# val2=ex[i+2]
			print('\t',val1,val2)
			if val1==0:
				print(f'\tnew i = {val2}')
				i=val2
			else:	
				i+=3
		# less than
		elif opcode==7:
			val1=valmode(ex,i+1,modes[0])
			val2=valmode(ex,i+2,modes[1])
			val3=ex[i+3]
			if val1<val2:
				ex[val3]=1
			else:
				ex[val3]=0
			i+=4
		# equals
		elif opcode==8:
			paras=ex[i+1:i+4]
			val1=valmode(ex,i+1,modes[0])
			val2=valmode(ex,i+2,modes[1])
			val3=ex[i+3]
			print('\t',modes)
			print('\t',paras)
			print('\t',[val1,val2,val3])

			if val1==val2:
				print(f'\tequal, writing 1 to {val3} (prev ({ex[val3]}))')
				ex[val3]=1
			else:
				print(f'\tunequal, writing 0 to {val3} (prev ({ex[val3]}))')
				ex[val3]=0
			i+=4
	# print(f'encountered {ex[i]} at {i}')
		else:
			print('bad opcode', opcode)
			break
	return ex, out[-1]

program=[3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
c=[4,3,2,1,0]


# output:
# Process000: 4
# Process001: 43
# Process002: 432
# Process003: 4321
# Process004: 43210