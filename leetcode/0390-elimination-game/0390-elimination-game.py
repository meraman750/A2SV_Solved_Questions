class Solution:
    def lastRemaining(self, n: int) -> int:
        
        def rem(n ,head, flag, step):
            if n == 1:
                return head
            if flag or n %2 == 1:
                head += step
            return rem(n//2, head, not flag, step*2)

        return rem(n, 1, True, 1)
            
            

        # start = 2
        # length = n
        # count = 0

        # return 0

        # head = 1
        # step = 1
        # iteration = n
        # flag = True
        # while iteration > 1:
        #     if flag or iteration % 2 == 1:
        #         head += step

        #     iteration //= 2
        #     step *=2
        #     flag = not flag

        # return head
