class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        for i in range(len(s)):
            l.append(s[i])
            if s[i]==")":
                if i==0:
                    return False
                elif i>0 and l[l.index(s[i])-1] != "(":
                    return False
                else:
                    l.pop()
                    l.pop()
            elif s[i]=="]":
                if i==0:
                    return False
                elif i>0 and l[l.index(s[i])-1] != "[":
                    return False
                else:
                    l.pop()
                    l.pop()
            elif s[i]=="}":
                if i==0:
                    return False
                elif i>0 and l[l.index(s[i])-1] != "{":
                    return False
                else:
                    l.pop()
                    l.pop()
        if l:
            return False
        else:
            return True
