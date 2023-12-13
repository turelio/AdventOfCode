# 2023-12-13
#Start	11:02	
#Part1	11:19	17min
#Part2	11:49	30min
#Total	47min
with open('input') as f:
	lista=f.read().splitlines()

scanners={}
for l in lista:
	i,j=l.split(': ')
	scanners[int(i)]=int(j)

severity={k:k*v for k,v in scanners.items()}
# find repeating cycle of positions, rest can be found by modulo
cycles={k:list(range(v))+list(range(v-2,0,-1)) for k,v in scanners.items()}
def forward(k,n):
	return cycles[k][n%len(cycles[k])]

silver=0
for k,v in scanners.items():
	if forward(k,k)==0:
		silver+=severity[k]
print('Silver:',silver)

d=0
while True:
	if d%1000000==0:
		print('delay',d)
	caught=False
	for k,v in scanners.items():
		if forward(k, k+d)==0:
			caught=True
			break
	if not caught:
		print('Gold:', d)
		break
	d+=1
