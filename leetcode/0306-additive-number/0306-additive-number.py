class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        temp = []

        def calc(n):
            if n >= len(num):
                # print(temp)
                # if len(temp) <= 2:
                #     return False
                # for i in range(2, len(temp)):
                #     if (temp[i-1] + temp[i-2]) != temp[i]:
                #         return False
                return len(temp) >= 3
            
            for i in range(n, len(num)):
                if num[n] == "0" and i > n:
                    break
                temp.append(int(num[n:i+1]))

                if len(temp) >= 3:
                    if temp[-1] != temp[-2] + temp[-3]:
                        temp.pop()
                        continue

                if calc(i+1):
                    return True
                temp.pop()
            return False

        return calc(0)