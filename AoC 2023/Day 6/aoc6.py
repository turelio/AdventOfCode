# 2023-12-06
# Start	06:00
# Part1	06:10	10min
# Part2	06:11	1min
# Total	11min
import math
silver=[(62,553),(64,1010),(91,1473),(90,1074)]
gold=[(62649190,553101014731074)]

# replaced bruteforce with quadratic equation, using discriminant and roots
def solve(times):
	total=1
	# 0 = -x^2 + dx - record, discriminant = sqrt(d^2-4*record)
	for d, record in times:
		x1=math.ceil((-d + math.sqrt(d**2-4*record))/-2)
		x2=math.floor((-d - math.sqrt(d**2-4*record))/-2)
		total*=x2-x1+1
	return total

print('Silver:',solve(silver))
print('Gold:',solve(gold))

