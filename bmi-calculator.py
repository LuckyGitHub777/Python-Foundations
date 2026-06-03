#!/usr/bin/env python3

"""
Simple BMI calculator for learning purposes.

This script demonstrates:
- User input
- Numeric conversion
- Basic arithmetic
- Functions
- Conditional logic
- Simple error handling
"""


def calculate_bmi(weight_kg, height_m):
    """Return BMI rounded to 1 decimal place."""
    if height_m <= 0:
        raise ValueError("Height must be greater than zero.")

    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)


def bmi_category(bmi):
    """Return a simple BMI category string."""
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal weight"
    if bmi < 30:
        return "Overweight"

    return "Obesity"


def main():
    """Run the BMI calculator."""
    try:
        weight = float(input("Enter your weight in kilograms: ").strip())
        height = float(input("Enter your height in meters, for example 1.75: ").strip())
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    try:
        bmi = calculate_bmi(weight, height)
    except ValueError as error:
        print(error)
        return

    category = bmi_category(bmi)

    print(f"\nYour BMI is {bmi}.")
    print(f"Category: {category}")


if __name__ == "__main__":
    main()
