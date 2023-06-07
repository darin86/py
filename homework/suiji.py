import random

def random_number(start, end):
    if start > end:
        start, end = end, start
    return random.randint(start, end)

def number_draw():
    print("Welcome to the Number Draw!")
    start_num = int(input("Enter the start number: "))
    end_num = int(input("Enter the end number: "))
    if start_num >= end_num:
        print("Invalid number range. Please try again.")
        return
    random_num = random_number(start_num, end_num)
    print(f"The random number is: {random_num}")

number_draw()
