import csv

BONUS = 10

with open("students.csv", "r", newline="") as infile:
    reader = csv.DictReader(infile)

    updated_students = []

    for row in reader:
        grade = int(row["Grade"])
        grade = min(100, grade + BONUS)

        updated_students.append({
            "Name": row["Name"],
            "Grade": grade
        })

with open("updated_students.csv", "w", newline="") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=["Name", "Grade"])

    writer.writeheader()
    writer.writerows(updated_students)

print("Finished! Updated grades saved to updated_students.csv")