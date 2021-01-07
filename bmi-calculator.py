#!/usr/bin/python

def calculate_bmi(height, weight):
    BMI = (weight * 703 / (height  *height))

    if BMI < 18.5:
        return 'Your BMI is ' + str(BMI) +'. Thats Under-weight.'
    if BMI >= 18.5 and BMI < 25 :
        return 'Your BMI is ' + str(BMI) +'. Thats a Normal Weight.'
    if BMI > 25:
        return 'Your BMI is ' + str(BMI) +'. Thats Over-weight.'
    return BMI

height = input("Enter your height: ")
weight = input("Enter your weight: ")
height = int(height)
weight = int(weight)

print (calculate_bmi(height, weight))
