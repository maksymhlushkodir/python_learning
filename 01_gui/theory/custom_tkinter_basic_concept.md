# Basic Concepts of CustomTkinter
To feel confident, focus on these three topics:

## 1. Widgets
These are the "building blocks" of your interface. The most important ones:

- **`CTkButton`** — Button

- **`CTkLabel`** — Text / Label

- **`CTkEntry`** — Text input field

- **`CTkCheckBox`** — Checkbox

## 2. Geometry (Placement)
How to arrange elements in a window. There are two main methods:

- **`.pack()`** — simply places elements one after another (or in a specified direction).

- **`.grid()`** — allows placing elements in a table layout (rows and columns). This is much more convenient for complex projects.

## 3. Functions (Callbacks)
How to make a button do something:

Write a regular Python function.

"Bind" it to the **`command`** parameter in the widget (for example, a button).