'''
给定数组 height，选择两条线与 x 轴组成容器，返回可盛水的最大面积。
min(height[i], height[j]) * (j - i)

'''

def maxarea(height:list[int])->int:
    if not height:
          return 0
    l, r =0,len(height)-1
    ans = 0
    while l<r:
        area = min(height[r], height[l]) * (r - l)
        ans = max(ans,area)
        if height[l]< height[r]:
                l+=1
        else:
                r-=1

    return ans