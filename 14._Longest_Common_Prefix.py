class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        else:
            word = strs[0]
            for i in strs[1:]:
                while not i.startswith(word):
                    word = word[:-1]
            if not word:
                return ""
            else:
                return word
