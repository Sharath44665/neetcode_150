class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # time: o(N), space: o(1)
        # [14,15,7,2,5,3,6,4,13,1,5]
        # [7,1,5,3,6,4]
        idx = 0
        currentMax = prices[0]
        currentMin = prices[0]
        maxDiff = 0
        currentDiff  = 0
        while idx < len(prices)-1:
            if prices[idx+1] > prices[idx]:
                currentMax = prices[idx+1]

            if prices[idx] < currentMin:
                currentMin = prices[idx]
            

            if prices[idx+1] > prices[idx]:
                currentDiff = currentMax - currentMin
            if currentMin < currentMax and currentDiff > maxDiff:
                maxDiff = currentDiff

            idx += 1
        return maxDiff
        

class SolutionFirst:
    def maxProfit(self, prices: List[int]) -> int:
        # time: o(N^2), space: o(1)
        firstIdx = 0
        lastIdx = len(prices) -1
        maxDiff = 0
        while firstIdx < lastIdx:
            # if prices[firstIdx] > prices[lastIdx]:
            #     lastIdx -= 1
            #     continue
            while lastIdx > firstIdx:
                currentDiff = prices[lastIdx] - prices[firstIdx]
                if currentDiff > maxDiff:
                    maxDiff = currentDiff
                lastIdx -= 1
            lastIdx = len(prices) -1 
            firstIdx += 1

        return maxDiff
        
        