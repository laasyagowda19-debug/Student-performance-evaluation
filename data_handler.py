
import csv
from pathlib import Path

# Project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Data folders
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "output"

# CSV files
INPUT_FILE = DATA_DIR / "student_data.csv"
OUTPUT_FILE = OUTPUT_DIR / "student_results.csv"

# Student fields
FIELDS = [
    "name",
    "register_no",
    "marks",
    "attendance",
    "study_hours"
]


# Save student details
def save_student_data(students):

    DATA_DIR.mkdir(parents=True, exist_ok=True)

    with open(INPUT_FILE, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=FIELDS
        )

        writer.writeheader()
        writer.writerows(students)

    print("Student data saved successfully.")


# Load student details
def load_student_data():

    if not INPUT_FILE.exists():
        return []

    students = []

    with open(INPUT_FILE, "r", newline="", encoding="utf-8") as file:

        reader = csv.DictReader(file)

        for row in reader:

            student = {
                "name": row["name"],
                "register_no": row["register_no"],
                "marks": float(row["marks"]),
                "attendance": float(row["attendance"]),
                "study_hours": float(row["study_hours"])
            }

            students.append(student)

    return students


# Save prediction results
def save_prediction_results(results):

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    result_fields = FIELDS + ["prediction"]

    with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=result_fields
        )

        writer.writeheader()
        writer.writerows(results)

    print("Prediction results saved successfully.")

    return OUTPUT_FILE
