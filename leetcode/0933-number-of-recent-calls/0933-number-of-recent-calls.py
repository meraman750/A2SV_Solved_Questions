class RecentCounter:

    def __init__(self):
        self.nums = deque()

    def ping(self, t: int) -> int:
        self.nums.append(t)
        while self.nums and self.nums[0] < t-3000:
            self.nums.popleft()
        return len(self.nums)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)