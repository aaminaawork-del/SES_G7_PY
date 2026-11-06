# Grade 7 Python Program: Comments, Type Conversion, Assignment Operators, and Conditional Statements
# Reference: Programming in Python

"""
Multi-line comment:
This program manages student scores, applies bonus points using 
assignment operators, and evaluates grade categories using conditional statements.
"""  

# Taking user input and converting data types
name = input("Enter student name: ")  
marks = float(
    input("Enter marks obtained (out of 100): ")
)  

# Assignment Operators (+=)
bonus_marks = 5
marks += bonus_marks  # Adds 5 bonus points (equivalent to marks = marks + 5)
print(f"Marks after adding {bonus_marks} bonus points: {marks}")

# Floor Division Assignment Operator (//=)
score_level = marks
score_level //= 10
print(f"Floor division score level (score // 10): {score_level}")

# Conditional Statements (if, if-elif-else ladder)
print("\n--- Grade Evaluation Report ---")
if marks >= 90:  
  print(f"Grade: A+ (Outstanding performance, {name}!)")
elif marks >= 75:  
  print(f"Grade: A (Very Good, {name}!)")
elif marks >= 50:  
  print(f"Grade: B (Good Effort, {name}!)")
else:  
  print(f"Grade: Needs Improvement. Keep practicing, {name}!")  
