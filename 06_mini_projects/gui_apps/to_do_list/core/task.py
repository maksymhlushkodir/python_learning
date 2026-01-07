import customtkinter as ctk

class Task(ctk.CTkFrame):
    def __init__(self, master, task_text: str):
        super().__init__(master)
        self.task_text = task_text

        # Label
        self.label = ctk.CTkLabel(self, text=task_text, font=('Arial', 24))
        self.label.pack(side='left', padx=20, pady=20)

        # Delete button
        self.delete_button = ctk.CTkButton(
            self,
            text='Done',
            command=self.destroy,
            width=70,
            height=35,
            font=('Arial', 18),
            hover_color="darkgreen"
        )
        self.delete_button.pack(side='right', padx=10, pady=10)