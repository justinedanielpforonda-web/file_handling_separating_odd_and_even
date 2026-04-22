#variables to be used
numbers = []

even = []
odd = []

# logic to separate the od and even number using if and else
for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)