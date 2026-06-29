class Solution:
    def numOfStrings(self, pattern, word):
        count = 0
        for s in pattern:
            if word.find(s) != -1: # return -1 when not found
                count += 1
        return count