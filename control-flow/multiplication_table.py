#!/usr/bin/python3
"""
Multiplication Table Generator
Generates and prints the multiplication table for a given number from 1 to 10
"""

# Get user input
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print multiplication table using for loop
print(f"\nMultiplication table for {number}:")
for i in range(1, 11):
    product = number * i
    print(f"{number} * {i} = {product}")