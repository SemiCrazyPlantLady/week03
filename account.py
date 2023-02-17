# account.py
# this program allows the user to input their bank account number of 10 digits
# if 10 numbers are not input correctly, the user is forced to try again.
# the program will read back the 10 digit number, only displaying the last 4 digits for security purposes.
# Author Debi Gormley


inputstring = (input('Please enter your 10 digit account number:'))
lengthofstring = len(inputstring)
if(lengthofstring !=10):
    print ('You have entered an incorrect number. The number you entered contained {} digits, your account is 10 digits - please start again!'.format (lengthofstring))
else:
    print ("Your account number is: XXXXXX{} and {} digits in length" .format (inputstring[6:], lengthofstring))
