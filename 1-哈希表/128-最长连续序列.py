
class Sloutions:
    def maxSublsit1(self,nums: list[int] ) -> int:
        if not nums:
            return 0
        temps=sorted(set(nums)) # 怎么去重？
        ans = 1
        curlen=1
        '''
        for prev, cur in zip(temps, temps[1:]):
            if cur - prev == 1:
            ...
        '''

        '''
        for i in range(1, len(temps)):
            if temps[i] - temps[i - 1] == 1:
            ...
        '''
        for index,key in enumerate(temps[1:],start=1):
            if   key - temps[index-1] == 1 :
                curlen +=1
            else:
                curlen =1
            ans= max(curlen,ans)
        return ans    
    '''
    1,2,3,4,100,200
    '''

    def maxSublsit2(self,nums: list[int] ) -> int:
        numset = set(nums)
        maxlen = 0
        for _,key in enumerate(numset):
            if key-1 not in numset:
                cur = key 
                curlen =1

                while cur+1 in numset:
                    cur +=1
                    curlen +=1
                
                maxlen = max(maxlen,curlen)
        return maxlen

if  __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    print(Sloutions().maxSublsit1(nums))
    print("\n")
    print(Sloutions().maxSublsit2(nums))