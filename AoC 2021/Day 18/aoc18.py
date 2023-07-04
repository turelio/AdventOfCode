#Start	 20211218	
#Part1	
#Part2	
#Total
import re
with open('input') as f:
	lista=f.read()

ex=[[[[[9,8],1],2],3],4]

class node:
	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key
 
root=node(0)


def order(tree,lista,n):
	if isinstance(lista, list):
		print(f'{n} nested:',lista[0], lista[1], '\n')
		n2=n+1
		tree.left=node(lista[0])
		tree.right=node(lista[1])
		x0=order(tree.left,lista[0],n2)
		x1=order(tree.right,lista[1],n2)
		if n2>4:
			tree.val=0
	return tree
tree=order(root,ex,0)

print(tree.left.val)