#reverse words in string

class Solution:
    def reverseWords(self, s: str) -> str:
        for line in s.split('\n'):
            return(' '.join(line.split()[::-1]))