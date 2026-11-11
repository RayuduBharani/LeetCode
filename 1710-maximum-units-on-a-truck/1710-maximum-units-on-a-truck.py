import math
class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key = lambda x : x[1])
        boxTypes = boxTypes[::-1]
        ans = 0
        for i , j in boxTypes :
            if (truckSize <= 0) :
                return ans
            elif (i <= truckSize) :
                ans += (i * j)
                truckSize -= i
                print(i , "i")
            else:
                ans += ((truckSize) * j)
                print(i , "i2")
                print(truckSize)
                truckSize -= (truckSize)
        
        return ans