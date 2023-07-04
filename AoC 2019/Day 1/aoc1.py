#Start	16:28 2021-12-06
#Part1	16:33
#Part2	16:37	
#Total	9min
from math import floor
with open('input') as f:
	lista=f.read().strip().splitlines()

suma=0
for l in lista:
	suma+=floor(int(l)/3-2)
print(suma)

suma=0
for l in lista:
	mass=int(l)
	while mass>0:
		mass=floor(mass/3)-2
		if mass<0:
			mass=0
		suma+=mass
print(suma)