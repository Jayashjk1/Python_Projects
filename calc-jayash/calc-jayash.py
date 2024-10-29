# !--Python_Calculator--!

operator = ('+', '-', '*', '/', '%')

def exit_calculator():
    print('!--Thanks, For Using Our Calculator, Have a nice Day--!')
    exit()

print('!--Welcome To Our Calculator--!')
for i in range(99):
    print('!-~-~-~-~-~-~-~-~-~-~-~-~-!')

    Q = input('Press (Q) to Quit, otherwise Press (Enter) to Continue :')
    if Q.lower() == 'q':
        exit_prompt = input("Do you want to Quit? ((Y) to Exit, (N) to Continue): ")
        if exit_prompt.lower() == 'y':
            exit_calculator()

        else:
            print('!!ERROR!!: InValid Option')
            continue  

    num1 = float(input('Please enter the first number: '))
    sign = input('Please enter an operator (+, -, *, /, %) :')
    num2 = float(input('Please enter the second number: '))

    if sign == '+':
        result = num1 + num2
        print("Result:", result)

    elif sign == '-':
        result = num1 - num2
        print("Result:", result)

    elif sign == '*':
        result = num1 * num2
        print("Result:", result)

    elif sign == '/':
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("!!Error!!: Division by zero is not allowed.")

    elif sign == '%':
        if num2 != 0:
            result = (num1 / num2) * 100
            print(f"{num1} is {result}% of {num2}")
        else:
            print("!!Error!!: Division by zero is not allowed.")
