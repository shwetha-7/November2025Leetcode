
# Wrong Solution 

class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        queue=[[bin(n)[2::],0]]
        visited={queue[0][0]:1}
        min_steps=float('inf')
        while queue:
              curr=queue.pop()
              print(curr)
            #   check if was 0 
              if self.convertBinaryToNumber(curr[0])==0:
                 min_steps=min(min_steps,curr[1])
                 continue 
            #   perform operation one 
              res_1=self.operation_1(curr[0])
              print("Result 1 : ",res_1)                         
              if res_1 not in visited:
                  visited[res_1]=1
                  queue.append([res_1,curr[1]+1])
            # perform operation two 
              res_2=self.operation_2(curr[0])
              print("Result 2: ",res_2)
              if res_2 not in visited:
                  visited[res_2]=1
                  queue.append([res_2,curr[1]+1])
                  
        return min_steps
    def operation_2(self,value:str):
        if len(value)>1:
            value=list(value)
            for i in range(1,len(value)):
                if value[i]=="1" and value[i-1]=="1":
                    value[i-1]="0"
                    break 
        return "".join(value)
            
    def operation_1(self,value:str):
        last=0 if int(value[-1]) else 1
        n=len(value)
        return value[:n-1:]+str(last)
    def convertBinaryToNumber(self,value:str):
        n,number,pow=len(value),0,0
        for i in range(n-1,-1,-1):
            number+=int(value[i])*(2**pow)
            pow+=1
        return number   
class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        ans=n
        ans^=ans>>16
        ans^=ans>>8
        ans^=ans>>4
        ans^=ans>>2
        ans^=ans>>1
        return ans
        
        
           
class TestApp:
    def test_case_one(self):
        assert Solution().minimumOneBitOperations(3)==2
    def test_case_two(self):
        assert Solution().minimumOneBitOperations(6)==4
