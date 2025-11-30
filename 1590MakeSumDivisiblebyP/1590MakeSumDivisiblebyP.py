class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        target=sum(nums)%p 
        if not target: return 0
        current_sum=0
        map={0:-1}
        n=len(nums)
        min_len=float('inf')
        for i in range(n):
            current_sum=(current_sum+nums[i])%p 
            needed=(current_sum-target+p)%p 
            if needed in map:
                min_len=min(min_len,i-map[needed])
            map[current_sum]=i
        return min_len if min_len<n else -1 
class TestApp:
    def test_case_one(self):
        assert Solution().minSubarray([3,1,4,2],6)==1
    def test_case_two(self):
        assert Solution().minSubarray([6,3,5,2],9)==2
    def test_case_three(self):
        assert Solution().minSubarray([1,2,3],3)==0
