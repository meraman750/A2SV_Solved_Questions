class DataStream:

    def __init__(self, value: int, k: int):
        self.nums = deque()
        self.val = value
        self.k = k
        self.last = -1

    def consec(self, num: int) -> bool:
        # print(self.last)
        self.nums.append(num)
        if num != self.val:
            self.last = len(self.nums)-1
            
        if len(self.nums) < self.k:
            return False
        elif len(self.nums) > self.k:
            self.last-=1
            self.nums.popleft()

        if self.last >= 0:
            return False
        else:
            return True

        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)