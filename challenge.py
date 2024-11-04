#!/usr/bin/python3
dc_characters = ['Batman', 'Superman', 'Wonder Woman', 'The Flash', 'Aquaman', 'Green Lantern', 'Cyborg', 'Harley Quinn', 'Joker', 'Lex Luthor']
print("All characters")
print(dc_characters)

print("First five characters")
print(dc_characters[0:5])

print("Last five characters")
print(dc_characters[-5:])

print("Every other character starting with Batman")
print(dc_characters[::2])

print("All except Batman and Lex")
print(dc_characters[1:-1])
