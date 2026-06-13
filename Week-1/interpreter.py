expression = input("Expression: ")
parts = expression.split(" ")

first_number = float(parts[0])
operator = parts[1]
second_number = float(parts[2])

if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "*":
    print(first_number * second_number)
elif operator == "/":
    print(first_number / second_number)