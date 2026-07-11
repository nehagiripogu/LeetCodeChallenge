class Solution:
    def palin(self, s, left, right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
    def validPalindrome(self, s):
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return (
                    self.palin(s, left + 1, right) or
                    self.palin(s, left, right - 1)
                )

        return True