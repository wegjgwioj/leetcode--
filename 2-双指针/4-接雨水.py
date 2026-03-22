'''
“给定柱状图高度数组 height，返回下雨后能接到的雨水总量。”



'''


'''

“某一个位置能接多少水”？
单个位置的水量由什么决定


'''

def water(height:list[int])->int:
        ans =0 
        n =len(height)
        pre_max=[0]*n
        pre_max[0] = height[0]
        for i in range(1,n):
                pre_max[i] = max(pre_max[i-1],height[i])

        suf_max = [0]*n
        suf_max[-1] = height[-1]
        for i in range(n-2,-1,-1):
                suf_max[i] = max(suf_max[i+1],height[i])

        for h,pre,suf in zip(height,suf_max,pre_max):
                ans += min(pre,suf)-h
            

        return ans