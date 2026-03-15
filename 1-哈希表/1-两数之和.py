from typing import List
def findtraget(nums:List[int],target: int)->List[int]:
    seen = {}
    for index,key in enumerate(nums):
        need = target - key
        if need in seen:
            return [seen[need],index]
        seen[key] = index

    return []

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    
    print(findtraget(nums,target))
       
     