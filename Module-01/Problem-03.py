# Check if a string is Palindrome

# madam
# racecar
# level
# mom
# rotator
# wow
# No lemon, no melon

my_str = input('Enter the String to check for Palindrome  : ')

my_str = my_str.casefold()

rev_str = reversed(my_str)

if list(my_str) == list(rev_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
