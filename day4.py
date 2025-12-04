## Advent of code 2025 - Day 3 ## 
data_file = open("day4.txt", "r")
df = data_file.readlines()
clean_df = [x.strip() for x in df]

## Part 1 
rolls_of_paper = 0

for idy, row in enumerate(clean_df):
    for idx, val in enumerate(row): 
        if val == "@":
            count_adj = 0
            if (idx > 0):
                count_adj += int(row[idx - 1] == "@")
            if (idx < len(row) - 1):
                count_adj += int(row[idx + 1] == "@")
            if (idy > 0): 
                count_adj += clean_df[idy-1][max(0,idx-1):(min(idx+1, len(row) - 1)) + 1].count("@")
            if (idy < len(clean_df) - 1):
                count_adj += clean_df[idy+1][max(0,idx-1):(min(idx+1, len(row) - 1)) + 1].count("@")
            
            if count_adj < 4: 
                rolls_of_paper += 1
        else: 
            continue

## Part 2
rolls_of_paper = 0
location = []
available_rolls = True
clean_df = [list(row) for row in clean_df]

while(available_rolls == True): 
    if len(location) > 0: 
        for loc_i in location:
            clean_df[loc_i[0]][loc_i[1]] = "."
            location = []
    for idy, row in enumerate(clean_df):
        for idx, val in enumerate(row): 
            if val == "@":
                count_adj = 0
                if (idx > 0):
                    count_adj += int(row[idx - 1] == "@")
                if (idx < len(row) - 1):
                    count_adj += int(row[idx + 1] == "@")
                if (idy > 0): 
                    count_adj += clean_df[idy-1][max(0,idx-1):(min(idx+1, len(row) - 1)) + 1].count("@")
                if (idy < len(clean_df) - 1):
                    count_adj += clean_df[idy+1][max(0,idx-1):(min(idx+1, len(row) - 1)) + 1].count("@")
            
                if count_adj < 4: 
                    rolls_of_paper += 1
                    location.append((idy, idx))
            else: 
                continue
    if len(location) == 0:
        available_rolls = False            
        