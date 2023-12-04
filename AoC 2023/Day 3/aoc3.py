# 2023-12-02
# Start	06:00	
# Part1	06:30	30min
# Part2	06:43	13min
# Total	43min
# Rewrote without using itertools by looking for special characters instead of numbers' neighbors
import re
with open('input') as f:
	lista=f.read().splitlines()

silver,gold=0,0
nums={}

xr,yr=len(lista[0]), len(lista)
for y,l in enumerate(lista):
	test=re.finditer(r'(\d+)', l)
	for number in test:
		x1,x2 = number.span()
		suma=int(number.group(0))
		for t in range(x1,x2):
			nums[(t,y)]=(x1,x2,y,suma)

silver=set()

gold=0
for i,y in enumerate(lista):
	for j,x in enumerate(y):
		if x!='.' and not x.isdigit():
			near=[(j-1,i-1),(j,i-1),(j+1,i-1),(j-1,i),(j+1,i),(j-1,i+1),(j,i+1),(j+1,i+1)]
			found=set()
			for n in near:
				if n in nums:
					silver.add(nums[n])
					found.add(nums[n])
			if x=='*' and len(found)==2:
				found=list(found)
				gold+=found[0][3]*found[1][3]
silver=sum([s[3] for s in silver])
print('Silver:',silver,'Gold:',gold)
