class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = [0] * 26

        for ch in s:
            idx = ord(ch) - ord('a')
            table[idx] += 1

        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            if table[idx] == 1:
                return i

        return -1