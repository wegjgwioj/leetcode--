import math
if __name__ == "__main__":
    nums=[0 ,1, 0 ,3 ,2, 3]
    l=len(nums)
    dp=[1]*l
    for i in range(l):
        for j in range(i):
            if nums[i]>nums[j]:
                dp[i] = max(dp[i],dp[j]+1)
    print(max(dp))

 
       
    

    

