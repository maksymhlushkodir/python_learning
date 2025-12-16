
class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def get_details(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}'

class FictionBook(Book):
    def __init__(self, title: str, author: str, year: int, genre: str):
        super().__init__(title, author, year)
        self.genre = genre

    def get_details(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}, Genre: {self.genre}'

class Textbook(Book):
    def __init__(self, title: str, author: str, year: int, subject: str):
        super().__init__(title, author, year)
        self.subject = subject

    def get_details(self):
        return f'Title: {self.title}, Author: {self.author}, Year: {self.year}, Subject: {self.subject}'

class Library:
    def __init__(self, name: str, inventory: list = None):
        self.name = name
        self.inventory = inventory
        if inventory is None:
            self.inventory = []

    def add_book(self, book_object: Book):
        self.inventory.append(book_object)

    def show_inventory(self):
        for i in self.inventory:
            print(i.get_details())

    def search_by_author(self, author_name: str):
        # Створюємо порожній список для результатів
        found_books = []
        for book in self.inventory:
            if book.author == author_name:
                found_books.append(book.get_details())
        return found_books  # Повертаємо список


# Створення об'єктів книг
fiction1 = FictionBook("Володар Перснів", "Дж.Р.Р. Толкін", 1954, "Фентезі")
textbook1 = Textbook("Алгебра 10 клас", "Іванов І.І.", 2022, "Математика")
fiction2 = FictionBook("Дванадцять стільців", "Ільф і Петров", 1928, "Сатира")

# Створення об'єкта бібліотеки
my_library = Library("Центральна Міська Бібліотека")

# Додавання книг
my_library.add_book(fiction1)
my_library.add_book(textbook1)
my_library.add_book(fiction2)

# Перевірка інвентарю
my_library.show_inventory()

# Пошук
print("\n--- Пошук ---")
search_result = my_library.search_by_author("Дж.Р.Р. Толкін")
print(search_result)