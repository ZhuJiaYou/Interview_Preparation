class MyQueue1:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self.move()
        return self.out_stack.pop()

    def move(self) -> None:
        if self.out_stack == []:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def peek(self) -> int:
        self.move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return self.in_stack == self.out_stack == []


class MyQueue2:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1


if __name__ == '__main__':
    q1 = MyQueue1()
    q1.push(1)
    q1.push(2)
    print(q1.peek())
    print(q1.pop())
    print(q1.pop())
    print(q1.empty())

    print()

    q2 = MyQueue2()
    q2.push(3)
    q2.push(4)
    print(q2.peek())
    print(q2.pop())
    print(q2.pop())
    print(q2.empty())
