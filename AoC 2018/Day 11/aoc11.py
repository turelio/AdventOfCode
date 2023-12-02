# 2023-12-02
#Start	10:59	
#Part1	11:17	18min
#Part2	11:34	17min
#Total	35min

# optimized from 40s to 4s by replacing itertools product used to generate square coordinates with manually summing rows in pre-calculated list
x,y,n=300,300,7803
# row/col 0 is unused
p_list=[[None]*(x+1) for _ in range(y+1)]
silver=[0,None]
gold=[0,None]

# pre-calculating
for i in range(1, x+1):
	for j in range(1, y+1):
		rack_id=i+10
		result=rack_id*j+n
		result*=rack_id
		result=(result//100)%10
		result-=5
		p_list[i][j]=result

# 17x17 is the biggest possible
for size in range(2,18):
	print(f'{size:2}x{size}')
	for i in range(1, x+2-size):
		for j in range(1, y+2-size):
			power=0
			for j2 in range(j,j+size):
				power+=sum(p_list[j2][i:i+size])
			if power>gold[0]:
				gold=[power, (i, j,size)]
			if size==3 and power>silver[0]:
				silver=gold=[power, (i, j,size)]

print(silver,gold)