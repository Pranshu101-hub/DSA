class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        st = ''
        maxi = 0
        for i in range(1,n):
            #print(s[:i],s[n-i:n])
            if s[:i] == s[n-i:n]:
                if maxi < i+1:
                    st = s[:i]
                    maxi = i+1
        return st