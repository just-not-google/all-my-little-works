from typing import Dict


fruits = ["яблоко", "банан", "груша"]
point = (3, 7)
student = {"name": "Alex", "age": 14}
numbers = {1, 2, 3, 2, 1}
print(fruits, type(fruits))
print(point, type(point))
print(student, type(student))
print(numbers, type(numbers))

nums = [10, 20, 30, 40, 50]
print(nums[0], nums[-1])
nums.append(60)
nums[1] = 25
print(len(nums), nums)

data = [4, 8, 15, 16, 23, 42, 8, 4, 15]
a = sum(data)
print(a, a / len(data))
print(min(data), max(data))
print(list(set(data)))
print(data.count(8))

phone_book = {
    "Alex": "+7-900-111-22-33",
    "Maria": "+7-900-444-55-66",
    "Ivan": "+7-900-777-88-99"
}
def add_contact(book: Dict[str, str], name, phone):
    if name in book.keys():
        return False
    book.update({name: phone})
def find_contact(book: Dict[str, str], name):
    try:
        return book[name]
    except KeyError:
        return "не найден"
def delete_contact(book: Dict[str, str], name):
    if name in book.keys():
        book.pop(name)
add_contact(phone_book, "Pidor", "+7000")
find_contact(phone_book, "Maria")
delete_contact(phone_book, "Ivan")

x = input(">> ").lower().strip()
x_lst = x.split()
print(x_lst)
print(set(x_lst))
answer = dict()
for i in x_lst:
    answer.update({i: x_lst.count(i)})
print(answer)