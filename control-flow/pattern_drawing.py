#!/usr/bin/python3
"""
Pattern Drawing Program
Draws a square pattern of asterisks based on user input size
"""

# Get user input
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Draw pattern using while loop for rows
while row < size:
    # Use for loop for columns
    for col in range(size):
        print("*", end="")
    # Move to next line after completing a row
    print()
    # Increment row counter
    row += 1