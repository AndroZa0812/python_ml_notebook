inp = input("Please enter the string to check for palindrome:")

if inp == inp[::-1]:
    print("This is a polindrome")
else:
    print("This is not a polindrome")
