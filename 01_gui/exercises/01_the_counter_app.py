import customtkinter as ctk

class CounterApp(ctk.CTk):
    def __init__(self, __count: int=0):
        super().__init__()
        self.__count = __count
        self.title('Counter App')
        self.geometry('600x600')

        # Button
        self.add_button = ctk.CTkButton(
            self,
            text='Addition',
            command=self.button_addition,
            width=200,
            height=60,
            font=('Arial', 24)
        )
        self.add_button.pack(pady=10)

        self.remove_button = ctk.CTkButton(
            self,
            text='Remover',
            command=self.button_remover,
            width=200,
            height=60,
            font=('Arial', 24)
        )
        self.remove_button.pack(pady=10)

        # Label
        self.label = ctk.CTkLabel(
            self,
            text=f'Count: {self.__count}',
            font=('Arial', 36)
        )
        self.label.pack(pady=20)

    @property
    def count(self):
        return self.__count

    def button_addition(self):
        self.__count += 1
        self.label.configure(text=f'Count: {self.__count}')

    def button_remover(self):
        self.__count -= 1
        self.label.configure(text=f'Count: {self.__count}')

if __name__ == '__main__':
    app = CounterApp()
    app.mainloop()