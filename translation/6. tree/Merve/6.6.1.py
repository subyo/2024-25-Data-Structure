1	def dfs(current, goal):
2	if current == goal:
3	return [current]
4
5	for next in adjacent(current):
6	result = dfs(next)
7	if result != None:
8	return [current] + result
9
10	return None
