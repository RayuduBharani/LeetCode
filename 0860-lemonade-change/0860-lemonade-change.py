class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        fives = 0
        tens = 0
        for i in range(len(bills)) :
            if (bills[i] == 5) :
                fives += 1
            
            elif (bills[i] == 10 and fives >= 1) :
                fives -= 1
                tens += 1
            elif (bills[i] == 10 and fives < 1) :
                return False
            
            elif (bills[i] == 20) :
                if (tens >= 1 and fives >= 1) :
                    fives -= 1
                    tens -= 1
                elif (fives >= 3) :
                    fives -= 3

                else :
                    return False
            print(fives , tens , bills[i])
        return True