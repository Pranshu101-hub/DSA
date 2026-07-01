class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        st = set()
        for i in nums:
            if i not in st:
                st.add(i)
            else:
                st.remove(i)
        return list(st)