''''

You are given two integers m and n representing a 0-indexed m x n grid. You are also given two 2D integer arrays guards and walls where guards[i] = [rowi, coli] and walls[j] = [rowj, colj] represent the positions of the ith guard and jth wall respectively.

A guard can see every cell in the four cardinal directions (north, east, south, or west) starting from their position unless obstructed by a wall or another guard. A cell is guarded if there is at least one guard that can see it.

Return the number of unoccupied cells that are not guarded.

 

Example 1:


Input: m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]]
Output: 7
Explanation: The guarded and unguarded cells are shown in red and green respectively in the above diagram.
There are a total of 7 unguarded cells, so we return 7.
Example 2:


Input: m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]]
Output: 4
Explanation: The unguarded cells are shown in green in the above diagram.
There are a total of 4 unguarded cells, so we return 4.
 

Constraints:

1 <= m, n <= 105
2 <= m * n <= 105
1 <= guards.length, walls.length <= 5 * 104
2 <= guards.length + walls.length <= m * n
guards[i].length == walls[j].length == 2
0 <= rowi, rowj < m
0 <= coli, colj < n
All the positions in guards and walls are unique.

'''


class Solution:
    def countUnguarded(self, m: int, n: int, guards: list[list[int]], walls: list[list[int]]) -> int:
        grid=[[0 for _ in range((n))] for _ in range(m)]
        for guard in guards:
            grid[guard[0]][guard[1]]=3 
        for wall in walls:
            grid[wall[0]][wall[1]]=1 
        for i in range(m):
            for j in range(n):
                if grid[i][j]==3:
                    self.checkLeft(i,j,grid)
                    self.checkRight(n,i,j,grid)
                    self.checkTop(i,j,grid)
                    self.checkBottom(m,i,j,grid)
        count=0 
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    count+=1
        return count
        
    def checkLeft(self,row:int,col:int,grid:list[list[int]]):
        for j in range(col-1,-1,-1):
            if grid[row][j]==3 or grid[row][j]==1:
                return 
            grid[row][j]=2
    def checkRight(self,n:int,row:int,col:int,grid:list[list[int]]):
        for j in range(col+1,n):
            if grid[row][j]==3 or grid[row][j]==1:
                return 
            grid[row][j]=2 
    def checkTop(self,row:int,col:int,grid:list[list[int]]):
        for i in range(row-1,-1,-1):
            if grid[i][col]==3 or grid[i][col]==1:
                return 
            grid[i][col]=2
    def checkBottom(self,m:int,row:int,col:int,grid:list[list[int]]):
        for i in range(row+1,m):
            if grid[i][col]==3 or grid[i][col]==1:
                return 
            grid[i][col]=2

class TestApp:
    def testCaseOne(self):
        assert Solution().countUnguarded(4,6,[[0,0],[1,1],[2,3]],[[0,1],[2,2],[1,4]])==7 
    def testCaseTwo(self):
        assert Solution().countUnguarded(3,3,[[1,1]],[[0,1],[1,0],[2,1],[1,2]])==4 
    def testCaseThree(self):
        assert Solution().countUnguarded(5,6,[[1,1],[1,4],[2,3]],[[0,0],[4,3],[4,5]])==7