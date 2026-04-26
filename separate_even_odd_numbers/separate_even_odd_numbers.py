file = open("numbers.txt", "r")
even_file = open("even.txt", "w")
odd_file = open("odd.txt", "w")
for line in file:
    number = int(line.strip())
    if number % 2 == 0:
        even_file.write(str(number) + "\n")
    else:
        odd_file.write(str(number) + "\n")
file.close()
even_file.close()
odd_file.close()
print("Done!")