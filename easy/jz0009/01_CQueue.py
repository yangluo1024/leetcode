class CQueue:
    """
    两个栈实现一个队列功能
    一个栈只负责入，一个栈只负责出
    """
    def __init__(self):
        self.IN, self.OUT = [], []

    def appendTail(self, value):
        self.IN.append(value)

    def deleteHead(self):
        if self.OUT: return self.OUT.pop()
        if not self.IN: return -1
        while self.IN:
            self.OUT.append(self.IN.pop())
        return self.OUT.pop()
