class Solution():
    def twoSum(self,nums,target):
        """
        :param nums:list[int]
        :param target: int
        :return: list[int]
        """
        for i in nums:
            j=target-i
            tmp_nums_start_index=nums.index(i)+1
            tmp_nums=nums[tmp_nums_start_index:]
            if j in tmp_nums:
                return[nums.index(i),tmp_nums_start_index+tmp_nums.index(j)]

if __name__ == '__main__':
    print(Solution().twoSum((2, 7, 11, 15), 9))