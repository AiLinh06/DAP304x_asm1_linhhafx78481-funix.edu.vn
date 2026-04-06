import pandas as pd
import numpy as np
import re

def file_process():
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    answer_key_array = answer_key.split(",")
    filename = input("\nEnter the filename: ")
    try:
        # Construct path to the Data Files directory
        file_path = "Data Files/" + filename
        with open(file_path, 'r') as file:
            print(f"\nSuccessfully opened {filename}.") 
            print("\n**** ANALYZING ****")
            
            invalid_lines = 0
            valid_lines = 0
            processed_data = [] # Array to store all valid split lines
            
            for line in file:
                line = line.strip()
                if not line:
                    continue # Skip empty lines
                
                arr = line.split(",")
                
                if len(arr) != 26:
                    print("\nInvalid line of data: does not contain exactly 26 values:\n")
                    print(line)
                    invalid_lines += 1
                elif not re.match(r"N\d{8}$", arr[0]):
                    print("\nInvalid line of data: N# is invalid\n")
                    print(line)
                    invalid_lines += 1
                else:
                    valid_lines += 1
                    processed_data.append(arr) # Store the split array
            
            if(invalid_lines == 0):
                print("\n No errors found!")
           
           # Calculate scores for each student
            student_scores = []
            high_score = 0
            skip_question = []
            wrong_question = []
            for answer in processed_data:
                score = 0
                for i in range(25):
                    if(answer[i+1] == answer_key_array[i]):
                        score += 4
                    elif(answer[i+1] != "" and answer[i+1] != answer_key_array[i]):
                        score -= 1
                        wrong_question.append(i+1)
                    else:
                        skip_question.append(i+1)
                if(score >= 80):
                    high_score += 1
                student_tuple = (answer[0], score)
                student_scores.append(student_tuple)
            
            skip_question.sort()
            wrong_question.sort()

            skip_question_count_dict = {}
            wrong_question_count_dict = {}
            
            # Count the number of skipped and wrong answers for each question
            for i in range(len(skip_question)):
                if skip_question[i] in skip_question_count_dict:
                    skip_question_count_dict[skip_question[i]] += 1
                else:
                    skip_question_count_dict[skip_question[i]] = 1
            for i in range(len(wrong_question)):
                if wrong_question[i] in wrong_question_count_dict:
                    wrong_question_count_dict[wrong_question[i]] += 1
                else:
                    wrong_question_count_dict[wrong_question[i]] = 1
            
            # Create and print results DataFrame
            df = pd.DataFrame(student_scores, columns=['Student ID', 'Score'])
                
            print("\n**** REPORT ****")
        
            print("\nTotal valid lines: ", valid_lines)
            print("\nTotal invalid lines: ", invalid_lines)
            print("\nTotal student of high scores: ", high_score)
            print("\nAverage Score: ", round(df['Score'].mean(), 2))
            print("\nHighest Score: ", max(df['Score']))
            print("\nLowest Score:", min(df['Score']))
            print("\nRange of Scores: ", max(df['Score'])-min(df['Score']))
            print("\nMedian Score: ", df['Score'].median(), "\n")

            print("\n**** SKIP QUESTION ****")
            max_skip_value = max(skip_question_count_dict.values())
            max_skip_question = []
            for key, value in skip_question_count_dict.items():
                if value == max_skip_value:
                    max_skip_question.append(key)
            
           
            print("\nQuestion that most people skip: ")
            for i in range(len(max_skip_question)):
                print( max_skip_question[i], "-", max_skip_value, "-", round(max_skip_value/len(student_scores), 2))
                    
            
            print("\n**** WRONG QUESTION ****")
            max_wrong_value = max(wrong_question_count_dict.values())
            max_wrong_question = []
            for key, value in wrong_question_count_dict.items():
                if value == max_wrong_value:
                    max_wrong_question.append(key)
           
            
            print("\nQuestion that most people wrong: ")
            for i in range(len(max_wrong_question)):
                print( max_wrong_question[i], "-", max_wrong_value, "-", round(max_wrong_value/len(student_scores), 2))
                    
            
            # Exporting results to a file
            output_filename = filename.replace(".txt", "_grades.txt")
            with open(output_filename, 'w') as f:
                for item in student_scores:
                    f.write(f"{item[0]},{item[1]}\n")
            print(f"\nResults saved to: {output_filename}")
            
            return processed_data


    except FileNotFoundError:
        print("The file was not found.")
        

# Execute the file processing
all_lines_array = file_process()





