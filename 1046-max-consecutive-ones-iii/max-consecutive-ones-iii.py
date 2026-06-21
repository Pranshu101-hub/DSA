class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start,end,maxx,store = 0,0,0,0

        while end<len(nums):
            #print(start,end,k,store,maxx)
            if nums[end] == 1:
                store += 1
                end += 1
            else:
                if k>0:
                    k -= 1
                    store += 1
                    end += 1
                else:
                    store -= 1
                    if nums[start] == 1:
                        pass
                    else:
                        k += 1
                    start += 1
            maxx = max(maxx,store)
            #print(start,end,k,store,maxx)
            #print("-"*10)
        return maxx
