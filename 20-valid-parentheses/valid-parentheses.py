class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in range(len(s)):
            if s[i] in "[{(":
                st.append(s[i])
            elif st == []: return False
            else:
                if st[-1] == "[" and s[i] == "]":
                    st.pop()
                elif st[-1] == "(" and s[i] == ")":
                    st.pop()
                elif st[-1] == "{" and s[i] == "}":
                    st.pop()
                else:
                    return False
        if st == []: return True
        return False