class Solution:
    def checkRecord(self, s: str) -> bool:
        acount=0
        lcount=0
        for i in s:
            if(i=='A'):
                acount+=1
                if(acount>1):
                    return False
                lcount=0
            if(i=='L'):
                lcount+=1
                if(lcount>2):
                    return False
            else:
                lcount=0
        return True
