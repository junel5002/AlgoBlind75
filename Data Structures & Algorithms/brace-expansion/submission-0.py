class Solution:
    def expand(self, s: str) -> List[str]:
        groups = []
        i = 0
        n = len(s)

        # Parse input into groups of characters
        while i < n:
            if s[i] == '{':
                i += 1
                options = []
                while i < n and s[i] != '}':
                    if s[i] != ',':
                        options.append(s[i])
                    i += 1
                options.sort()
                groups.append(options)
                i += 1  # skip '}'
            else:
                groups.append([s[i]])
                i += 1

        # Backtracking to build all combinations
        result = []
        path = []

        def dfs(index: int) -> None:
            if index == len(groups):
                result.append("".join(path))
                return

            for ch in groups[index]:
                path.append(ch)
                dfs(index + 1)
                path.pop()

        dfs(0)
        return result
        