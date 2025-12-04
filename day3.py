## Advent of code 2025 - Day 3 ## 
import re

data_file = open("day3.txt", "r")
df = data_file.readlines()
clean_df = [x.strip() for x in df]

## Part 1 
joltages = [] 

for bank in clean_df: 
    first_integer = max(bank)

    if(bank.index(max(bank)) == (len(bank) - 1)): 
        second_integer = first_integer
        first_integer = max(max(bank[:-1]))
                          
    else: 
        second_integer = max(bank[bank.index(max(bank))+1:])

    joltages.append(int(first_integer + second_integer))

sum(joltages)

## Part 2 

joltages = [] 

for bank in clean_df: 
    integer = []
    found_int = 0 
    for i in range(12):
        found_int = 0
        temp_bank = bank
        while found_int == 0: 
            current_max = max(temp_bank)
            if (bank.index(current_max) + (12 - i) <= len(bank)):
                integer.append(current_max)
                bank = bank[bank.index(current_max)+1:]
                found_int = 1 
            else: 
                temp_bank = bank[:bank.index(max(current_max))]

    joltages.append(int(''.join(integer)))


sum(joltages)
    



