# each element contains completion time in minutes, tuple means the times were split into Part 1 and 2
data={
"2015":[5,13,22,21,38,(13,4),(50,2),(14,9),(23,1),(17,1),(40,1),(7,56),(15,5),(10,14),(42,5),(7,14),(44,5),(20,5),(29,22),(13,30),(27,7),(202,3),(43,1),(35,41),(28,1)],
"2016":[54,28,15,54,(14,15),(2,6),(20,10),(62,1),(33,40),(54,2),0,(17,1),(60,8),(51,23),(36,40),(15,71),(59,1),(20,2),(38,87),(33,4),(33,5),(32,0),(41,40),(69,10),(22,0)],
"2017":[32,6,77,(3,4),(8,4),(21,1),(24,71),(11,2),(37,31),(36,0),(14,2),(10,10),(17,30),0,(10,7),(14,22),(17,33),0,0,0,0,0,0,0,0],
"2018":[(3,36),(8,9),(23,16),(41,10),(18,22),(24,35),(13,53),(18,0),0,(22,2),(18,17),(46,39),0,(18,21),(162,23),0,0,(19,12),0,0,0,0,0,0,0],
"2019":[9,25,(16,24),(11,12),(90,57),(22,19),0,(9,18),0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
"2020":[10,15,65,90,(50,10),(13,5),(12,14),(7,25),(15,7),(10,0),(20,27),(19,19),(7,0),(23,35),(17,5),(23,45),(18,7),(44,0),0,0,0,0,0,0,0],
"2021":[15,15,55,115,80,85,30,146,149,50,70,270,62,115,240,122,83,0,0,0,100,(31,0),0,0,0,(62,0)],
"2022":[15,22,21,12,30,8,233,93,110,36,47,135,108,64,95,(260,50),(105,0),66,0,0,69,(75,0),111,0,(87,0)],
"2023":[(4,11),(15,6),(30,13),(8,13),(26,244),(10,1),(101,34),(15,39),(15,4),(32,108),(13,27),(17,0),(54,12),(17,39),(6,26),0,0,0,0,0,0,0,0,0,0]
}

def count_progress(data):
	summary=[]
	counter=0
	suma=0
	for year,days in data.items():
		year_count=0
		year_sum=0
		for i in days:
			if i==0:
				continue
			elif isinstance(i,int):
				year_count+=2
				year_sum+=i
			else:
				if 0 in i:
					year_count+=1
				else:
					year_count+=2
				year_sum+=sum(i)
		counter+=year_count
		suma+=year_sum
		
		print(f'{year}\t[{year_count:02}/50] stars\t\t{(year_count/50):.1%}\t\t{(year_sum//60):02}:{(year_sum%60):02}h\t\t{year_sum:4} minutes, ~{(year_sum/year_count):.0f} minutes per star')
		summary.append((year, year_count, year_sum))
	
	total=('Total',counter,suma)
	print(f'Total\t[{counter:02}/{(len(data)*50):02}] stars\t\t{counter/(len(data)*50):.1%}\t\t{(suma//60):02}:{(suma%60):02}h\t\t{suma:4} minutes, ~{(suma/counter):.0f} minutes per star')

	return total,summary[::-1]

total,summary=count_progress(data)
year, year_count, year_sum = total
out='## Summary\n'
out+='Year|Stars|%|Time spent|Minutes per star\n'
out+='-|-|-|-|-\n'
out+=f'{year}|[{year_count}/{len(data)*50}]|{(year_count/(len(data)*50)):.1%}|{(year_sum//60):02}:{(year_sum%60):02}h|{(year_sum/year_count):.0f} min/★\n'
for year, year_count, year_sum in summary:
	entry=f'{year}|[{year_count:02}/50]|{(year_count/50):.1%}|{(year_sum//60):02}:{(year_sum%60):02}h|{(year_sum/year_count):.0f} min/★\n'
	out+=entry

with open("README.md", "w", encoding="utf-8") as f:
	f.write(out)
