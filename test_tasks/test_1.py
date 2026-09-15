from typing import Union


ANSWER = {
    "Name": "Alex",
    "Age": 14,
    "Height": 1.89,
    "Is_student": True
}
for key, value in ANSWER.items():
    print(f"{key}: {value}")

a = 5
b = 10
a, b = b, a
print(a, b)

value_1 = "42"
int_value_1 = int(value_1) + 8
float_value_1 = float(int_value_1) / 2
str_value_1 = str(float_value_1) + "!"
print(str_value_1)

PRODUCTS = [
    "яблоко",
    "банан",
]
x = input(">> ")
lst = x.split()
if len(lst) != 3:
    raise ValueError("Нужно все 3 значения!")
product = lst[0]
price = float(lst[1])
number = int(lst[2])
TYPE_VALUES = {
    product: str,
    price: Union[int, float],
    number: int
}
for key, value in TYPE_VALUES.items():
    if not isinstance(key, value):
        raise ValueError(f"Значение {key} не подходит по типу!")
if price < 0 or number < 0:
    raise ValueError("Цифровые значения не могут быть меньше нуля!")
if not product in PRODUCTS:
    raise ValueError("Такого продукта не было найдено!")
print(f"Товар: {product.capitalize()}\n"
      f"Цена за 1 кг: {price}\n"
      f"Количество: {number}\n"
      f"Итого: {price * number}")

y = input(">> ")
if y.isdigit():
    print("int")
elif "." in y and not ".." in y:
    y_1 = y.replace(".", "")
    if y_1.isdigit():
        print("float")
elif y == "True" or y == "False":
    print("bool")
else:
    print("str")

UNITS = {
    "km": 1000,
    "m": 1,
    "sm": 1/100,
    "mi": 1609.34
}
z = input(">> ")
z_lst = z.split()
if len(z_lst) != 2:
    raise ValueError("Должно быть 2 значения для этой задачи!")
value_ee = float(z_lst[0])
unit_of_measurement = z_lst[1].lower()
if not (isinstance(value_ee, float) or isinstance(unit_of_measurement, str)):
    raise ValueError("Значения не удовлетворяют типам данных!")
if not unit_of_measurement in UNITS.keys():
    raise ValueError("Данной единицы измерения не найдено!")
value_22 = value_ee * UNITS[unit_of_measurement]
print(f"{value_ee:.2f} {unit_of_measurement} = {value_22:.2f} m")
