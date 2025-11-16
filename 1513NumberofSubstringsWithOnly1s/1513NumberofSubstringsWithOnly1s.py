class Solution:
    def numSub(self, s: str) -> int:
        total=ans=0
        for i in range(len(s)):
            if s[i]=='0':
                ans+=(total*(total+1)//2)%(10**9+7)
                total=0
            else:
                total+=1
        ans+=(total*(total+1)//2)%(10**9+7)
        return ans 
class TestApp:
    def test_case_one(self):
        assert Solution().numSub("0110111")==9
    def test_case_two(self):
        assert Solution().numSub("00011")==3
    def test_case_three(self):
        assert Solution().numSub("111111")==21
    def test_case_four(self):
        assert Solution().numSub("101")==2