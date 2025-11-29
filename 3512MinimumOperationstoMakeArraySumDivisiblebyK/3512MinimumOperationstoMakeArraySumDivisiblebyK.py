class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        return sum(nums)%k 


class TestApp:
    def test_case_one(self):
        assert Solution().minOperations([3,9,7],5)==4
    def test_case_two(self):
        assert Solution().minOperations([4,1,3],4)==0
    def test_case_three(self):
        assert Solution().minOperations([3,2],6)==5