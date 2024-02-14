
while 5<10:
    operator = input("What operator would you like to use:\n+\n-\n*\n/\n//\n**\n%\n")
    if operator == "break":
        break
    else:
        print(f"Invalid operator: \'{operator}\'")
        continue

        print(f"Invalid operator: \'{operator}\'")
    num1 = float(input("Input first number:"))
    num2 = float(input("Input second number:"))
    if operator == "+":
        plus = num1 + num2
        print(plus)
    elif operator == "-":
        minus = num1 - num2
        print(minus)
    elif operator == "*":
        multi = num1 * num2
        print(multi)
    elif operator == "/":
        div = num1 / num2
        print(div)
    elif operator == "//":
        rem = num1 // num2
        print(rem)
    elif operator == "**":
        power = num1 ** num2
        print(power)
    else:
        modulo = num1 % num2
        print(modulo)

