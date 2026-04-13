class Solution:
    def smallestNumber(self, pattern: str) -> str:

        n = len(pattern)
        used = [False] * 10
        ans = ""

        def backtrack(path):
            nonlocal ans

            if ans:
                return

            if len(path) == n + 1:
                ans = path
                return

            for d in range(1, 10):

                if used[d]:
                    continue

                if path:
                    prev = int(path[-1])

                    if pattern[len(path)-1] == 'I' and d <= prev:
                        continue
                    if pattern[len(path)-1] == 'D' and d >= prev:
                        continue

                used[d] = True
                backtrack(path + str(d))
                used[d] = False

        backtrack("")
        return ans