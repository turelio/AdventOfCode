# 2023-11-20
#Start	18:19
#Part1	19:13	54min
#Part2	19:15	2min	
#Total	56min
with open('input') as f:
	lista=f.read().splitlines()

chips=[l for l in lista if l[0]=='v']
bots=[l for l in lista if l[0]=='b']

bot_values={}
for bot in bots:
	bot=bot.split()
	bot_values[int(bot[1])]={'values':set(),'low':[int(bot[6]),bot[5]], 'high':[int(bot[-1]), bot[-2]]}

for c in chips:
	c=c.split()
	bot_values[int(c[-1])]['values'].add(int(c[1]))

outputs={}

def resolve(k):
	if len(bot_values[k]['values'])!=2:
		return
	else:
		# print('resolving',k, bot_values[k])
		if bot_values[k]['values']==set([61,17]):
			print('SILVER', k)
		if bot_values[k]['low'][1]=='bot':
			bot_values[bot_values[k]['low'][0]]['values'].add(min(bot_values[k]['values']))
		else:
			if bot_values[k]['low'][0] not in outputs:
				outputs[bot_values[k]['low'][0]]=[]
			outputs[bot_values[k]['low'][0]].append(min(bot_values[k]['values']))

		if bot_values[k]['high'][1]=='bot':
			bot_values[bot_values[k]['high'][0]]['values'].add(max(bot_values[k]['values']))
		else:
			if bot_values[k]['high'][0] not in outputs:
				outputs[bot_values[k]['high'][0]]=[]
			outputs[bot_values[k]['high'][0]].append(max(bot_values[k]['values']))

		bot_values[k]['values']=set()
		resolve(bot_values[k]['low'][0])
		resolve(bot_values[k]['high'][0])
		return

for k,v in bot_values.items():
	if len(v['values'])==2:
		start=k

resolve(start)

print('GOLD', outputs[0][0]*outputs[1][0]*outputs[2][0])