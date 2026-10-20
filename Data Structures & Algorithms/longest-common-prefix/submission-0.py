class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

        
            

        



#NB:first we are going to start with an empty string, then we check each character across each word, and then if it ends or is different from the matching word we return the result. Otherwise we update or add it to the matching characters.Then we finaly return the result.