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


class ToDoApp(ctk.CTk):
    def __init__(self, tasks: list=None):
        super().__init__()
        self.tasks = tasks
        if tasks is None:
            self.tasks = []

        # App
        self.title('To-Do List')
        self.geometry('500x600')

        self.entry = ctk.CTkEntry(
            self,
            placeholder_text='What needs to be done?',
            width=350,
            font=('Arial', 24)
        )
        self.entry.pack(padx=20, pady=20)

        self.button_add_task = ctk.CTkButton(
            self,
            text='Add Task',
            command=self.add_task,
            font=('Arial', 24)
        )
        self.button_add_task.pack(padx=20, pady=5)

        self.scrollable_frame = ctk.CTkScrollableFrame(
            self,
            width=450,
            height=400,
            label_text="Active Tasks"
        )
        self.scrollable_frame.pack(padx=20, pady=20, fill="both", expand=True)

    def add_task(self):
        task_text = self.entry.get()
        if task_text:
            new_task = Task(self.scrollable_frame, task_text)
            new_task.pack(padx=10, pady=5, fill="x")
            self.entry.delete(0, 'end')


if __name__ == '__main__':
    app = ToDoApp()
    app.mainloop()