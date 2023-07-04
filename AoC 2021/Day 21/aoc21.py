#Start	14:24	20211221
#Part1	14:55	31min
#Part2	16:34	99min-30min=69min
#Total	100min
# with open('input') as f:
# 	lista=f.read()
# ~75 seconds
# Player 1 starting position: 6
# Player 2 starting position: 7

class Player():
	def __init__(self, pos, name):
		self.pos=pos
		self.score=0
		self.score2=0
		self.name=name
	def move(self, n):
		for i in range(n):
			self.pos+=1
			if self.pos==11:
				self.pos=1
		self.score+=self.pos
	def add(self, n):
		self.score2+=n
class Dice():
	def __init__(self, n):
		self.n=n
	def roll(self):
		suma=0
		for i in range(3):
			suma+=self.n
			self.n+=1
			if self.n>100:
				self.n=1
		return suma


p1=Player(6, 'P1')
p2=Player(7, 'P2')
dice=Dice(1)
j=0
while True:
	p1.move(dice.roll())
	j+=3
	if p1.score>=1000:
		break
	p2.move(dice.roll())
	j+=3
	if p1.score>=1000:
		break	
#silver
print(j,p2.score, j*p2.score)

scores2=[0,0,0,1,3,6,7,6,3,1]
pos1,sc1=6,0
pos2,sc2=7,0
multi=1
p1_win=[]
p2_win=[]
def dirac(pos1,sc1,pos2,sc2, multi, p1_now):
	if p1_now:
		for i,v in enumerate(scores2):
			if v==0:
				continue
			new_multi=multi*v
			new_pos1 = ((pos1 + i - 1) % 10) + 1
			new_sc1=sc1+new_pos1
			if new_sc1>=21:
				p1.add(new_multi)
			else:
				dirac(new_pos1, new_sc1, pos2,sc2,new_multi, False)
	else:
		for i,v in enumerate(scores2):
			if v==0:
				continue
			new_multi=multi*v
			new_pos2 = ((pos2 + i - 1) % 10) + 1
			new_sc2=sc2+new_pos2
			if new_sc2>=21:
				p2.add(new_multi)
			else:
				dirac(pos1, sc1, new_pos2,new_sc2,new_multi, True)
		return
	#print(p1.score2, p2.score2)


dirac(pos1,sc1,pos2,sc2, multi, True)
print(p1.score2, p2.score2)