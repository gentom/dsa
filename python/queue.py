#!/usr/bin/env python


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def show(self):
        print(self.items)


if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.show()
    q.enqueue(9)
    q.show()
    q.enqueue(10.5)
    q.show()
    q.enqueue('Ballo')
    q.show()
    q.dequeue()
    q.dequeue()
    q.show()
