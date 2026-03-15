from typing import List
class Solution:
    def groupAna(self,strs:List[str])-> List[List[str]]:
        ans={}
        for _,key in enumerate(strs):
            sorted_word =''.join(sorted(key))
            if sorted_word in ans:
                ans[sorted_word].append(key)
            else:
                ans[sorted_word] = [key]

        return list(ans.values())

if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution().groupAna(strs))

'''
sorted_word = ''.join(sorted(key))
key = "eat"
sorted(key)
['a', 'e', 't']
''.join(['a', 'e', 't'])
"aet"
'-'.join(['a', 'e', 't'])
"a-e-t"
'''