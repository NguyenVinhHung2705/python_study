class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        tmp = x
        palindrome_num = 0
        while x != 0:
            palindrome_num = (palindrome_num * 10) + (x % 10)
            x //= 10
        if palindrome_num == tmp:
            return True
        return False 