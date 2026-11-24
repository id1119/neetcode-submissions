class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        i, j = 0 , len(s)-1
        if len(s) <= 1:
            return True
        while i <=j:
            if '0'<=s[i]<='9' or 'a'<=s[i]<='z':
                if '0'<=s[j]<='9' or 'a'<=s[j]<='z':
                    if s[i] == s[j]:
                        i+=1
                        j-=1
                    else:
                        return False
                else:
                    j-=1
            else:
                i+=1
        return True