"""
LeetCode 3. 无重复字符的最长子串

题目:
给定一个字符串 `s` ，请你找出其中不含有重复字符的最长子串的长度。

示例 1:
输入: s = "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是子串的长度，"pwke" 是一个子序列，不是子串。

提示:
0 <= s.length <= 5 * 10^4
s 由英文字母、数字、符号和空格组成。
"""


def subString(s:str)-> int:
    seen=[]
    l=0
    ans=0
    for r, ch in enumerate(s):
        # 如果 ch 已经在窗口里，就移动 l 缩窗
       
        while ch in seen:
            
            l += 1
            
        # 把当前字符放进窗口
        seen.append(ch)
        
        # 更新答案
        ans = max(ans, r - l + 1)

    return ans
   

        
        
        



# ans = [1,2,6,3,5,4,7]
# temp={}
# for i in ans:
#     print(i)
#     if i% 2 != 0:
#         temp[i]='test'



# ans.sort(reverse=True)
# for Index,key in temp.items():

#     print(f"{Index}:'{key}'")

# print(ans)
    