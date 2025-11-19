class Solution:
    def isOneBitCharacter(self, bits: list[int]) -> bool:
        index=0
        while index<len(bits)-1:
              if bits[index]==1:
                  index+=2
              else:
                  index+=1
        return index!=len(bits)
        
class TestApp:
    def test_case_one(self):
        assert Solution().isOneBitCharacter([1,0,0])==True  
    def test_case_two(self):
        assert Solution().isOneBitCharacter([1,1,1,0])==False
    def test_case_three(self):
        assert Solution().isOneBitCharacter([0])==True 
    def test_case_four(self):
        assert Solution().isOneBitCharacter([0,0,0])==True
