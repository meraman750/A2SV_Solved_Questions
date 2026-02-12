class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m = set(ransomNote)
        for i in m:
            if ransomNote.count(i) > magazine.count(i) or i not in magazine:
                return False
        return True