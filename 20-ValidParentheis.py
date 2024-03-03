class Solution:
    def isValid(self, s: str) -> bool:
        c=len(s)
        i=0
        j=1
        b=True
        while c>0:
            if s[i]=="(":
                if s[j]==")":
                    b=True
                else:
                    return False
            if s[i]=="[":
                if s[j]=="]":
                    b=True
                else:
                    return False
            if s[i]=="{":
                if s[j]=="}":
                    b=True
                else:
                    return False
            
            i+=2
            j+=2
            c-=2
        return True
    
