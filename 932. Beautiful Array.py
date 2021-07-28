class Solution:
    def beautifulArray(self, N):
        a = list(range(1, N + 1))
        return self.r_fun(a)
        pass

    def r_fun(self, a):
        if len(a) <= 1:
            return a
        odd = [v for idx, v in enumerate(a) if idx % 2 == 1]
        even = [v for idx, v, in enumerate(a) if idx % 2 == 0]
        odd = self.r_fun(odd)
        even = self.r_fun(even)
        return odd + even
