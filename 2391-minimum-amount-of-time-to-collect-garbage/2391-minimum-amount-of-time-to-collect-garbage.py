class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        s = 0
        for i in range(len(garbage)):
            if(i != 0):
                s += travel[i-1]
            if('P' in garbage[i]):
                s += garbage[i].count("P")
        for i in range(len(garbage)-1, 0, -1):
            if('P' not in garbage[i]):
                s -= travel[i-1]
            else:
                break
        for i in range(len(garbage)):
            if(i != 0):
                s += travel[i-1]
            if('G' in garbage[i]):
                s += garbage[i].count("G")
        for i in range(len(garbage)-1, 0, -1):
            if('G' not in garbage[i]):
                s -= travel[i-1]
            else:
                break
        for i in range(len(garbage)):
            if('M' in garbage[i]):
                s += garbage[i].count("M")
            if(i != 0):
                s += travel[i-1]
        for i in range(len(garbage)-1, 0, -1):
            if('M' not in garbage[i]):
                s -= travel[i-1]
            else:
                break
        return s