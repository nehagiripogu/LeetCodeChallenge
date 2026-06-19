class Solution:
    def largestAltitude(self, gain):
        ans = acc = 0

        for it in gain:
            acc += it
            d = acc - ans
            ans += d & ~(d >> 0x1F)

        return ans