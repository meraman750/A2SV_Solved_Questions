class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        count1 = Counter(word1)
        count2 = Counter(word2)

        d1 = defaultdict(int)
        d2 = defaultdict(int)

        for key, val in count1.items():
            d1[val] +=1

        for key, val in count2.items():
            d2[val] +=1
        
        for key, val in count1.items():
            if key not in count2:
                return False
        
        for key, val in count2.items():
            if key not in count1:
                return False

        for key, val in d1.items():
            if key not in d2 or val != d2[key]:
                return False

        for key, val in d2.items():
            if key not in d1 or val != d1[key]:
                return False
        return True 
        
