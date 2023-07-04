aoc={
"2015":[5,13,22,21,38,(13,4),(50,2),(14,9),(23,1),(17,1),(40,1),(7,56),(15,5),(10,14),(42,5),(7,14),(44,5),(20,5),(29,22),(13,30),(27,7),0,0,0,0],
"2016":[54,28,15,54,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
"2017":[32,6,77,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
"2018":[39,17,39,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
"2019":[9,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
"2020":[10,15,65,90,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
"2021":[15,15,55,115,80,85,30,146,149,50,70,270,62,115,240,122,83,0,0,0,100,(31,0),0,0,0,(62,0)],
"2022":[15,22,21,12,30,8,233,93,110,36,47,135,108,64,95,0,(105,0),66,0,0,69,(75,0),111,0,(87,0)]
}

def count_progress(lista):
	counter=0
	suma=0
	for l in lista:
		year_count=0
		year_sum=0
		# lista[i]=list(map(int, lista[i]))
		for i in lista[l]:
			if i==0:
				continue
			elif isinstance(i,int):
				year_count+=2
				year_sum+=i
			else:
				# print(type(i), i)
				if 0 in i:
					year_count+=1
				else:
					year_count+=2
				year_sum+=sum(i)
		counter+=year_count
		suma+=year_sum
		print(f'{l}\t{"{:02d}".format(year_count)}/50\t{"{:02d}".format(year_sum//60)}:{"{:02d}".format(year_sum%60)}')


	msg=f"[{counter}/{len(aoc)*50}] done, {'{:.1%}'.format(counter/(len(aoc)*50))} progress, {suma} minutes / {suma//60}:{suma%60}h total, ~{'{:.0f}'.format(suma/counter)} minutes per star"
	print(msg)
	return msg
#print(count_progress(aoc))
message=count_progress(aoc)
out=f"{message}\n"
out+="2015|2016|2017|2018|2019|2020|2021|2022\n"
out+="-|-|-|-|-|-|-|-\n"
for i in range(25):
	for j in range(2015,2023):
		if isinstance(aoc[str(j)][i], int):
			value=aoc[str(j)][i]
		else:
			value=sum(aoc[str(j)][i])
		out+=f"{value}|"
	out+="\n"


with open("README.md", "w") as f:
	f.write(out)
