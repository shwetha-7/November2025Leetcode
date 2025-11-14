class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        mat=[[0 for _ in range(n)] for _ in range(n)]
        for query in queries:
            start_row,start_col=query[0],query[1]
            end_row,end_col=query[2],query[3]
            for i in range(start_row,end_row+1):
                for j in range(start_col,end_col+1):
                    mat[i][j]+=1
        return mat
    
class Solution:
    def rangeAddQueries(self, n: int, queries: list[list[int]]) -> list[list[int]]:
        mat=[[0 for _ in range(n)] for _ in range(n)]
        for query in queries:
            row1,row2=query[0],query[2]
            for i in range(row1,row2+1):
                mat[i][query[1]]+=1
                if query[3]+1<n:
                    mat[i][query[3]+1]-=1
        # apply prefix sum at for each row 
        for i in range(n):
            for j in range(1,n):
                    mat[i][j]+=mat[i][j-1]
        return mat

class TestApp:
    def test_case_one(self):
        assert Solution().rangeAddQueries(3,[[1,1,2,2],[0,0,1,1]])==[[1,1,0],[1,2,1],[0,1,1]]
    def test_case_two(self):
        assert Solution().rangeAddQueries(2,[[0,0,1,1]])==[[1,1],[1,1]]
