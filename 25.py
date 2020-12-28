#!/usr/bin/env python3

iv = 7
divisor = 20201227

def transform_subject(subject: int, loop: int):
    value = 1
    for i in range(loop):
        value *= subject
        value %= divisor
    return value

def transform_subject_get_loop(subject: int, target):
    value = 1
    for i in range(100000000):
        value *= subject
        value %= divisor
        if value == target:
            return i + 1
    raise ValueError('impossible to find a loop-value')

card_ex = (5764801, 8)
door_ex = (17807724, 11)

assert transform_subject(7, card_ex[1]) == card_ex[0]
assert transform_subject(7, door_ex[1]) == door_ex[0]
assert transform_subject(card_ex[0], door_ex[1]) == transform_subject(door_ex[0], card_ex[1])

card_pub_key = 5099500
card_priv_key = transform_subject_get_loop(7, card_pub_key)
print("card's loop", card_priv_key)

door_pub_key = 7648211
door_priv_key = transform_subject_get_loop(7, door_pub_key)
print("door's loop", door_priv_key)

key0 = transform_subject(door_pub_key, card_priv_key)
key1 = transform_subject(card_pub_key, door_priv_key)
print("encryption key", key0, key1)

