import customtkinter as ctk
# from api_core.weather_api import WeatherService  # Імпортуємо твій майбутній клас API


class WeatherApp:
    def __init__(self):
        # Налаштування вікна
        self.root = ctk.CTk()
        self.root.title("Weather App by Maksym")
        self.root.geometry("400x500")

        # Створюємо екземпляр сервісу погоди (поки без логіки)
        # self.weather_service = WeatherService()

    def run(self):
        print("Програма запускається...")  # Тепер ти побачиш це в консолі
        self.root.mainloop()  # Це "магічна" команда, яка тримає вікно відкритим