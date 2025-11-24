class Solution:
    def prefixesDivBy5(self, nums: list[int]) -> list[bool]:
        ans=[]
        val=0
        for i in range(len(nums)):
            val=(val*2+nums[i])%5 
            ans.append(val==0)
        return ans
class TestApp:
    def test_case_one(self):
        assert Solution().prefixesDivBy5([0,1,1])==[True,False,False]
    def test_case_two(self):
        assert Solution().prefixesDivBy5([1,1,1])==[False,False,False]
    def test_case_three(self):
        assert Solution().prefixesDivBy5([1,1,0,0,0,1,0,0,1])==[False,False,False,False,False,False,False,False,False]
