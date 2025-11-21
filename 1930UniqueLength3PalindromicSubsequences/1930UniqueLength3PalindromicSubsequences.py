# Recursion 
# TC : O(2^N)
# SC : O(N)

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        res=set()
        self.helper([],0,len(s),list(s),res)
        return len(res)
    def helper(self,stack:list[str],index:int,n:int,arr:list[str],res:set):
        if index==n:
           if len(stack)==3:
               temp="".join(stack)
               if temp==temp[::-1]:
                   res.add(temp)
           return 
        stack.append(arr[index])
        self.helper(stack,index+1,n,arr,res)
        stack.pop()
        self.helper(stack,index+1,n,arr,res)
        
#  Optimal Approach 
# By taking sum of first and last occurrences of the current character & count the number of palindrome can be formed 
# since the size of the palindrome string is 3 
# We just need to find the first an last occurrences of the character & in the middle we can place any character 
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        temp=set(s)
        count=0 
        for ch in temp:
            count = count+len(set(s[s.index(ch)+1:s.rindex(ch)]))
        return count
    
class TestApp:
    def test_case_one(self):
        assert Solution().countPalindromicSubsequence("aabca")==3 
    def test_case_two(self):
        assert Solution().countPalindromicSubsequence("adc")==0
    def test_case_three(self):
        assert Solution().countPalindromicSubsequence("bbcbaba")==4
              
          