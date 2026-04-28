class TextFileWriter:
    def __init__(self, output_filename):
        self.output_filename = output_filename
    def write_lines(self):
        with open(self.output_filename, "w") as file:
            has_more_lines = "y"

            while has_more_lines == "y":
                user_input = input("Enter line: ")
                file.write(user_input + "\n")
                has_more_lines = input("Are there more lines (y/n)? ")
# main
writer = TextFileWriter("mylife.txt")
writer.write_lines()
print("text saved to mylife.txt")