import customtkinter as ctk

app =ctk.CTk()

app.title("Greetings")
app.geometry("400x300")


label1 = ctk.CTkLabel(master=app, text='What is your name?')
label1.pack(pady=20, padx=20)

entry = ctk.CTkEntry(master=app, placeholder_text='write your name')
entry.pack(pady=20, padx=20)

def get_text():
    text = entry.get()
    label1.configure(text=f'Hello, {text}!')
    print(f"Entry contains: {text}")

button1 = ctk.CTkButton(master=app, text="Click me", command=get_text)
button1.pack(pady=20, padx=20)

app.mainloop()