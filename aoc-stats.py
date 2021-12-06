aoc={
"2015":[5,13,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
"2016":[54,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
"2017":[32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
"2018":[39,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
"2019":[9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
"2020":[10,15,65,90,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
"2021":[15,15,55,115,80,85,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
}

def count_progress(lista):
	counter=0
	for i in lista:
		counter+=lista[i].count(0)
	result=len(aoc)*25-counter
	print(f"[{result}/{len(aoc)*25}] done, {'{:.1%}'.format(result/(len(aoc)*25))} progress")
	return result
print(count_progress(aoc))

def mdtable(lista):
	out="2015|2016|2017|2018|2019|2020|2021\n"
	out+="-|-|-|-|-|-|-\n"
	for i in range(25):
		for j in range(2015,2022):
			out+=f"{lista[str(j)][i]}|"
		out+="\n"
	return out

f=open("README.md", "w")
f.write(mdtable(aoc))
f.close()
