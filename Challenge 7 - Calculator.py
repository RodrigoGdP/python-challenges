def calc (num1, op, num2):
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "/":
        result = num1 / num2
    elif op == ".":
        result = num1 * num2
    return result

num1 = int(input("\n\nType the first number number:\n\n"))
op = input("\nChoose operator (+ - / x)\n\n")
num2 = int(input("\nType the second number\n\n"))
print (f"\nResult: {num1} {op} {num2} = {calc(num1, op, num2)}")