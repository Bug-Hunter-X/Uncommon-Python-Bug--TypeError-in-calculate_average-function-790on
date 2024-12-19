def calculate_average(numbers):
    if not numbers:
        return 0
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0 # Handle list with only non-numeric elements
    total = sum(numeric_numbers)
    average = total / len(numeric_numbers)
    return average

my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_numbers = [1,2,3,4,5]
result = calculate_average(my_numbers)
print(f"The average is: {result}")

my_numbers = [1,2,3,4,'a']
result = calculate_average(my_numbers)
print(f"The average is: {result}") #This will now work without error