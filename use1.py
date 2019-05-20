import random
import sys
R=33
C=45

sys.setrecursionlimit(3000)
visited=[]
trac=[]

def isLegit(r, c):
    if r<R and r>=0 and c<C and c>=0:
        return True
    else:
        return False

def generate(pac,food):
    visited.append(pac)
    init = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    random.shuffle(init)
    init = [(pac[0]+i[0], pac[1]+i[1]) for i in  init]
    for i in init:
    	if isLegit(i[0], i[1]):
    		if dfs(i, visited, food) == True:
    			break
    return visited

def dfs(i, visited, food):
	if i == food:
		visited.append(i)
		return True

	init = [(-1, 0), (0, -1), (1, 0), (0, 1)]
	random.shuffle(init)
	init = [(i[0]+j[0], i[1]+j[1]) for j in init]
	init = [k for k in init if (isLegit(k[0], k[1])) and (k not in visited)]
	if len(init) == 0:
		return False
	visited.append(i)

	for j in init:
		if dfs(j, visited, food) == True:
			return True
	return False
