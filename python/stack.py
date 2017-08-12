#!/usr/bin/env python


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def show(self):
        return self.items


if __name__ == "__main__":
    st = Stack()

    print(st.isEmpty())
    print(st.show())
    st.push(4)
    st.push('dog')
    print(st.peek())
    st.push(True)
    print(st.show())
    print(st.size())
    print(st.isEmpty())
    st.push(8.4)
    print(st.pop())
    print(st.pop())
    print(st.size())
    st.push(5)
    st.push(10)
    print(st.show())
