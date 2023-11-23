#2023-11-23
#Start	14:05
#Part1	17:57	232min-30min przerwy=202min
#Part2	18:00	3min
#Total	205min

costs={1:53,2:73,3:113,4:173,5:229}

# dicts, even deep copies kept causing bugs so i crammed all the variables
def fight(hp, armor, mana, spent, boss_hp, boss_dmg, p_cd,s_cd,r_cd,spell,gold=0):
	if gold:
		hp-=1
		if hp<=0:
			return
	if p_cd:
		boss_hp-=3
		p_cd-=1
	if s_cd:
		armor=7
		s_cd-=1
	else:
		armor=0

	if r_cd:
		mana+=101
		r_cd-=1
	if boss_hp<=0:
		silver.add(spent)
		return

	if spell==1:
		boss_hp-=4
	elif spell==2:
		boss_hp-=2
		hp+=2
	elif spell==3:
		if s_cd:
			return
		s_cd=6
	elif spell==4:
		if p_cd:
			return
		p_cd=6
	elif spell==5:
		if r_cd:
			return
		r_cd=5
	mana-=costs[spell]
	spent+=costs[spell]
	if spent>min(silver):
		return
	if mana<0:
		return
	if boss_hp<=0:
		silver.add(spent)
		return

	if p_cd:
		boss_hp-=3
		p_cd-=1
	if s_cd:
		armor=7
		s_cd-=1
	else:
		armor=0
	if r_cd:
		mana+=101
		r_cd-=1
	if boss_hp<=0:
		silver.add(spent)
		return

	dmg=boss_dmg-armor
	if dmg<=0:
		dmg=1
	hp-=dmg
	if hp<=0:
		return

	for choice in [1,2,3,4,5]:
		fight(hp, armor, mana, spent, boss_hp, boss_dmg, p_cd,s_cd,r_cd,choice,gold)

silver=set()
silver.add(100000)
for choice in [1,2,3,4,5]:
	fight(50,0,500,0,58,9,0,0,0,choice)

print(sorted(list(silver)))

silver=set()
silver.add(10000000)
for choice in [1,2,3,4,5]:
	fight(50,0,500,0,58,9,0,0,0,choice,1)

print(sorted(list(silver)))
