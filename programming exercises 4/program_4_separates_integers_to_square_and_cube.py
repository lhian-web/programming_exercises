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