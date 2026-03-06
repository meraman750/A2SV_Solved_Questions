class Node:
    def __init__(self, val="", next=None, prev=None): 
        self.val = val
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = Node(homepage)
        self.cur = self.head 

    def visit(self, url: str) -> None:
        now = Node(url)
        self.cur.next = now
        now.prev = self.cur
        self.cur = now

    def back(self, steps: int) -> str:
        while steps > 0:
            if self.cur.prev:
                self.cur = self.cur.prev
            else:
                return self.cur.val 
            steps-=1
        return self.cur.val 

    def forward(self, steps: int) -> str:
        while steps > 0:
            if self.cur.next:
                self.cur = self.cur.next
            else:
                return self.cur.val
            steps-=1
        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)