class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)

        # If length difference is more than 1, impossible in one edit
        if abs(m - n) > 1:
            return False

        # Make sure s is the shorter (or equal) string
        if m > n:
            return self.isOneEditDistance(t, s)

        # Find first mismatch
        for i in range(m):
            if s[i] != t[i]:
                # Case 1: same length -> must be one replacement
                if m == n:
                    return s[i + 1:] == t[i + 1:]

                # Case 2: t is longer by 1 -> must be one insertion into s
                return s[i:] == t[i + 1:]

        # All first m chars matched
        # They are one edit apart only if t has exactly one extra trailing char
        return n == m + 1
        