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
	suma=0
	for i in lista:
		lista[i]=list(map(int, lista[i]))
		counter+=lista[i].count(0)
		suma+=sum(lista[i])

	result=len(aoc)*25-counter

	msg=f"[{result}/{len(aoc)*25}] done, {'{:.1%}'.format(result/(len(aoc)*25))} progress, {suma} minutes total"
	print(msg)
	return msg
#print(count_progress(aoc))

def mdtable(lista):
	out=f"{count_progress(aoc)}\n"
	out+="2015|2016|2017|2018|2019|2020|2021\n"
	out+="-|-|-|-|-|-|-\n"
	for i in range(25):
		for j in range(2015,2022):
			out+=f"{lista[str(j)][i]}|"
		out+="\n"
	return out

f=open("README.md", "w")
f.write(mdtable(aoc))
f.close()
