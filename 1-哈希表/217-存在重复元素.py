class Solution:
    def containsDuplicate(self,nums:list[int])->bool:
        temps = nums
        temps = set(temps)
        if len(temps) == len(nums):
            return False
        return True
    

if __name__ == "__main__":
    nums = [ 1,2,3,1,4]
    print(Solution().containsDuplicate(nums))
    print(Solution().containsDuplicate([1,2,3,4]))
    print(Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]))