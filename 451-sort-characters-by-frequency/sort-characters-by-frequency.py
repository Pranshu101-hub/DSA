class Solution:
    def frequencySort(self, s: str) -> str:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        print(d)
        val = []
        for i in d:
            val.append((i,d[i]))
        val.sort(key=lambda x: x[1], reverse=True)
        print(val)
        st = ""
        for i in val:
            st = st + i[0]*i[1]
        return st
