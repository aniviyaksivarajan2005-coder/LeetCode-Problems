class Manacher:
    def __init__(self, s):
        # Modified string
        self.ms = "@"
        for ch in s:
            self.ms += "#" + ch
        self.ms += "#$"

        self.p = [0] * len(self.ms)
        self.run_manacher()

    def run_manacher(self):
        n = len(self.ms)
        left = right = 0

        for i in range(1, n - 1):

            if i < right:
                self.p[i] = min(right - i, self.p[left + right - i])

            while self.ms[i + self.p[i] + 1] == self.ms[i - self.p[i] - 1]:
                self.p[i] += 1

            if i + self.p[i] > right:
                left = i - self.p[i]
                right = i + self.p[i]

    def getLongest(self, center, odd):
        pos = 2 * center + 2 + (0 if odd else 1)
        return self.p[pos]

    def check(self, l, r):
        length = r - l + 1
        longest = self.getLongest((l + r) // 2, length % 2 == 1)
        return longest >= length


class Solution:
    def shortestPalindrome(self, s: str) -> str:

        n = len(s)

        if n <= 1:
            return s

        m = Manacher(s)

        # Find longest palindromic prefix
        longestPrefix = 0

        for i in range(n - 1, -1, -1):
            if m.check(0, i):
                longestPrefix = i + 1
                break

        suffix = s[longestPrefix:]

        return suffix[::-1] + s