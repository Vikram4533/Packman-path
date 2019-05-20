import sys
sys.setrecursionlimit(30000)
visited=[]
tracker=[]
walls=[]
R=33
C=45

def isLegit(r, c,wal):
	if r<R and r>=0 and c<C and c>=0:
		return (r,c) not in wal
	else:
		return False

def addPaths(r, c,wal):
	vis=[]
	if isLegit(r-1, c,wal) and (r-1, c) not in visited:
		vis.append((r-1, c))
	if isLegit(r, c-1,wal) and (r, c-1) not in visited:
		vis.append((r, c-1))
	if isLegit(r, c+1,wal) and (r, c+1) not in visited:
		vis.append((r, c+1))
	if isLegit(r+1, c,wal) and (r+1, c) not in visited:
		vis.append((r+1, c))
	return vis

def dfscaller(pac,food,wal,pos):
	visited.append(pac)
	ini=addPaths(pac[0],pac[1],wal)
	for i in ini:
		if dfs(i,visited,food,wal) == True:
			tracker.append(i)
			print(tracker[::-1])
			return tracker[::-1]
	
	#return tracker

def dfs(i,visited,food,wal):
	if(i==food):
		tracker.append(i)
		return True
	ini=addPaths(i[0],i[1],wal)
	if len(ini) == 0:
		return False
	visited.append(i)
	for j in ini:
		if dfs(j, visited, food, wal) == True:
			tracker.append(j)
			return True




























