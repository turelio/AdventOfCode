# 2023-12-06
# Start	06:00
# Part1	06:10	10min
# Part2	06:11	1min
# Total	11min

silver=[(62,553),(64,1010),(91,1473),(90,1074)]
gold=[(62649190,553101014731074)]

def solve(times):
	total=1
	for d, record in times:
		won=0
		for i in range(d+1):
			if (i*(d-i))>record:
				won+=1
				pass
		total*=won
	return total

print('Silver:',solve(silver))
print('Gold:',solve(gold))