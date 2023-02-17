# account.py
# this program allows the user to input their bank account number of any length greater than 5 digits (we have at least one digit secured! not very secure...)
# the assumption is that the user can have a infinite numberical input (note it is not advised to have extended length bank account numbers as they charge per page of statements)
# the program will read back the input number, only displaying the last 4 digits for security purposes.
# Author Debi Gormley


inputstring = (input('Please enter your account number:'))
lengthofstring = len(inputstring)
output = 4
if lengthofstring <= output:
    print('Sorry - your account number it too short for security purposes, please make sure to enter 5 digits or more')
else:
    security = lengthofstring - output
    mystring = 'X' * security
    print ('Your secure account number is: '+ mystring + (inputstring[security:] ))
