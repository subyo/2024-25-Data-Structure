1	def solutionViable(matrix):
2	# Check that no set is empty
3	for i in range(9):
4	for j in range(9):
5	if len(matrix[i][j]) == 0:
6	return False
7
8	return True
9
10	def solve(matrix):
 


11
12	reduce(matrix)
13
14	if not solutionViable(matrix):
15	return None
16
17	if solutionOK(matrix):
18	return matrix
19
20	print("Searching...")
21
22	for i in range(9):
23	for j in range(9):
24	if len(matrix[i][j]) > 1:
25	for k in matrix[i][j]:
26	mcopy = copy.deepcopy(matrix)
27	mcopy[i][j] = set([k])
28
29	result = solve(mcopy)
30
31	if result != None:
32	return result
33
34	return None
