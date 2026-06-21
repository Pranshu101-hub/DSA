class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if s == [] or g == []: return 0
        tot = 0
        g = sorted(g)
        s = sorted(s)
        gp,sp = 0,0
        while gp < len(g):
            if g[gp] <= s[sp]:
                gp+=1
                sp+=1
                tot += 1
            else:
                sp+=1
            if sp == len(s): return tot
            print(gp,sp,tot)
        return tot