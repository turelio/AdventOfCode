#Start	12:25	20211217
#Part1	13:25	60min
#Part2	13:48	23min
#Total	83min
#bruteforced
with open('input') as f:
	lista=f.read()

x1=94
x2=151
y1=-156
y2=-103

target=[[i,j] for i in range(x1,x2+1) for j in range (y2, y1-1,-1)]

# [x, y, velx, vely, max_y]
def step(pos):
	pos[0]+=pos[2]
	pos[1]+=pos[3]
	if pos[1]>pos[4]:
		pos[4]=pos[1]
	if pos[2]>0:
		pos[2]-=1
	elif pos[2]<0:
		pos[2]+=1
	pos[3]-=1
	return pos

def test_probe(pos):
	while True:
		if pos[0]>x2 or pos[1]<y1:
			return None
		if [pos[0],pos[1]]in target:
			print("in target")
			return pos[4]
		pos=step(pos)

#print(target)
height_list=[]
hit_list=[]
for i in range(500):
	for j in range(-500,500):
		print(f"testing {i} {j}")
		result=test_probe([0,0,i,j,0])
		if result is not None:
			height_list.append(result)
			hit_list.append([i,j])

print(max(height_list), len(hit_list))


