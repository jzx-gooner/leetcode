#递归
class Solution:
    def permute(self,num):
        if len(nums)<=1:
            return [nums]
        answer=[]
        for i,num in enumerate(nums):
            n=nums[:i]+nums[i+1:]
            for y in self.permute(n):
                answer.append([num]+y)
        return answer