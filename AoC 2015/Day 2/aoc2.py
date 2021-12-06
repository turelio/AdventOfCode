#0 12:32 
#1 12:39 7 min
#2 12:45 13 min
with open('input') as f:
	lista=f.read().splitlines()


lista=[l.split('x') for l in lista]
total=0
for i in lista:
	l, w, h=int(i[0]), int(i[1]), int(i[2])
	total+=2*l*w + 2*w*h + 2*h*l + min([l*w, w*h, h*l])

print(total)
total2=0
for i in lista:
	l, w, h=int(i[0]), int(i[1]), int(i[2])
	min1, min2=sorted([l,w,h])[0], sorted([l,w,h])[1]
	total2+=2*min1+2*min2+l*w*h
print(total2)