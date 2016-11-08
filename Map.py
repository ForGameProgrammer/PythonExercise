income = [100, 450, 75, 90, 225, 550]

# Function that doubles the number - Simple
def double_income(number):
    return number * 2

# Map runs function for each element in list, List stays same - First Argument Function name no (), Second Argument list
# List Makes it List - Simple?
new_income = list(map(double_income, income))

print(new_income)
# [200, 900, 150, 180, 450, 1100]

# Same with for
new_income = [item * 2 for item in income]
print(new_income)
# [200, 900, 150, 180, 450, 1100]
