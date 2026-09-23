class Solution:
    def reverse(self, x: int) -> int:
        #Solved by Jehad Hasan
        if x < 0:
            sign = -1
        else:
            sign = 1
        num = abs(x)
        result = 0
        while num > 0:
            ld = num % 10
            result = (result * 10) + ld
            num = num // 10
        result = result * sign

        if result < -2147483648 or result > 2147483647:
            return 0

        return result
        
      