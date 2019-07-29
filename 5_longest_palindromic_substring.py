#最长回文字符串
class Solution:
    def longsetPalindrome(self,s:"str")->"str":
        #对称的两种形式 bb 或者bab
        palindrome=”“
        for i in range(len(s)):
            len1=len(self.getlgetlongestPalidrome(s,i,i))
            if len1>len(palindrome):
                palindrome=self.getlgetlongestPalidrome(s,i,i)
            len2=len(self.getlongestPalidrome(s,i,i+1))
            if len2>len(palindrome):
                palindrome=self.getlgetlongestPalidrome(s,i,i+1)
    
    def getlongestPalidrome(self,s,left,right):
        while s[left]==s[right] and left>0 and right<len(s) :
            left-=1
            right+=1
        return s[left+1:right]