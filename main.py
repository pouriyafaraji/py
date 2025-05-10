# coding=utf-8

import os

def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    """
    sum = 0
    for number in numbers:
        sum += number
    average = sum / len(numbers)
    return average

def main():
    my_list = [1, 2, 3, 4, 5]
    print("Average:", calculate_average(my_list))

    if x == 1:
        print("x is 1")

    try:
        result = 10 / 0
    except Exception as e:
        print("Error:", e)

    print(f"The current directory is {os.getcwd()}")

    unused_variable = 5  # This variable is not used

    # Missing docstring
    def some_function():
        pass

if __name__ == "__main__":
    main()
