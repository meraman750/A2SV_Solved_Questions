class FrequencyTracker:

    def __init__(self):
        self.arr = defaultdict(int)
        self.count = defaultdict(int)

    def add(self, number: int) -> None:
        self.count[self.arr[number]] -=1
        self.arr[number] = self.arr.get(number, 0) +1
        self.count[self.arr[number]] +=1

    def deleteOne(self, number: int) -> None:
        if number in self.arr:
            self.count[self.arr[number]] -=1
            self.arr[number] -=1
            self.count[self.arr[number]] +=1
            if self.arr[number] == 0:
                del self.arr[number]

    def hasFrequency(self, frequency: int) -> bool:
        return self.count[frequency] > 0


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)