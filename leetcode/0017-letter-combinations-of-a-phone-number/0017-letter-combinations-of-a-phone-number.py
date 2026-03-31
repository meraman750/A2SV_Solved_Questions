class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        ans = []
        d = {
                    '2': 'abc',
                    '3': 'def',
                    '4': 'ghi',
                    '5': 'jkl',
                    '6': 'mno',
                    '7': 'pqrs',
                    '8': 'tuv',
                    '9': 'wxyz',
                } 

        def calc(temp, cur):
            if cur >= len(digits):
                ans.append(temp)
                return 

            for i in d[digits[cur]]:
                temp += i
                calc(temp, cur+1)
                temp = temp[:-1]

        calc("", 0)
        return ans

            





















        # def add_digits(temp, cur, digit):
        #             if digit >= n:
        #                 ans.append("".join(temp))
        #                 return  
        #             for i in range(len(d[cur])):
        #                     temp.append(d[cur][i])
        #                     if digit+1 < n:
        #                         add_digits(temp, digits[digit+1], digit+1)
        #                     else:
        #                         ans.append("".join(temp))
        #                     temp.pop()

        # add_digits([], digits[0], 0)
        # return ans

        


