from abc import ABC, abstractmethod
from datetime import datetime

class Person:
    def __init__(self, person_id: int, first_name: str, last_name: str):
        self._person_id = person_id
        self._first_name = first_name
        self._last_name = last_name

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @first_name.setter
    def first_name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("The name must be a string")
        if len(value.strip()) < 2:
            raise ValueError("Length must be at least 2 characters")
        self._first_name = value

    @last_name.setter
    def last_name(self, value: str):
        if not isinstance(value, str):
            raise TypeError("The name must be a string")
        if len(value.strip()) < 2:
            raise ValueError("Length must be at least 2 characters")
        self._last_name = value

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    def __str__(self):
        return f"Person: {self.full_name} (ID: {self._person_id})"


class LibraryItem(ABC):
    def __init__(self, inventory_number: int, title: str, status: str):
        self._inventory_number = inventory_number
        self._title = title
        self._status = status

    @abstractmethod
    def get_description(self):
        pass

    def check_out(self):
        if self._status == "available":
            self._status = "issued"
            return self._status
        else:
            return self._status

    def check_in(self):
        if self._status == "issued":
            self._status = "available"
            return self._status
        else:
            return self._status

    def __eq__(self, other):
        if not isinstance(other, LibraryItem):
            return False
        return self._inventory_number == other._inventory_number


class Book(LibraryItem):
    def __init__(self, _inventory_number: int, _title: str, _status: str,
             author: str, isbn: str, year: int, genre: str):
        super().__init__(_inventory_number, _title, _status)
        self._author = author
        self._isbn = isbn
        self._year = year
        self._genre = genre

    def get_description(self):
        return {
            "type": "book",
            "inventory_number": self._inventory_number,
            "title": self._title,
            "status": self._status,
            "author": self._author,
            "isbn": self._isbn,
            "year": self._year,
            "genre": self._genre
        }

    def __str__(self):
        return (
            f"Type: book\n"
            f"Inventory Number: {self._inventory_number}\n"
            f"Title: {self._title}\n"
            f"Status: {self._status}\n"
            f"Author: {self._author}\n"
            f"Isbn: {self._isbn}\n"
            f"Year: {self._year}\n"
            f"Genre: {self._genre}\n"
        )

    def __repr__(self):
        return (f"Book(_inventory_number = '{self._inventory_number}',"
                f" _title = '{self._title}', _status = '{self._status}',"
                f" _author = '{self._author}', _isbn = '{self._isbn}',"
                f" _year = '{self._year}', _genre = '{self._genre}')")


class Magazine(LibraryItem):
    def __init__(self, _inventory_number: int, _title: str,
             _status: str, issue_number: int):
        super().__init__(_inventory_number, _title, _status)
        self._issue_number = issue_number

    def get_description(self):
        return {
            "type": "magazine",
            "inventory_number": self._inventory_number,
            "title": self._title,
            "status": self._status,
            "issue_number": self._issue_number
        }

    def __str__(self):
        return (
            f"Type: magazine\n"
            f"Inventory Number: {self._inventory_number}\n"
            f"Title: {self._title}\n"
            f"Status: {self._status}\n"
            f"Issue Number: {self._issue_number}\n"
        )

    def __repr__(self):
        return (f"Magazine(_inventory_number = '{self._inventory_number}',"
                f" _title = '{self._title}', _status = '{self._status}',"
                f" _issue_number = '{self._issue_number}')")


class Reader(Person):
    def __init__(self, _person_id: int, _first_name: str, _last_name: str):
        super().__init__(_person_id, _first_name, _last_name)
        self._reader_id = _person_id
        self._borrowed_books = []

    def borrow_book(self, book):
        if book._status == "available":
            book._status = "issued"
            self._borrowed_books.append(book)
            return f"The book was issued"
        else:
            return f"Book not available"

    def return_book(self, book):
        if book in self._borrowed_books:
            book._status = "available"
            self._borrowed_books.remove(book)
            return f"The book was returned"
        else:
            return f"You did not take this book"

    def get_borrowed_books(self):
        return self._borrowed_books

    def __str__(self):
        return (f"Full Name: {self._first_name} {self._last_name}\n"
                f"ID: {self._person_id}\n")


class Employee(Person, ABC):
    def __init__(self, _person_id: int, _first_name: str,
                 _last_name: str, department: str, salary: int):
        super().__init__(_person_id, _first_name, _last_name)
        self._employee_id = _person_id
        self._department = department
        self._salary = salary

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("The salary should be a number")
        if value < 0:
            raise ValueError("The salary cannot be negative")
        self._salary = value

    def calculate_tax(self):
        return self._salary * 0.13

    @abstractmethod
    def work(self):
        pass

    def __str__(self):
        return (f"Employee ID: {self._employee_id}\n"
                f"Department: {self._department}\n"
                f"Salary: {self._salary}\n")


class Transaction:
    def __init__(self, transaction_id: int, reader: Reader, item: LibraryItem):
        self._transaction_id = transaction_id
        self._reader = reader
        self._item = item
        self._date_borrowed = datetime.now()
        self._date_returned = None
        self._is_closed = False

    def close_transaction(self):
        if not self._is_closed:
            self._date_returned = datetime.now()
            self._is_closed = True
            return f"The transaction #{self._transaction_id} closed"
        return "The transaction has already been closed"

    def calculate_fine(self, daily_fine: float = 10.0) -> float:
        if not self._is_closed:
            days_overdue = (datetime.now() - self._date_borrowed).days - 14
            if days_overdue > 0:
                return days_overdue * daily_fine
        return 0.0


    def __str__(self):
        return (f"Transaction ID: {self._transaction_id}\n"
                f"Reader: {self._reader}\n"
                f"Item: {self._item}\n"
                f"Date Borrowed: {self._date_borrowed}\n"
                f"Date Returned: {self._date_returned}\n")


class Library:
    def __init__(self):
        self._catalog = []
        self._readers = {}
        self._employees = []
        self._transactions = []

    def add_item(self, item: LibraryItem):
        self._catalog.append(item)

    def register_reader(self, reader: Reader):
        self._readers[reader._reader_id] = reader

    def add_employee(self, employee: Employee):
        self._employees.append(employee)

    def find_item_by_title(self, title: str):
        results = []
        for item in self._catalog:
            if title.lower() in item._title.lower():
                results.append(item)
        return results

    def find_item_by_inventory_number(self, inventory_number: int):
        for item in self._catalog:
            if item._inventory_number == inventory_number:
                return item
        return None

    def __str__(self):
        return (f"Catalog: {self._catalog}\n"
                f"Readers: {self._readers}\n"
                f"Employees: {self._employees}\n"
                f"Transactions: {self._transactions}\n")