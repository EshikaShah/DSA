from collections import OrderedDict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = OrderedDict()
        count = {}
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = i
                count[s[i]] = 1
            else:
                count[s[i]] += 1
        if d:
            for key in d:
                if(count[key] == 1):
                    return d[key]
        return -1