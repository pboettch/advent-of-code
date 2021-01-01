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
            n = n.prev
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

input = '739862541'
# input = '389125467'

val_node = {}

for i in list(input) + list(range(len(input) + 1, 1000001)):
    node = CupInCircle(int(i), prev, None)
    val_node[int(i)] = node

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

current = first
count = 0
for move in range(int(1e7)):
    # take out three cups
    three = current.next

    current.next = three.next.next.next
    three.next.next.next.prev = current

    # print('pick up ', three.to_str(3))

    dest_val = current.val

    while True:
        dest_val -= 1
        if dest_val < 1:
            dest_val = input_len

        dest = val_node[dest_val]
        if dest != three and dest != three.next and dest != three.next.next:
            break

    dest.next.prev = three.next.next
    three.next.next.next = dest.next

    dest.next = three
    three.prev = dest

    current = current.next

    count += 1
    if count % 10000 == 0:
        print(count)

one = first.find(1)
print('part2', one.next.val * one.next.next.val)
