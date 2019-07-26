#验证输入是不是能被完全开根号
class Solution:
    def isPerfectSquare(self,num:int) ->bool:
        if num==1:
            return True
        left,right=0,num
        while left<=right:
            mid=left+(right-left)//2
            if mid>num/mid:
                right=mid-1
            elif mid==num/mid:
                retun True
            else:
                left=mid+1
        return left==num//left and num%left==0