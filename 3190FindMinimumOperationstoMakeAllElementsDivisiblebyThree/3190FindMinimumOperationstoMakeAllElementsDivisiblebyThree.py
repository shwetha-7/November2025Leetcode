class Solution:
    def minimumOperations(self, nums: list[int]) -> int:
        count=0
        for num in nums:
            if num%3: count+=1
        return count  
class TestApp:
    def test_case_one(self):
        assert Solution().minimumOperations([1,2,3,4])==3
    def test_case_two(self):
        assert Solution().minimumOperations([3,6,9])==0
    def test_case_three(self):
        assert Solution().minimumOperations([12,3,4,5])==2