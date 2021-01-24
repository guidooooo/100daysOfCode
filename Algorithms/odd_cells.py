class Solution(object):
	def oddCells(self, n, m, indices):
		"""
		:type n: int
		:type m: int
		:type indices: List[List[int]]
		:rtype: int
		"""

		
		count = 0
		matrix=[[0 for _ in range(m)] for _ in range(n)]

		for i in indices:
			for k in range(m):
				matrix[i[0]][k] +=1

			for j in range(n):
				matrix[j][i[1]] +=1

		for x in matrix:
			for y in x:
				if y % 2 !=0:
					count +=1

		return count

sol = Solution()
print(sol.oddCells(n = 2, m = 3, indices = [[0,1],[1,1]]))
print(sol.oddCells(n = 2, m = 2, indices = [[1,1],[0,0]]))