class solution:
    def intersection( self,nums1: list[int], nums2: list[int]) -> list[int]:
        ans=[]
        n1 =set(nums1)
        n2 =set(nums2)
        for key in n1:
            if key in n2 :
                ans.append(key)
    
        return ans


if __name__ == "__main__":
    print(solution().intersection([1,2,2,1],[2,2]))