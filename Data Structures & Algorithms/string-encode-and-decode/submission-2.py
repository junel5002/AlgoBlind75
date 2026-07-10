class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for word in strs:
            encoded += str(len(word)) + "#" + word

        return encoded
    
#NB: str(len(word)) converts the integer into a string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s): #this line means while we've not reached the end yet, continue decoding
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            word_start_index = j + 1
            word_end_index = word_start_index + length

            res.append(s[word_start_index:word_end_index])

            i = word_end_index #now i takes on from where the previous 
                         #word in the string ended

        return res


#time complexity: O(m + n) for each encode() and decode() function calls
#space complexity: O(m + n) for each encode() and decode() function calls

#where m is the sum of lengths of all the strings and n is the number of
#strings
