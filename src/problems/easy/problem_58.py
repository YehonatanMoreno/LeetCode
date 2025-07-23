class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        i, n = 0, len(s)
        while i < n and s[n - 1 - i] != " ":
            i += 1
        return i
