class NumberCategorizer:
    def __init__(self, source_file: str = "numbers.txt"):
        self.source_file = source_file

    def read_numbers_from_source(self) -> list[int]:

        try:
            with open(self.source_file, "r") as file:
                number_list = [int(value.strip()) for value in file.readlines()]
            return number_list

        except FileNotFoundError:
            print(f"File {self.source_file} not found.")
            return []

        except ValueError:
            print("Error: File must contain only integers.")
            return []

    def append_numbers_to_file(self, target_file: str, number_value: int):
        with open(target_file, "a") as file:
            file.write(f"{number_value}\n")

    def separate_even_and_odd(self):
        numbers = self.read_numbers_from_source()

        open("even.txt", "w").close()
        open("odd.txt", "w").close()

        for current_number in numbers:
            if current_number % 2 == 0:
                self.append_numbers_to_file("even.txt", current_number)
            else:
                self.append_numbers_to_file("odd.txt", current_number)

if __name__ == "__main__":
    number_categorizer = NumberCategorizer()
    number_categorizer.separate_even_and_odd()