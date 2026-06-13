class Solution(object):
    def reverse(self, x):
        flag = False
        rev = 0

        if x < 0:
            x = -x
            flag = True

        while x > 0:
            last = x % 10
            rev = rev * 10 + last
            x = x // 10

        if flag:
            rev = -rev
        if rev < -2**31 or rev > 2**31 - 1:
            return 0

        return rev