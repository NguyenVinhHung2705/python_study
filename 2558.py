import math

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        sum_of_list = sum(gifts)
        gifts = sorted(gifts,reverse= True)
        if gifts[0] == 1:
            return sum_of_list
        while k > 0:
            tmp = gifts[0]
            gifts[0] = int(math.sqrt(gifts[0]))
            sum_of_list = sum_of_list - (tmp - gifts[0])
            tmp = gifts[0]
            i = 1
            while tmp < gifts[i]:
                gifts[i - 1] = gifts[i]
                i+=1
                if i == len(gifts):
                    break
            gifts[i - 1] = tmp
            k -= 1
        return sum_of_list

x = Solution()
print(x.pickGifts([70,58,12,11,41,66,63,14,39,71],19))