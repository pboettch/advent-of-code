#!/usr/bin/env python3


class CupInCircle:
    def __init__(self, val: int):
        self.val = val
        self.next = next

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

    def __len__(self):
        l = 0

        n = self
        while True:
            l += 1
            n = n.next
            if n == self:
                break

        return l


first = None  # start

input = '739862541'
# input = '389125467'

val_node = {}

node_1 = None

prev = None

for i in list(input) + list(range(len(input) + 1, 1000001)):
    node = CupInCircle(int(i))
    val_node[int(i)] = node

    if i == '1':
        node_1 = node

    if first is None:
        first = node

    if prev is not None:
        prev.next = node

    prev = node


# close the circle
node.next = first

input_len = len(first)

print('len', input_len)

current = first
count = 0
for move in range(int(1e7)):
    # take out three cups
    three = current.next

    current.next = three.next.next.next

    # print('pick up ', three.to_str(3))

    dest_val = current.val

    while True:
        dest_val -= 1
        if dest_val < 1:
            dest_val = input_len

        dest = val_node[dest_val]
        if dest != three and dest != three.next and dest != three.next.next:
            break

    three.next.next.next = dest.next

    dest.next = three

    current = current.next

    count += 1
    if count % 100000 == 0:
        print(count)

print('part2', node_1.next.val * node_1.next.next.val)
