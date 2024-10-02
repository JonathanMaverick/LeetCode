class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_list = sorted(score, reverse = True)
        res = ["0"] * len(score)
        for i in range(len(score)):
            temp = sorted_list.index(score[i]) + 1
            if temp == 1:
                res[i] = "Gold Medal"
            elif temp == 2:
                res[i] = "Silver Medal"
            elif temp == 3: 
                res[i] = "Bronze Medal"
            else :
                res[i] = str(temp)
        
        return res
            
                