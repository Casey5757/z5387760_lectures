regular_rate = 51.45
overtime_rate = 88.9
limit_hours = 35
hours_worked = int(input("Enter the number of hours worked:"))
if hours_worked <= limit_hours:
    pay = hours_worked * regular_rate
else:
    regular_pay = limit_hours * regular_rate
    overtime_pay = (hours_worked - limit_hours) * overtime_rate
    pay = regular_pay + overtime_pay

print(f"Your total pay for the week is: ${pay:.2f}")



hours = int(input("Enter number of hours you work this week: "))

normal_rate = 51.45
overload_rate = 88.9
threshold = 35

if hours > threshold:
    payment = (threshold * normal_rate) + ((hours - threshold) * overload_rate)
else:
    payment = hours * normal_rate

print(f"This weekly payment is {payment} dollars")

# Exercise 2
numbers = [-2, 3, 9, 1, 7, 2, 11, 0, 3, 12, 3, 15, 10]

largest_number = numbers[0]

for number in numbers:
    if number > largest_number:
        largest_number = number


print("Remembered largest number: ", largest_number)


