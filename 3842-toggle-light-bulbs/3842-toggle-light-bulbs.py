class Solution(object):
    def toggleLightBulbs(self, bulbs):
        """
        :type bulbs: List[int]
        :rtype: List[int]
        """
        arr=bulbs
        seen=set()
        for i in range(len(bulbs)):
            if arr[i] in seen:
                seen.remove(arr[i])
            else:
                seen.add(arr[i])
        return sorted(list(seen))
