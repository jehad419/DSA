class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Solved by Jehad Hasan
        if x < 0:
            return False
        elif x == 0:
            return True
        elif x > 0:
            num = x
            result = 0
            while num > 0:
                ld = num % 10
                result = (result * 10) + ld
                num = num // 10
            return result == x
        