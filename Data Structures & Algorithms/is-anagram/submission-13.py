class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        for char in s:
            countS[char] = countS.get(char, 0) + 1
        for char in t:
            countT[char] = countT.get(char, 0) + 1
    
        return countS == countT


       
        




#NB: First we sort the letters in both words and we compare the sorted words and if they are equal we just return true or return false.
        