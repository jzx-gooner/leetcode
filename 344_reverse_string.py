#反转字符串
#空间复杂度，不再另外开辟空间
class Solutuin:
    def reverseString(self,s:list[str]) -> None:
        for i in range(len(s)//2):
            s[i],s[-i-1]=s[-i-1],s[i]

