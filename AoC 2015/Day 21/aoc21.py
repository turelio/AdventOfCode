#2022-12-29
#Part1	11:00-11:27 (27min)
#Part2	11:27-11:34 (7min)
#Total	34min
import itertools

weapons=[(4,0,8), (5,0,10), (6,0,25), (7,0,40), (8,0,74)]

armors=[(0,1,13),(0,2,31),(0,3,53),(0,4,75),(0,5,102),(0,0,0)]

rings=[(1,0,25),(2,0,50),(3,0,100),(0,1,20),(0,2,40),(0,3,80)]
rings+=list(itertools.combinations(rings,2))+[(0,0,0)]

def fight(items):
	bhp=109
	bdmg=8
	barmor=2
	hp=100
	dmg=0
	armor=0
	cost=0

	for item in items:
		dmg+=item[0]
		armor+=item[1]
		cost+=item[2]

	while True:
		hit=dmg-barmor
		if hit<=0:
			hit=1
		bhp-=hit
		if bhp<=0:
			return True, cost
		bhit=bdmg-armor
		if bhit<=0:
			hit=1
		hp-=bhit
		if hp<=0:
			return False, cost

silver=[]
gold=[]
for weapon in weapons:
	for armor in armors:
		for ring in rings:
			# print(ring, len(ring))
			if len(ring)==2:
				ring=[sum(n) for n in list(zip(*ring))]
				# print(ring)
			items=[]
			items.append(weapon)
			items.append(armor)
			items.append(ring)
			won,cost=fight(items)
			if won:
				silver.append(cost)
			else:
				gold.append(cost)
print(min(silver), max(gold))
