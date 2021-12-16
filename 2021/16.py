#!/usr/bin/env python3

import sys

if __name__ == "__main__":
    for l in open(sys.argv[1] if len(sys.argv) > 1 else '16-input'):
        src = l.strip()

    stream_in = ''
    for c in src:
        stream_in += f'{int(c, 16):04b}'

    part1 = 0


    def process(stream: str, packet_count: int = None):
        global part1

        ret = []

        while len(stream) >= 6 + 5:
            V, T, stream = int(stream[:3], 2), int(stream[3:6], 2), stream[6:]

            part1 += V

            if T == 4:
                N = 0
                while True:
                    start, n, stream = stream[0], stream[1:5], stream[5:]
                    N *= 16
                    N += int(n, 2)
                    if start == '0':
                        break
                ret += [N]
            else:
                I, stream = int(stream[0]), stream[1:]
                if I == 0:
                    L, stream = int(stream[:15], 2), stream[15:]
                    R, _ = process(stream[:L])
                    stream = stream[L:]
                elif I == 1:
                    L, stream = int(stream[:11], 2), stream[11:]
                    R, stream = process(stream, L)

                if T == 0:
                    ret += [sum(R)]
                elif T == 1:
                    t = R[0]
                    for i in R[1:]:
                        t *= i
                    ret += [t]
                elif T == 2:
                    ret += [min(R)]
                elif T == 3:
                    ret += [max(R)]
                elif T == 5:
                    ret += [R[0] > R[1]]
                elif T == 6:
                    ret += [R[0] < R[1]]
                elif T == 7:
                    ret += [R[0] == R[1]]
                else:
                    print('invalid operator')

            if packet_count is not None:
                packet_count -= 1
                if packet_count == 0:
                    break

        return ret, stream


    part2, _ = process(stream_in)

    print('part1', part1)
    print('part2', part2[0])
