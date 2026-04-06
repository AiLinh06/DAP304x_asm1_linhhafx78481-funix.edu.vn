# Exam Grading Program

A Python program designed to automate the grading of student multiple-choice exams. The script processes class data files, validates student information, calculates scores based on a fixed answer key, and generates detailed statistical reports and grade files.

## Features

- **Data Validation**: Automatically checks each line of data for:
  - Exact column count (Student ID + 25 answers).
  - Valid Student ID format (Starts with 'N' followed by 8 digits).
- **Automated Grading**:
  - Correct answer: **+4 points**
  - Incorrect answer: **-1 point**
  - Skipped answer: **0 points**
- **Statistical Reporting**:
  - Total valid/invalid records.
  - Number of students with high scores (>= 80).
  - Average, highest, lowest, range, and median scores.
- **Detailed Question Analysis**:
  - Identifies which questions were skipped by the most students.
  - Identifies which questions were answered incorrectly by the most students.
- **Result Export**: Saves results as a `.txt` file (e.g., `class1_grades.txt`).

## Requirements

The program requires the following Python libraries:
- `pandas`
- `numpy`

You can install them using pip:
```bash
pip install pandas numpy
```

## How to Prepare Your Data

1. Create a folder named `Data Files/` in the same directory as the script.
2. Place your class text files (e.g., `class1.txt`, `class2.txt`) inside that folder.
3. Each line in the file should follow this format:
   `Student_ID,Answer1,Answer2,...,Answer25`

## How to Run

1. Open your terminal or command prompt.
2. Run the script:
   ```bash
   python lastname_firstname_grade_the_exams.py
   ```
3. When prompted, enter the filename (e.g., `class1.txt`).

## Output Files

After processing, the program will generate a result file in the same directory as the script with the naming convention `[filename]_grades.txt`. This file contains the Student ID and their final score on each line.

## Author

Developed by [Your Name] for the DAP304x Assignment.
