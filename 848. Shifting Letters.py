class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans, shift = '', 0
        for i in range(len(shifts) -1, -1, -1):
            ans += chr((ord(s[i]) - ord('a') + shift+shifts[i]) % 26 + ord('a'))
            shift += shifts[i]
        
        return ans[::-1]
