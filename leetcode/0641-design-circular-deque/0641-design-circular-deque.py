class MyCircularDeque:

    def __init__(self, k: int):
        self.dec = deque()
        self.idx = 0
        self.k = k
        
    def insertFront(self, value: int) -> bool:
        if self.idx < self.k:
            self.dec.appendleft(value)
            self.idx +=1
            return True
        return False

    def insertLast(self, value: int) -> bool:
        if self.idx < self.k:
            self.dec.append(value)
            self.idx+=1
            return True
        return False

    def deleteFront(self) -> bool:
        if self.dec:
            self.dec.popleft()
            self.idx-=1
            return True
        return False

    def deleteLast(self) -> bool:
        if self.dec:
            self.dec.pop()
            self.idx-=1
            return True
        return False

    def getFront(self) -> int:
        if self.dec:
            return self.dec[0]
        return -1

    def getRear(self) -> int:
        if self.dec:
            return self.dec[-1]
        return -1

    def isEmpty(self) -> bool:
        return not self.dec

    def isFull(self) -> bool:
        return self.idx >= self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()