"""Power of 4
Write a method to determine whether a given integer (zero or positive number) is a power of 4
without using the multiply or divide operator. If it is, return True, else return False.
Examples:
is_power_of_four(5) ==> False
is_power_of_four(16) ==> True
"""

# bit manipulation
def is_power_of_four(number):
    test = 1
    while test < number:
        test = test << 2
    return test == number

# Repeatedly divide y into x.The first time you get a non-zero remainder you know x is not an integer power of y.
def is_power_of_four(x):
    y = 4
    while x % y == 0:
        x = x / y
    return x == 1

print(is_power_of_four(1))
print(is_power_of_four(4))
print(is_power_of_four(16))
print(is_power_of_four(1024))
print(is_power_of_four(2048))