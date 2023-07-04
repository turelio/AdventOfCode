
#Start	10:25
#Part1	10:42
#Part2	11:34
#Total	69min
# First pass, 500ms	
import re
from sympy import symbols, solve, sympify, Eq, solveset

with open('input') as f:
	lista=f.read().splitlines()

expressions={}
expressions2={}
for l in lista:
	expressions[l[:4]]=l[6:]
	expressions2[l[:4]]=l[6:]

def solve(n):
	if re.match(r'(....) (.) (....)', n):
		t=re.search(r'(....) (.+) (....)', n)
		new=f'solve(expressions["{t[1]}"]) {t[2]} solve(expressions["{t[3]}"])'
		return eval(new)
	else:
		return eval(n)

silver=int(solve(expressions['root']))

def solve2(n):
	if n=='X':
		return n
	if n == 'fgtg == pbtm':
		left=solve2(expressions2["fgtg"])
		right='13751780524553'
		result=f'({left})'
		return result
	elif re.match(r'(....) (.) (....)', n):
		t=re.search(r'(....) (.+) (....)', n)
		new=f'(({solve2(expressions2[t[1]])}){t[2]}({solve2(expressions2[t[3]])}))'
		return new
	else:
		return f'{n}'

expressions2['root']='fgtg == pbtm'
expressions2['humn']='X'

test=solve2(expressions2['root'])
x = symbols("X")
test2=sympify(test)
gold=solveset(Eq(test2, 13751780524553),x)

print('Silver:', silver)
print('Gold:', gold)
print(test)
