## Advent of code 2025 - Day 3 ## 

data_file = open("day5.txt", "r")
df = data_file.read()

fresh_ingredients_range, available_ingredients = df.split("\n\n", 1)

fresh_ingredients_range = fresh_ingredients_range.split("\n")
available_ingredients = available_ingredients.split("\n")

# Part 1 
fresh_entity = []

for i in fresh_ingredients_range: 
    min_ingredient, max_ingredient = i.split("-")
    min_ingredient = int(min_ingredient)
    max_ingredient = int(max_ingredient)
    
    for j in available_ingredients: 
        if int(j) >= min_ingredient and int(j) <= max_ingredient: 
            fresh_entity.append(int(j))

len(set(fresh_entity))

# Part 2 

## Consolidate the ranges ##
fresh_ingredients_tuple = [tuple(map(int, r.split('-'))) for r in fresh_ingredients_range]

fresh_ingredients_tuple.sort(key=lambda x: x[0])

consolidated_fresh_ingredients = []
for min_ingredient, max_ingredient in fresh_ingredients_tuple:
    if not consolidated_fresh_ingredients or min_ingredient > consolidated_fresh_ingredients[-1][1] + 1:
        # no overlap, create new interval
        consolidated_fresh_ingredients.append([min_ingredient, max_ingredient])
    else:
        # overlap, extend the previous interval
        consolidated_fresh_ingredients[-1][1] = max(consolidated_fresh_ingredients[-1][1], max_ingredient)

## Count number of ingredients ##

count_ingredients = 0 

for i in consolidated_fresh_ingredients: 
    count_ingredients += i[1] - i[0] + 1
