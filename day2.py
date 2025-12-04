## Advent of code 2025 - Day 2 ## 

data_file = open("day2.txt", "r")
df = data_file.readlines()

product_codes = df[0].split(",")

## Part 1 ## 
invalid_codes = [] 

for code_range in product_codes:
    min_number = int(code_range.split("-")[0])
    max_number = int(code_range.split("-")[1])

    for i in range(min_number, max_number + 1):
        if len(str(i)) % 2 == 0:
            min_number_check = str(i)[0:int(len(str(i))/2)]
            max_number_check = str(i)[int(len(str(i))/2):]

            if int(min_number_check) == int(max_number_check): 
                invalid_codes.append(i)

sum(invalid_codes)

## Part 2 ## 

invalid_codes = [] 

for code_range in product_codes:
    min_number = int(code_range.split("-")[0])
    max_number = int(code_range.split("-")[1])

    for i in range(min_number, max_number + 1):
        code_i = str(i)
        for block_size in range(1, round(len(code_i)/2) + 1):
            if len(code_i) % block_size != 0:
                continue
            
            block = code_i[:block_size]
            if block * (len(code_i) // block_size) == code_i:
                invalid_codes.append(int(code_i))

set(invalid_codes)
sum(set(invalid_codes))

        