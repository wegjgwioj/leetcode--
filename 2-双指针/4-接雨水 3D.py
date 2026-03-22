'''
“给定柱状图高度数组 height，返回下雨后能接到的雨水总量。”



'''


'''

“某一个位置能接多少水”？
单个位置的水量由什么决定


'''

def water(height:list[int])->int:
        ans =0 
        l, r = 0, len(height) - 1
        left_max, right_max = 0, 0
        

        while l < r:
            if left_max < right_max:
                
                ans=ans+left_max-height[l]

            else:
                ans=ans+right_max-height[r]

        return ans