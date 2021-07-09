class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(start, end):
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1

        i, n = 0, len(s)
        for j in range(n):
            if s[j] == ' ':
                reverse(i, j-1)
                i = j + 1
        else:
            reverse(i, n-1)
            reverse(0, n-1)

        return s
