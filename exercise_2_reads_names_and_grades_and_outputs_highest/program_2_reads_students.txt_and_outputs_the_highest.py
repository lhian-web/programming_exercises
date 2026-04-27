class StudentGradeAnalyzer:
    def __init__(self, input_file: str = "students.txt"):
        self.input_file = input_file

    def read_students_data(self):
        try:
            students = []

            with open(self.input_file, "r") as file:
                for line in file:
                    name, gwa = line.strip().split(",")
                    students.append((name.strip(), float(gwa.strip())))

            return students

        except FileNotFoundError:
            print(f"File {self.input_file} does not exist")
            return []

        except ValueError:
            print("Error: Each line must be in 'Name, GWA' format")
            return []