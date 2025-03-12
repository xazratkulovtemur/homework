import csv
file_path=r"D:\MAAB academy new\python\homework\lesson-9\homework\grades.csv"
with open(file_path, 'r', encoding='utf-8') as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row)

subject_totals = {}
subject_counts = {}

# Read the CSV file
with open(file_path, 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)  # Read as a list of dictionaries

    for row in reader:
        subject = row["Subject"]
        grade = row["Grade"]

        try:
            score = float(grade.strip())  # Convert grade to float

            if subject not in subject_totals:
                subject_totals[subject] = 0
                subject_counts[subject] = 0

            subject_totals[subject] += score
            subject_counts[subject] += 1
        except ValueError:
            print(f"Skipping invalid value '{grade}' in column Grade")

# Calculate averages
subject_averages = {subject: subject_totals[subject] / subject_counts[subject] for subject in subject_totals}

# Write the results to average_grades.csv
output_file = r"D:\MAAB academy new\python\homework\lesson-9\homework\averagegrades.csv"

with open(output_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Subject", "Average Grade"])

    for subject, avg in subject_averages.items():
        writer.writerow([subject, round(avg, 2)])

print(f"Average grades saved to {output_file}")