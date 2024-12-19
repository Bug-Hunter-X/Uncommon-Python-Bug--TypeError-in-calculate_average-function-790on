def calculate_average(numbers):
    if not numbers:  # Handle empty list
        return 0
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_numbers = []
result = calculate_average(my_numbers)
print(f"The average is: {result}") #This will work fine

my_numbers = [1,2,3,4,5]
result = calculate_average(my_numbers)
print(f"The average is: {result}") #This will also work fine

my_numbers = [1,2,3,4,'a']
result = calculate_average(my_numbers) #This will throw an error
print(f"The average is: {result}")