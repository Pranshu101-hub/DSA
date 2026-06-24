class Solution:
    def maxDistinct(self, s: str) -> int:
        l = []
        ss = set()
        j = 1
        for i in range(len(s)):
            if s[i] not in ss:
                ss.add(s[i])
                l.append(s[i:j])
                j = i+1
            #print(l,ss,j,i)
        return len(l)

