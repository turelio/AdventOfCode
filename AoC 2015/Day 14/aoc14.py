#2022-12-28
#Part1	12:06-12:16 (10min)
#Part2	12:16-12:30 (14min)
#Total	24min
with open('input') as f:
	lista=f.read().splitlines()

reindeers={}
for l in lista:
	l=l.split(' ')
	reindeers[l[0]]={'speed':int(l[3]), 'duration':int(l[6]), 'tduration':int(l[6]), 'cooldown':int(l[-2]), 'tcooldown':int(l[-2]), 'distance1':0,'distance2':0}

for i in range(2503):
	for k,v in reindeers.items():
		if v['duration']!=0:
			reindeers[k]['distance1']+=v['speed']
			reindeers[k]['duration']-=1
		else:
			reindeers[k]['cooldown']-=1
			if reindeers[k]['cooldown']==0:
				reindeers[k]['cooldown']=reindeers[k]['tcooldown']
				reindeers[k]['duration']=reindeers[k]['tduration']
	reindeers=dict(sorted(reindeers.items(), key=lambda x:x[1]['distance1'], reverse=True))
	winners=[x[0] for x in reindeers.items()if x[1]['distance1']==list(reindeers.items())[0][1]['distance1']]
	for w in winners:
		reindeers[w]['distance2']+=1

for k,v in reindeers.items():
	print(k, v['distance1'], v['distance2'])
