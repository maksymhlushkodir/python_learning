class Vehicle:
    def __init__(self, brand: str, model: str, year: int, color: str, max_spead: int):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.max_spead = max_spead
        self._is_engine_on = False

    def start_engine(self):
        self._is_engine_on = True
        print(f'The engine is running. {self._is_engine_on}')

    def stop_engine(self):
        self._is_engine_on = False
        print(f'The engine is stopped. {self._is_engine_on}')

    def get_info(self):
        print(f'{self.brand}\'s car info: model: {self.model}, year: {self.year}, '
              f'color:{self.color}, max spead: {self.max_spead}')

class Car(Vehicle):
    def __init__(self, brand: str, model: str, year: int, color: str, max_spead: int, num_doors: int):
        super().__init__(brand, model, year, color, max_spead)
        self.num_doors = num_doors

    def open_trunk(self):
        print('Opening trunk')

    def get_info(self):
        print(f'{self.brand}\'s car info: model: {self.model}, year: {self.year}, '
              f'color:{self.color}, max spead: {self.max_spead}, num doors: {self.num_doors}')

class Truck(Vehicle):
    def __init__(self, brand: str, model: str, year: int, color: str, max_spead: int,
                 max_load: int, current_load: int):
        super().__init__(brand, model, year, color, max_spead)
        self.max_load = max_load
        self.current_load = current_load

    def load_cargo(self, weight):
        self.current_load += weight
        if self.current_load <= self.max_load:
            print(f'current load: {self.current_load}, max load: {self.max_load}')
        else:
            self.current_load = self.max_load
            print(f'The weight is too heavy. Current load:{self.current_load}'
                  f'max load: {self.max_load}')

    def get_info(self):
        print(f'{self.brand}\'s car info: model: {self.model}, year: {self.year}, '
              f'color:{self.color}, max spead: {self.max_spead}, max load: {self.max_load}'
              f'current load: {self.current_load}')

# Створення об'єктів
my_car = Car("BMW", "model X", 2023, 'Blue', 250, 4)
my_car.start_engine()
my_truck = Truck("Volvo Trucks", "model X", 2015, 'Black', 170, 20000, 0) # 20000 кг

# Дії
my_car.start_engine()
my_car.get_info()
my_car.open_trunk()

print("-" * 20)

my_truck.start_engine()
my_truck.load_cargo(15000)
my_truck.load_cargo(6000) # Спроба перевантаження
my_truck.get_info()