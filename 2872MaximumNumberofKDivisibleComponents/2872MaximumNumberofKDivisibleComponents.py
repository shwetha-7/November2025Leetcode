from collections import defaultdict

class Solution:
    def maxKDivisibleComponents(self, n: int, edges: list[list[int]], values: list[int], k: int) -> int:
        adjacents=defaultdict(list)
        for n1,n2 in edges:
            adjacents[n1].append(n2)
            adjacents[n2].append(n1)
        res=0
        def dfs(curr:int,parent:int)->int:
            total=values[curr]
            for child in adjacents[curr]:
                if child!=parent:
                    total+=dfs(child,curr)
            if total%k==0:
                nonlocal res
                res+=1
            return total
        dfs(0,-1)
        return res
class TestApp:
    def test_case_one(self):
        assert Solution().maxKDivisibleComponents(5,[[0,2],[1,2],[1,3],[2,4]],[1,8,1,4,4],6)==2
    def test_case_two(self):
        assert Solution().maxKDivisibleComponents(7,[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]],[3,0,6,1,5,2,1],3)==3