class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        st = []
        res = []
        for i in nums2:
            if st == [] or i<st[-1]: st.append(i)
            else:
                while st!=[] and st[-1] < i :
                    d[st.pop()] = i
                    #print(d)

                st.append(i)
            #print(st)

        #print(d)
        for i in nums1:
            if i not in d:
                res.append(-1)
            else: res.append(d[i])
        return res