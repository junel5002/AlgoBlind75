class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS = {}
        countT = {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) 
            #this returns the value of the key if its exists otherwise put 0 as default but we add one 
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT
        
countS = {
    "r": 1,
    "a": 1,
    "c": 1,
    "e": 1
}

countT = {
    "c": 1,

}

s = "racecar"
t = "carrace"