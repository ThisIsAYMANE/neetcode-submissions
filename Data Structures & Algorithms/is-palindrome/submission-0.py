class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1 = list(s.lower())
        str1 = [x for x in str1 if x.isalnum()]
        rev = []

        for x in range(len(str1) - 1, -1, -1):
            rev.append(str1[x])

        for y in range(len(str1)):
            if rev[y] != str1[y]:
                return False

        return True