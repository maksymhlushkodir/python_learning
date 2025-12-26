import customtkinter as ctk

# 1. Creating the main window
app = ctk.CTk()
app.title("Simple Window")
app.geometry("400x240")

# 2. Adding elements (widgets)
label = ctk.CTkLabel(app, text="Hello, this is CustomTkinter")
label.pack(pady=20) # Placing an element with an indent

button = ctk.CTkButton(app, text="Click me")
button.pack(pady=10)

# 3 Starting the event processing loop
app.mainloop()