with open('input') as f:
    map=f.read().splitlines()
# 31 length 0-30, 323, 0-322
m_length=len(map)
m_width=len(map[0])

def tree_count(a,b):
    x=a
    y=b
    count=0
    while y<=(m_length-1):
        if map[y][x]=='#':
            count+=1
        x+=a
        y+=b
        if x>30:
            x=x-31
    return count

# Part 1
print(tree_count(3,1))
# Part 2
print(tree_count(3,1)*tree_count(1,1)*tree_count(5,1)*tree_count(7,1)*tree_count(1,2))

