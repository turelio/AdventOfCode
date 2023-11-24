# 2023-11-24
#Start	14:05
#Part1	14:25	20min
#Part2	14:27	2min
#Total	22min
with open('input') as f:
	lista=f.read().strip()
print(lista)

test=lista
# test='^.....^.^^^^^.^..^^.^.......^^..^^^..^^^^..^.^^.^.^....^^...^^.^^.^...^^.^^^^..^^.....^.^...^.^.^^.^'
print(len(test))
    # Its left and center tiles are traps, but its right tile is not.
    # Its center and right tiles are traps, but its left tile is not.
    # Only its left tile is a trap.
    # Only its right tile is a trap.

patterns=set([('^','^','.'),('.','^','^'),('^','.','.'),('.','.','^')])
rows=[test]
while len(rows)!=400000:
	if len(rows)%10000==0:
		print(len(rows))
	# for r in rows:
	# 	print(''.join(r))
	prev=rows[-1]
	# print(prev)
	row=''
	for i,v in enumerate(prev):
		trips=[i-1,i,i+1]
		trips=[prev[i] if i in range(len(prev)) else '.' for i in trips]
		# print(i,trips)
		if tuple(trips) in patterns:
			row+='^'
		else:
			row+='.'
	rows.append(row)
print(len(rows))
silver=0
for r in rows:
	silver+=r.count('.')
print(silver)