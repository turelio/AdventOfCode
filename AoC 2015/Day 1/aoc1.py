#0 12:24
#1 12:27 3 minutes
#2 12:29 5 minutes
with open('input') as f:
	directions=f.read()

floor=0
for c, d in enumerate(directions):
	if d=="(":
		floor+=1
	else:
		floor-=1
	if floor==-1:
		print(c+1)

print(floor)