#
# @lc app=leetcode id=67 lang=python
#
# [67] Add Binary
#

# @lc code=start
class Solution(object):
    def addBinary(self, a, b):
        if min(len(a), len(b)) == 0:
            return(max(a, b))
        else:
            i, j = len(a)-1, len(b)-1
            s = ""
            c = 0
            while max(i, j) >= 0 or c == 1:
                if c == 0:
                    if i < 0 and j >= 0:
                        s = str(b[j]) + s
                        c = 0
                    elif j < 0 and i >= 0:
                        s = str(a[i]) + s
                        c = 0
                    elif i >= 0 and j >= 0:
                        if a[i] == "0" and b[j] == "0":
                            s = "0" + s
                            c = 0
                        elif a[i] == "1" and b[j] == "1":
                            s = "0" + s
                            c = 1
                        else:
                            s = "1" + s
                            c = 0
                elif c == 1:
                    if i < 0 and j >= 0:
                        if b[j] == "0":
                            s = "1" + s
                            c = 0
                        else:
                            s = "0" + s
                            c = 1
                    elif j < 0 and i >= 0:
                        if a[i] == "0":
                            s = "1" + s
                            c = 0
                        else:
                            s = "0" + s
                            c = 1
                    elif i < 0 and j < 0:
                        s = "1" + s
                        c = 0
                    elif i >= 0 and j >= 0:
                        if a[i] == "0" and b[j] == "0":
                            s = "1" + s
                            c = 0
                        elif a[i] == "1" and b[j] == "1":
                            s = "1" + s
                            c = 1
                        else:
                            s = "0" + s
                            c = 1
                
                i -= 1
                j -= 1
                
            return(s)
        
# @lc code=end

