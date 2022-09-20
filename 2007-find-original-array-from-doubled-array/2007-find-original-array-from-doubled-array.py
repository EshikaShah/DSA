from collections import Counter
class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if(len(changed)%2!=0):
            return []
        l = []
        d = Counter(changed)
        changed.sort(reverse = True)
        for num in changed:
            if(num%2==0 and d[num]!=0 and d[num//2]!=0):
                if(num == 0):
                    if(d[num]%2 == 0):
                        d[num] -= 1
                        d[num//2] -= 1
                        l.append(num//2)
                else:
                    d[num] -= 1
                    d[num//2] -= 1
                    l.append(num//2)
        if(sum(d.values())==0):
            return l
        return []