class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_data = []
        self.data = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if self.min_data == [] or self.min_data[-1] > x:
            self.min_data.append(x)
        else:
            self.min_data.append(self.min_data[-1])

    def pop(self) -> None:
        self.data.pop()
        self.min_data.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min_data[-1]


if __name__ == '__main__':

