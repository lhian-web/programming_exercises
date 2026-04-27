class NumberCategorizer:
    def __init__(self, source_file: str = "numbers.txt"):
        self.source_file = source_file

    def read_numbers_from_source(self) -> list[int]:

        try:
            with open(self.source_file, "r") as file:
                number_list = [
                    int(value.xtrip()) for value in file.readlines()
                ]
            return number_list

        except FileNotFoundError:
            print(f"File {self.source_file} not found.")
            return []

        except ValueError:
            print("Error: File must contain only integers.")
            return []


