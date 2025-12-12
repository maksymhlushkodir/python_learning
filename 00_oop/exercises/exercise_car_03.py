class Car:
    wheels = 4

    def __init__(self, brand: str, model: str, year: int, color: str, fuel: float, max_fuel: float):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.fuel = fuel
        self.max_fuel = max_fuel
        self._is_engine_on = False

    def start_engine(self):
        if self._is_engine_on: # 1. Перевірка: Якщо вже працює
            print(f'{self.brand}\'s engine is already running.')
        elif self.fuel <= 2.00: # 2. Перевірка: Чи достатньо палива
            print('Not enough fuel to start engine')
        else: # 3. Якщо вимкнений І палива достатньо
            self._is_engine_on = True
            self.fuel -= 0.1 # Можна додати невелику витрату палива на запуск
            print(f'{self.brand}\'s engine started! Fuel left: {self.fuel:.2f}L')

    def fill_up_car(self):
        # Скільки літрів ще можна залити
        space_left = self.max_fuel - self.fuel

        if space_left == 0:
            print(f'{self.brand}\'s tank is already full ({self.fuel:.2f}L).')
            return # Зупиняємо виконання методу

        print(f'Space left in tank: {space_left:.2f} liters. You currently have {self.fuel:.2f}L.')
        try:
            # Зчитуємо вхідні дані і перетворюємо їх на float
            fuel_choice = float(input('How many liters do you want to fill? '))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return

        if fuel_choice > space_left:
            # Якщо користувач хоче залити більше, ніж влізе
            self.fuel = self.max_fuel
            print(f'Filled {space_left:.2f}L. The tank is now full: {self.fuel:.2f}L.')
        elif fuel_choice > 0:
            # Якщо все добре, додаємо паливо
            self.fuel += fuel_choice
            print(f'Successfully filled {fuel_choice:.2f}L. Current fuel: {self.fuel:.2f}L.')
        else:
            print("Invalid amount.")

    def get_info(self):
        print(f'{self.brand}\'s car info: model: {self.model}, year: {self.year}, '
              f'color:{self.color}, fuel: {self.fuel:.2f}, max fuel: {self.max_fuel:.2f}')

my_dream_car = Car('GTR', 'r34', 2001, 'Blue', 1.98, 72.00)
my_dream_car.start_engine()
my_dream_car.fill_up_car()
my_dream_car.start_engine()
my_dream_car.get_info()