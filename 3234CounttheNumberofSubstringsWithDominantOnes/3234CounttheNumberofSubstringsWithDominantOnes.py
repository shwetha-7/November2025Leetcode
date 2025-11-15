class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n,count=len(s),0
        total=0
        for i in range(n):
            count_zeros=count_ones=0
            for j in range(i,n):
                if s[j]=='0':
                    count_zeros+=1
                else:
                    count_ones+=1
                total+=1
                if count_ones>=count_zeros**2:
                    count+=1
        return count 
import math
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n=len(s)
        prefix_sum=[0]*n 
        prefix_sum[0]=1 if s[0]=='1' else 0 
        for i in range(1,n):
            prefix_sum[i]=prefix_sum[i-1]+ 1 if s[i]=='1' else 0 
        ans=0 
        for i in range(n):
            for j in range(i,n):
                ones=prefix_sum[j]-(prefix_sum[i-1] if i>0 else 0)
                zeros=(j-i+1)-ones 
                if zeros**2>ones:
                    wasteIndex=(zeros**2)-ones 
                    j+=wasteIndex-1
                elif (zeros**2)==ones:
                    ans+=1
                else:
                    ans+=1
                    k=int(math.sqrt(ones))-zeros 
                    next_j=j+k 
                    if next_j>=n:
                        ans+=(n-j-1) 
                        break 
                    else:
                        ans+=k 
                    j=next_j
        return ans
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        pre = [-1] * (n + 1)
        for i in range(n):
            if i == 0 or s[i - 1] == "0":
                pre[i + 1] = i
            else:
                pre[i + 1] = pre[i]

        res = 0
        for i in range(1, n + 1):
            cnt0 = 1 if s[i - 1] == "0" else 0
            j = i
            while j > 0 and cnt0 * cnt0 <= n:
                cnt1 = (i - pre[j]) - cnt0
                if cnt0 * cnt0 <= cnt1:
                    res += min(j - pre[j], cnt1 - cnt0 * cnt0 + 1)
                j = pre[j]
                cnt0 += 1
        return res
class TestApp:
    def test_case_one(self):
        assert Solution().numberOfSubstrings("00011")==5
    def test_case_two(self):
        assert Solution().numberOfSubstrings("101101")==16