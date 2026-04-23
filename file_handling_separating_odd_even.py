try:
    #accessing the files and closing after reading 
    file = open("numbers.txt", "r")
    data = file.read()
    numbers = data.split()
    file.close()

    even = []
    odd = []

# logic to separate the od and even number using if and else
    for num in numbers:
        num = int(num)
        if num % 2 == 0:
            even.append(str(num))
        else:
            odd.append(str(num))

    even_file = open("even.txt", "w")
    for num in even:
        even_file.write(num + " ")
    even_file.close()

    odd_file = open("odd.txt", "w")
    for num in odd:
        odd_file.write(num + " ")
    odd_file.close()
    print("Files created successfully!")

#error catching
except FileNotFoundError:
    print("Number.txt not found")
except ValueError:
    print("Data on file is invalid")