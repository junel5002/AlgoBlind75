class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        word_length = len(beginWord)

        # Map each wildcard pattern to all words matching that pattern.
        # Example: "hot" -> "*ot", "h*t", "ho*"
        pattern_to_words = defaultdict(list)

        # Include beginWord as well so BFS can expand from it naturally.
        all_words = wordList + [beginWord]

        for word in all_words:
            for index in range(word_length):
                pattern = word[:index] + "*" + word[index + 1:]
                pattern_to_words[pattern].append(word)

        # Standard BFS for shortest path in an unweighted graph.
        queue = deque([(beginWord, 1)])
        visited_words = set([beginWord])

        while queue:
            current_word, current_length = queue.popleft()

            # Generate all one-letter-different wildcard patterns.
            for index in range(word_length):
                pattern = current_word[:index] + "*" + current_word[index + 1:]

                # Explore neighbors that share this pattern.
                for next_word in pattern_to_words[pattern]:
                    if next_word == endWord:
                        return current_length + 1

                    if next_word not in visited_words:
                        visited_words.add(next_word)
                        queue.append((next_word, current_length + 1))

                # Clear this pattern list after processing to avoid
                # repeated work in future BFS steps.
                pattern_to_words[pattern] = []

        return 0






