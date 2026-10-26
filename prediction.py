
# prediction.py

PASS_MARKS = 35
MIN_ATTENDANCE = 75
MIN_STUDY_HOURS = 1


class StudentPerformance:

    def __init__(self, student):
        self.student = student

    def predict(self):

        marks = float(self.student["marks"])
        attendance = float(self.student["attendance"])
        study_hours = float(self.student["study_hours"])

        if (
            marks >= PASS_MARKS
            and attendance >= MIN_ATTENDANCE
            and study_hours >= MIN_STUDY_HOURS
        ):
            return "Likely to Pass"

        return "Needs Improvement"


def predict_students(students):

    results = []

    for student in students:

        model = StudentPerformance(student)

        prediction = model.predict()

        # Preserve register number and all other details
        result = student.copy()

        result["prediction"] = prediction

        results.append(result)

    # Sort by marks
    results.sort(
        key=lambda student: float(student["marks"]),
        reverse=True
    )

    # Students needing improvement
    at_risk = [
        student for student in results
        if student["prediction"] == "Needs Improvement"
    ]

    # Prediction categories
    categories = set(
        student["prediction"]
        for student in results
    )

    return results, at_risk, categories
