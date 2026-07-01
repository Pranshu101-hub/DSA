class Solution:
    def candy(self, arr: List[int]) -> int:
        ca = [1]*len(arr)
        for i in range(1,len(arr)):
            if arr[i] > arr[i-1]:
                ca[i] = ca[i-1]+1
        
        for i in range(len(arr)-1,0,-1):
            if arr[i] < arr[i-1]:
                ca[i-1] = max(ca[i-1], ca[i]+1)
        return sum(ca)