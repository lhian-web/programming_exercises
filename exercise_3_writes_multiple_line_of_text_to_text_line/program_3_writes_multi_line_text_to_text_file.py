class MultiLineWriter:
    def __init__(self, output_file: str = "myline.txt"):
        self.output_file = output_file

    def write_multiple_lines(self):
        with open(self.output_file, "w") as file:

            while True:
                user_line = input("Enter Line: ")

                file.write(user_line + "\n")

                continue_option = input("Are there more lines? y/n: ").lower()

                if continue_option == "n":
                    break
