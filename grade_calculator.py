def calculate_grade(percentage):
    if percentage >= 90:
        return 'A+'
    elif percentage >= 80:
        return 'A'
    elif percentage >= 70:
        return 'B'
    elif percentage >= 60:
        return 'C'
    elif percentage >= 50:
        return 'D'
    else:
        return 'F'
def main():
    print("=== CLI Grade Calculator ===")
    student_data = {}
    while True:
        try:
            num_subjects = int(input("Enter total number of subjects: "))
            if num_subjects > 0:
                break
            print("Enter a positive number.")
        except ValueError:
            print("Invalid input. Enter a whole number, not words.")
    for i in range(1, num_subjects + 1):
        subject_name = input(f"Enter name for subject {i}: ").strip()
        while True:
            try:
                marks = float(input(f"Enter marks obtained in {subject_name} (0-100): "))
                if 0 <= marks <= 100:
                    student_data[subject_name] = marks
                    break
                else:
                    print("Invalid input. Marks must be between 0 and 100.")
            except ValueError:
                print("Invalid input. Enter a valid numerical value.")
    total_marks = sum(student_data.values())
    max_marks = num_subjects * 100
    percentage = (total_marks / max_marks) * 100 if max_marks > 0 else 0
    grade = calculate_grade(percentage)
    print("\n" + "="*30)
    print("        GRADE REPORT        ")
    print("="*30)
    for subject, marks in student_data.items():
        print(f"{subject:<15}: {marks:.2f}")
    print("-" * 30)
    print(f"Total Marks    : {total_marks:.2f} / {max_marks}")
    print(f"Percentage     : {percentage:.2f}%")
    print(f"Overall Grade  : {grade}")
    print("="*30)
if __name__ == "__main__":
    main()