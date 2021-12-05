import re

with open('input') as f:
	lista0=f.read()

lista=lista0.split('\n\n')
for c, v in enumerate(lista):
	lista[c]=v.replace("\n", " ")
def contains(string, substring):
	return bool(re.search(substring, string))

#x=lista[1]
#print(x)
#print(contains(x, "pid:"))

fieldlist=["byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"]

counter1=0
lista2=[]
for l in lista:
	print(f"checking {l}")
	checklist=[]
	for i in fieldlist:
		checklist.append(contains(l, i))
	print(checklist)
	if all(checklist):
		#print("valid")
		counter1+=1
		lista2.append(l)
print(len(lista2))

print(counter1)
s = 'hgt:60in iyr:2014 byr:1919 pid:720386216 cid:99 ecl:gry hcl:#a97842 eyr:2028'
s2='156issan'
#measurement=re.search(r'[A-Za-z]+', s2).group()
#height=re.search(r'\d+', s2).group()
#print(height, measurement)
#print(re.search(r'hcl:(.*?)($|\s)', s).group(1))
def contains_valid(string, substring):
	fieldvalue=re.search(fr'{substring}(.*?)($|\s)', string).group(1)
	if substring=="byr:":
		if 2002>=int(fieldvalue)>=1920:
			#print(f"{substring} {fieldvalue} is valid")
			return True
	elif substring=="iyr:":
		if 2020>=int(fieldvalue)>=2010:
			return True
	elif substring=="eyr:":
		if 2030>=int(fieldvalue)>=2020:
			return True
	elif substring=="hgt:":
		try:
			measurement=re.search(r'[a-z]+', fieldvalue).group()
		except AttributeError:
			return False
		height=re.search(r'\d+', fieldvalue).group()
		print(height)
		print(measurement)
		if measurement=="in":
			if 76>=int(height)>=59:
				return True
			else:
				return False
		elif measurement=="cm":
			if 193>=int(height)>=150:
				return True
			else:
				return False
		else:
			return False
	elif substring=="hcl:":
		return bool(re.search(r"^#[0-9a-f]{6}$",fieldvalue))
	elif substring=="ecl:":
		return bool(re.search(r"^(amb|blu|brn|gry|grn|hzl|oth)$",fieldvalue))
	elif substring=="pid:":
		return bool(re.search(r"^[0-9]{9}$",fieldvalue))
	return False

counter2=0
for l in lista2:
	print(f"checking {l}")
	checklist=[]
	for i in fieldlist:
		checklist.append(contains_valid(l, i))
	print(checklist)
	if all(checklist):
		print("valid")
		counter2+=1
		
print(counter2)

#print(contains_valid(s, "pid:"))

# byr (Birth Year) - four digits; at least 1920 and at most 2002.
# iyr (Issue Year) - four digits; at least 2010 and at most 2020.
# eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
# hgt (Height) - a number followed by either cm or in:
#     If cm, the number must be at least 150 and at most 193.
#     If in, the number must be at least 59 and at most 76.
# hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
# ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
# pid (Passport ID) - a nine-digit number, including leading zeroes.
# cid (Country ID) - ignored, missing or not.


# OLD, 2020
# list=list.split("\n\n")
# j=0
# for i in list:
#     list[j]=i.replace("\n"," ")
#     list[j]=list[j].split(" ")
#     y=0
#     protodict= {}
#     for x in list[j]:
#         list[j][y]=list[j][y].split(":")
#         protodict.update({list[j][y][0]:list[j][y][1]})
#         y+=1
#     list[j]=protodict
#     j+=1
# #print(list)

# count=0
# for n in list:
#     if len(n)==8:
#         count+=1
#     elif (len(n)==7) and not ('cid' in n):
#         count+=1


# # 2, verification


# print(count)