class Solution:
    def __init__(self):
        self.max_sum_value=0
        
    def maxSumDivThree(self, nums: list[int]) -> int:
        self.helper(0,len(nums),0,nums)
        return self.max_sum_value
    def helper(self,index:int,n:int,sum_value:int,nums:list[int]):
        if index==n:
            if sum_value%3==0:
                self.max_sum_value=max(self.max_sum_value,sum_value)
            return 
        self.helper(index+1,n,sum_value+nums[index],nums)
        self.helper(index+1,n,sum_value,nums)
class Solution:
    def maxSumDivThree(self, nums: list[int]) -> int:
        dp=[0,-float('inf'),-float('inf')]
        for num in nums:
            dummy=dp[:]
            for j in range(3):
                index=(j+num%3)%3 
                dummy[index]=max(dummy[index],dp[j]+num) 
            dp=dummy     
        return dp[0]   

class TestApp:
    def test_case_one(self):
        assert Solution().maxSumDivThree([3,6,5,1,8])==18
    def test_case_two(self):
        assert Solution().maxSumDivThree([4])==0
    def test_case_three(self):
        assert Solution().maxSumDivThree([1,2,3,4,4])==12
    