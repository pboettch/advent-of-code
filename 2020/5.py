#!/usr/bin/env python3

def to_seatid(l: str):
    return int(l.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1'), 2)


assert to_seatid('BFFFBBFRRR') == 567
assert to_seatid('FFFBBBFRRR') == 119
assert to_seatid('BBFFBBFRLL') == 820

print(to_seatid('FBFBBFFRLR'))

max_seatid = 0

seat_ids = []

with open('5.input') as f:
    for l in f.readlines():
        seat_id = to_seatid(l)
        if seat_id > max_seatid:
            max_seatid = seat_id
        seat_ids.append(seat_id)

print(f'max-seatid {max_seatid}')

last_seat_id = -1
for seat_id in sorted(seat_ids):
    if last_seat_id != -1 and seat_id == last_seat_id + 2:
        print('could be', seat_id - 1)
    last_seat_id = seat_id


