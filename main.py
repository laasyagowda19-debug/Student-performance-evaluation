
# main.py

import re

from prediction import predict_students

from data_handler import (
    save_student_data,
    load_student_data,
    save_prediction_results
)


def main():

    print("=" * 45)
    print(" STUDENT PERFORMANCE PREDICTION SYSTEM")
    print("=" * 45)

    students = []

    try:

        # Number of students
        count = int(input("Enter number of students: "))

        if count <= 0:
            print("Please enter a positive number.")
            return

        # Enter student details
        for i in range(count):

            print(f"\nEnter details for student {i + 1}")

            # Student Name - alphabets and spaces only
            name = input("Student Name: ").strip()

            if not re.fullmatch(r"[A-Za-z ]+", name):
                print("Invalid name! Enter alphabets only.")
                return

            # Register Number - numbers only and unique
            while True:

                register_no = input("Register Number: ").strip()

                # Check numbers only
                if not register_no.isdigit():

                    print("Invalid register number! Enter numbers only.")
                    continue

                # Reject register number containing only zeros
                if int(register_no) == 0:

                    print("Register number cannot be zero!")
                    print("Enter another register number.")
                    continue

                # Check duplicate register number
                if any(
                    student["register_no"] == register_no
                    for student in students
                ):

                    print("Register number already exists!")
                    print("Enter another register number.")
                    continue

                # Valid register number
                break

            # Marks - numeric only
            try:
                marks = float(input("Marks (0-100): "))
            except ValueError:
                print("Invalid marks! Enter numbers only.")
                return

            if not 0 <= marks <= 100:
                print("Marks must be between 0 and 100.")
                return

            # Attendance - numeric only
            try:
                attendance = float(
                    input("Attendance percentage (0-100): ")
                )
            except ValueError:
                print("Invalid attendance! Enter numbers only.")
                return

            if not 0 <= attendance <= 100:
                print("Attendance must be between 0 and 100.")
                return

            # Study Hours - numeric only
            try:
                study_hours = float(
                    input("Study hours per day (0-24): ")
                )
            except ValueError:
                print("Invalid study hours! Enter numbers only.")
                return

            if not 0 <= study_hours <= 24:
                print("Study hours must be between 0 and 24.")
                return

            # Add student details
            students.append({
                "name": name,
                "register_no": register_no,
                "marks": marks,
                "attendance": attendance,
                "study_hours": study_hours
            })

        # Final duplicate register number check
        register_numbers = [
            student["register_no"]
            for student in students
        ]

        if len(register_numbers) != len(set(register_numbers)):

            print("Duplicate register numbers are not allowed.")
            return

        # Save student data
        save_student_data(students)

        # Load saved student data
        students = load_student_data()

        # Generate predictions
        results, at_risk, categories = predict_students(students)

        # Display prediction results
        print("\nSTUDENT PREDICTION RESULTS")
        print("-" * 45)

        for student in results:

            print("\nStudent Name:", student["name"])

            print("Register Number:", student["register_no"])

            print("Marks:", student["marks"])

            print("Attendance:", student["attendance"], "%")

            print("Study Hours:", student["study_hours"])

            print("Prediction:", student["prediction"])

        # Summary
        print("\nSUMMARY")
        print("-" * 45)

        print("Total students:", len(results))

        print("Prediction categories:", categories)

        print("Students needing improvement:", len(at_risk))

        # Count students likely to pass
        passed_students = sum(
            1 for student in results
            if student["prediction"] == "Likely to Pass"
        )

        print("Students likely to pass:", passed_students)

        # Save prediction results
        output_file = save_prediction_results(results)

        print("\nResults saved to:", output_file)

    except ValueError:

        print("Invalid input. Please enter numbers correctly.")


if __name__ == "__main__":
    main()
