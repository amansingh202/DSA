## Leetcode 860. Lemonade Change

class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:


        five = 0
        ten = 0

        n = len(bills)

        for i in range(n):

            if bills[i] == 5:
                five += 1

            elif bills[i] == 10:
                if five:
                    five -= 1
                    ten += 1
                else:
                    return False
            
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five >= 3:
                    five -= 3
                else:
                    return False
                
        return True
    
obj = Solution()

bills = [5,5,10,10,20]

print(obj.lemonadeChange(bills))