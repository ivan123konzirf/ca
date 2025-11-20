# Простой калькулятор
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

print("Выберите операцию:")
print("+ - сложение")
print("- - вычитание")
print("* - умножение")
print("/ - деление")

operation = input("Операция: ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Ошибка: деление на ноль!"
else:
    result = "Неверная операция"

print(f"Результат: {result}")