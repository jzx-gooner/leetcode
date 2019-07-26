#找字符中第一个非重复的数的索引 
class Solution:
    def firstUniqChar(self,s:str)->int:
        # method1
        # from collections import Counter
        # lookup=Counter(s)
        # method2 
        lookup=dict()
        for i in s:
            if i in lookup:
                lookup[i]+=1
            else:
                lookup[i]=1
        for i,c in enumerate(s):
            if lookup[c]==1:
                return i
        return -1