# don't run it anymore lol

import os
temp='''# 
# Start		
# Part1		
# Part2		
# Total	
with open('input') as f:
	lista=f.read()

'''

def build_folder(n):
	os.makedirs(f'AoC {n}')
	for j in range(1,26):
		os.makedirs(f'AoC {n}/Day {j}')
		filedir=f"AoC {n}/Day {j}/aoc{j}.py"
		with open(filedir, "w") as f:
			f.write(temp)

#build_folder(2024)