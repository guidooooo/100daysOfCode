"""
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. Return the minimum time in seconds to visit all the points in the order given by points.

You can move according to these rules:

In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.
"""

class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        current_point = points.pop(0)
        target_point = points.pop(0)

        seconds = 0

        move_fg = False

        while True:

        	if current_point[0] < target_point[0]:
        		current_point[0] +=1
        		move_fg = True
        	elif current_point[0] > target_point[0]:
        		current_point[0] -=1
        		move_fg = True

        	if current_point[1] < target_point[1]:
        		current_point[1] +=1
        		move_fg = True
        	elif current_point[1] > target_point[1]:
        		current_point[1] -=1
        		move_fg = True

        	if move_fg: seconds +=1

        	if current_point == target_point and len(points)==0:
        		return seconds
        	elif current_point == target_point:
        		target_point = points.pop(0)


sol = Solution()
print(sol.minTimeToVisitAllPoints(points = [[1,1],[3,4],[-1,0]]))
print(sol.minTimeToVisitAllPoints(points = [[3,2],[-2,2]]))