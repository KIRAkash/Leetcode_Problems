"""Your friend is typing his name into a keyboard.  Sometimes, when typing a character c, the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your friends name, with some characters (possibly none) being long pressed.

 

Example 1:

Input: name = "alex", typed = "aaleex"
Output: true
Explanation: 'a' and 'e' in 'alex' were long pressed."""
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        last=""
        for i in name:
            if(len(typed)==0):
                return False
            if(typed[0]==i):
                typed=typed[1:]
                last=i
            elif(typed[0]==last):
                while(len(typed)>0 and typed[0]==last):
                    typed=typed[1:]
                if(len(typed)>0 and typed[0]==i):
                    typed=typed[1:]
                    last=i
                else:
                    return False
            else:
                return False
        while(len(typed)>0 and typed[0]==last):
            typed=typed[1:]
        if(len(typed)==0):
            return True
        else:
            return False
