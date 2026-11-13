class Solution:
    def isValid(self, s: str) -> bool:

        p = {'}':'{',')':'(',']':'['}

        r = []

        for st in s:

            if st in p:
                if r and r[-1]==p[st]:
                    r.pop()
                else:
                    return False
            else:
                r.append(st)
        
        return not r


        