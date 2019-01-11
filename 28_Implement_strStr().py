
class Solution():
    def strStr(self,str1,str2):
        """
        :param str1:str
        :param str2: str
        :return: int
        """
        for i in range(len(str1)-len(str2)+1):
            if str1[i:i+len(str2)]==str2:
                return i
        return -1

if __name__ == '__main__':
    print(Solution().strStr("hello", "lo"))
    print(Solution().strStr("helllo","lllo"))