class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for i in tokens:
            if i.isdigit() or (i.startswith('-') and i[1:].isdigit()):
                st.append(int(i))
            else:
                if i == '+':
                    s = st[-1] + st[-2]
                    st.pop()
                    st.pop()
                    st.append(s)
                elif i=='-':
                    s = st[-2] - st[-1]
                    st.pop()
                    st.pop()
                    st.append(s)
                elif i=='*':
                    s = st[-1] * st[-2]
                    st.pop()
                    st.pop()
                    st.append(s)
                else: 
                    s = int(st[-2]/st[-1])
                    st.pop()
                    st.pop()
                    st.append(s)
            #print(st)
        return st[-1]