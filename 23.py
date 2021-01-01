#!/usr/bin/env python3


class CupInCircle:
    def __init__(self, v: int, p, n):
        self.val = v
        self.prev = p
        self.next = n

    def to_str(self, count=-1):
        s = ''
        n = self
        while True:
            s += str(n.val)

            n = n.next
            if n == self:
                break

            count -= 1
            if count == 0:
                break
        return s

    def __str__(self):
        return self.to_str()

    def find(self, val):
        n = self
        while True:
            if n.val == val:
                return n
            n = n.next
            if n == self:
                break
        return None

    def __len__(self):
        l = 0

        n = self
        while True:
            l += 1
            n = n.next
            if n == self:
                break

        return l


prev = None
first = None  # start
for i in '739862541':
# for i in '389125467':
    node = CupInCircle(int(i), prev, None)

    if prev is not None:
        prev.next = node

    if first is None:
        first = node

    prev = node

# close the circle
first.prev = prev
prev.next = first

input_len = len(first)
print('len', input_len)
print(first)

current = first
for move in range(100):
    print('--', move + 1, '--', len(first))
    print(first)

    # take out three cups
    three = current.next

    current.next = three.next.next.next
    three.next.next.next.prev = current

    print('pick up ', three.to_str(3))

    dest_val = current.val - 1

    while True:
        dest = current.find(dest_val)
        if dest is not None:
            break
        else:
            dest_val -= 1
            if dest_val < 0:
                dest_val = input_len

    print('dest', dest.val)

    dest.next.prev = three.next.next
    three.next.next.next = dest.next

    dest.next = three
    three.prev = dest

    current = current.next

one = first.find(1)
print('part1', one.to_str()[1:])
