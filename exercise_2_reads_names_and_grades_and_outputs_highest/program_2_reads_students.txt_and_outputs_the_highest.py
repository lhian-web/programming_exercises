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

    def find_highest(self):
        students = self.read_students_data()

        if not students:
            print("No data found")

        highest_gwa = students[0][1]
        highest_student = [students[0][0]]

        for name, gwa in students[1:]:

            if gwa < highest_gwa:
                highest_gwa = gwa
                highest_student = [name]

            elif gwa == highest_gwa:
                highest_student.append(name)

        print("Top student(s) with highest GWA:")
        for student in highest_student:
            print(f"Name: {student}")
        print(f"Highest GWA: {highest_gwa}")

if __name__ == "__main__":
    analyzer = StudentGradeAnalyzer()
    analyzer.find_highest()
