class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
        


#NB: First you start with an empty string, then you check through the characters of each word. if it stops or is different from the matching charaters you return  the result. Otherwise you add or update it to the matching characters. and finally you return the result.