#   Grocery Receipt
#   Your groceries ring up as 5.63, 13.40, 3.99, 4.57, and 2.47, respectively.
#   Use the 5 items you printed in Q1 and declare them as variables. Assign each variable with a price listed above.
#   Use Python as a calculator to add your variables together and print out the total cost of all the items.

Thing1 = 5.63
Thing2 = 13.4
Thing3 = 3.99
Thing4 = 4.57
Thing5 = 2.47 
print(Thing1 + Thing2 + Thing3 + Thing4 + Thing5, 2)

#   Rounded to two decimal places using round() function:
print(round(Thing1 + Thing2 + Thing3 + Thing4 + Thing5, 2))

#   Rounded to two decimal places using format():
print("{:.2f}".format(Thing1 + Thing2 + Thing3 + Thing4 + Thing5))

#   Rounded to two decimal places using %.2f:
print ("%.2f" % (Thing1 + Thing2 + Thing3 + Thing4 + Thing5))
#   Print recognizes: % = special chacater, f = floating type, .2 = two digits after decimal