class Solution:
    def minOperations(self, nums: list[int]) -> int:
        count=0
        stack=[-1]
        for i in range(len(nums)):
            num=nums[i]
            while num<stack[-1]: stack.pop()
            if num>stack[-1]:
                count+=num>0
                stack.append(num)
        return count
class TestApp:
    def test_case_one(self):
        assert Solution().minOperations([0,2])==1
    def test_casE_two(self):
        assert Solution().minOperations([3,1,2,1])==3
    def test_case_three(self):
        assert Solution().minOperations([1,2,1,2,1,2])==4
    def test_case_four(self):
        assert Solution().minOperations([5,1,4,3,2,2,1,1,7])==6
    def test_case_five(self):
        assert Solution().minOperations([1,4,4,6])==3
        
