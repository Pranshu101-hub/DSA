class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t): return ""
        
        count = defaultdict(int)
        for i in t:
            count[i] += 1
        
        t = len(t)
        min = (0, float("inf"))
        start = 0

        for end, i in enumerate(s):
            if count[i] > 0:
                t -= 1
            count[i] -= 1

            if t == 0:
                while True:
                    char_at_start = s[start]
                    if count[char_at_start] == 0:
                        break
                    count[char_at_start] += 1
                    start += 1
                
                if end - start < min[1] - min[0]:
                    min = (start, end)
                
                count[s[start]] += 1
                t += 1
                start += 1
        
        return "" if min[1] > len(s) else s[min[0]:min[1]+1]