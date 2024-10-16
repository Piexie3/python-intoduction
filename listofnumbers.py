
numbers = []

print("Enter a list of numbers, type 0 when finished.")

while True:
    number = float(input("Enter number: "))
    if number == 0:
        break
    numbers.append(number)

total_sum = sum(numbers)

if numbers:
    average = total_sum / len(numbers)
else:
    average = 0

largest_number = max(numbers)

positive_numbers = [num for num in numbers if num > 0]
smallest_positive_number = min(positive_numbers) if positive_numbers else None

sorted_numbers = sorted(numbers)

print(f"\nThe sum is: {total_sum}")
print(f"The average is: {average}")
print(f"The largest number is: {largest_number}")
if smallest_positive_number is not None:
    print(f"The smallest positive number is: {smallest_positive_number}")
else:
    print("No positive numbers were entered.")
    
print("The sorted list is:")
for num in sorted_numbers:
    print(num)
