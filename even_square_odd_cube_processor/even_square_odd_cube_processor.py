class NumberProcessor:
    def __init__(self, filename):
        self.filename = filename
    def read_numbers(self):
        with open(self.filename) as file:
            return [int(line.strip()) for line in file]
    def process_numbers(self, numbers):
        even_squares = []
        odd_cubes = []
        for number in numbers:
            if number % 2 == 0:
                even_squares.append(number ** 2)
            else:
                odd_cubes.append(number ** 3)
        return even_squares, odd_cubes
    def write_numbers(self, filename, numbers):
        with open(filename, "w") as file:
            for number in numbers:
                file.write(str(number) + "\n")
# main
processor = NumberProcessor("integers.txt")
numbers = processor.read_numbers()
even_squares, odd_cubes = processor.process_numbers(numbers)
processor.write_numbers("double.txt", even_squares)
processor.write_numbers("triple.txt", odd_cubes)
print("files created")