class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for word in strs:
            # Sort the letters in the word
            key = "".join(sorted(word))

            # Add the original word to its group
            groups[key].append(word)

        return list(groups.values())

#most efficient and simpler
#step1: create a hashmap, step2: go through each word in the list, 
#step3: sort each word, step4: use as key in the hashmap....

"""NB: defaultdict() is a special hashmap. it works in a way that anytime you want to 
add a value to a key and the key doesn't exist yet, it will create an empty datatype
depending on the parameter it takes in. eg. defaultdict(list) means all the values
are going to be in a list so when it want to create an empty data type, it's an empty
list it will create """



"""NB: The difference btn .sort() and sorted() is that .sort() only works on lists
while sorted() works on tuples, strings, dicts and returns a list
for eg. array = ["apple", "mango", "banana"]
array.sort() will give me array = ["apple", "banana", "mango"] """

"""let's say myName = "Nelson"
sorted_name = sorted(myName) will give me ["e", "l", "n", "N", "o", "s"]

NB: "".join() converts everything in a list into a string
for eg. firstName = ["N", "e", "l", "s", "o", "n"]
 "".join(firstName) gives me "Nelson"""