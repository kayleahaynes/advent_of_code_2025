## Advent of code 2025 - Day 1 ## 
import re

data_file = open("day1.txt", "r")
df = data_file.readlines()

# Parts 1 and 2 
dial_start = 50 

dial_location = [dial_start] 
zero_count = 0 

for rotation in df: 
    rotation_direction = rotation[0]
    rotation_length = int(rotation[1:])
    current_position = dial_location[-1]
    
    for _ in range(rotation_length):
        if rotation_direction == "L":
            current_position = (current_position - 1) % 100
        else: 
            current_position = (current_position + 1) % 100
        if current_position == 0: 
            zero_count += 1
    dial_location.append(current_position)
    print(zero_count)

sum(1 for d in dial_location if d == 0)



