'''
给定整数数组 nums，找出所有和为 0 且不重复的三元组。

先排序的原因：
    双指针移动规则
    去重规则


'''

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            # 1. i 去重
            if i>0 and nums[i] == nums[i-1]:
                continue
            # 2. 定义 l, r
            l,r =i+1,len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]

                if s < 0:
                    l+=1
                elif s > 0:
                    r-=1
                else:
                    ans.append([nums[i], nums[l], nums[r]])

                    # 3. l 去重
                    while l<r and nums[l]==nums[l+1]: l+=1
                    # 4. r 去重
                    while l<r and nums[r]==nums[r-1]: r-=1

                    # 5. 再收缩
                    l+=1
                    r-=1

        return ans
