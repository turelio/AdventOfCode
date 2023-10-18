# 2023-10-17
#Start	21:48
#Part1	22:29	41min
#Part2	22:39	10min
#Total	51min

with open('input') as f:
	lista=f.read().splitlines()

data={}
lista=sorted(lista)

for l in lista:
	l=l.split()
	date=l.pop(0)[1:]
	time=l.pop(0)[:-1]
	if l[-1]=='shift':
		gid=l[1][1:]
		current=gid
		if current not in data:
			data[current]={}
		if date not in data[gid]:
			data[current][date]=[0]*60
	if l[-1]=='asleep':
		nap_start=int(time[-2:])
	if l[-1]=='up':
		nap_end=int(time[-2:])
		if date not in data[gid]:
			data[current][date]=[0]*60
		for i in range(nap_start,nap_end):
			data[current][date][i]=1

naps=[]
for k,v in data.items():
	nap=0
	for k2, v2 in v.items():
		nap+=sum(v2)
	naps.append([k,nap])
naps=sorted(naps, key=lambda x:x[1])

stats=[]
for k,v in data.items():
	cum_minutes=[t for t in v.values()]
	cum_minutes=list(zip(*cum_minutes))
	cum_minutes=[sum(i) for i in cum_minutes]
	max_minute=cum_minutes.index(max(cum_minutes))
	stats.append([int(k),max_minute, max(cum_minutes), sum(cum_minutes)])
gold=sorted(stats, key=lambda x:x[2])[-1]
silver=sorted(stats, key=lambda x:x[3])[-1]

print('Silver: ', silver[0]*silver[1])
print('Gold: ', gold[0]*gold[1])