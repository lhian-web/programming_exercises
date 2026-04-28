class IntegerSquareAndCube:
    def __init__(self, source_file: str = "integers.txt"):
        self.source_file = source_file

    def read_integers(self):
        try:
            with open(self.source_file, "r") as file:
                return [int(line.strip()) for line in file]

        except FileNotFoundError:
            print(f"File {self.source_file} not found")
            return []

        except ValueError:
            print("File must contain only integers")
            return []

    def write_integers(self, filename: str, value: int):
        with open(filename, "a") as file:
            file.write(f"{value}\n")

    def process_integers(self):
        integers = self.read_integers()

        open("double.txt", "w").close()
        open("triple.txt", "w").close()

        for number in integers:
            if number % 2 == 0:
                self.write_integers("double.txt", number ** 2)

            else:
                self.write_integers("triple.txt", number ** 3)

if __name__ == "__main__":
    integers = IntegerSquareAndCube()
    integers.process_integers()