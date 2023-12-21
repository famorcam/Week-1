# TODO: Create a converter that takes in degrees in Fahrenheit, and prints
# them out in celsius. Use the `input()` function to assist you.
# use documentation and your knowledge of Python to complete this

# consider: what happens if the `input()` function takes in a
# non-numeric answer. How will you handle erroneous values?


def f_to_c_converter(f) :
    f = input("enter temp in Fahrenheit: ")
    f_to_c_converter = (int(f)-32)*5/9
    print(str(f) + ' degrees Fahrenheit is equal to ' + str(f_to_c_converter) + ' degrees celsius')

f_to_c_converter()