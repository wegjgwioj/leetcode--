'''
用快慢指针，r 扫描数组，遇到非零就把它放到 l，然后 l 前进；这样非零元素按原顺序被依次搬到前面，剩下的位置自然变成 0。
'''
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        l=0
        for  r in range(len(nums)):
            if nums[r] != 0 :
                if l!=r:
                    nums[l]=nums[r]
                    nums[r]=0
                l+=1   

            
            