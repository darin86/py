print("我可以为你做以下事情：\n")
print("1:简易计算器\n")
print("2:随机抽数\n")
print("3:今天吃什么\n")
ch=int(input("请输入指令："))
if ch==1:
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def calculator():
        print("Welcome to the Calculator!")
        print("Operations:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        operation = input("Enter the operation number (1-4): ")

        if operation not in ['1', '2', '3', '4']:
            print("Invalid operation number. Please try again.")
            return

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if operation == '1':
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif operation == '2':
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif operation == '3':
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif operation == '4':
            result = divide(num1, num2)
            if isinstance(result, str):
                print(result)
            else:
                print(f"Result: {num1} / {num2} = {result}")
                
    calculator()
    print("Powered by Darin_Wong")

elif ch==2:
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
    print("Powered by Darin_Wong")
elif ch==3:
    import random

    food_options = ["Pizza", "Sushi", "Burger", "Tacos", "Pasta", "Salad"] 
    def decide_what_to_eat():
        print("Welcome to the Food Lottery!")
        print("Today's food options are:")
        for food in food_options:
            print("- " + food)
        print("Let's decide what to eat!")

        winner = random.choice(food_options)
        print("The winner is: " + winner)

    decide_what_to_eat()
    print("Powered by Darin_Wong")