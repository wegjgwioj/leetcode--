'''
给定整数数组 nums，找出所有和为 0 且不重复的三元组。

先排序的原因：
    双指针移动规则
    去重规则


'''

class Solutions:
    def sumThreeNumbers(self, nums:list[int])->list[list[int]]:
        ans =[]
        if not nums:
            return []
        nums.sort()
        
        
        return ans