"""You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record."""

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
