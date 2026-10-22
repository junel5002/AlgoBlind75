class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
        







#NB: First im going to start with an empty string, then i check through every character across all word. if it ends or is different i would return the result. Otherwise i would add or update it to the matching characters and finally i return the result.