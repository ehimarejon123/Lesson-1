inport tkinter as tk
window = tk.Tk()
window.title("My Profile Card")
window.geometry("400x380")
title = tk.Label(
    window,
    text="MY PROFILE CARD",
    bg="purple",
    fg="white",
    font=("Arial", 16, "bold"),
    padx=10,
    pady=10
)
title.grid(row=0, column=0, columnspan=2, sticky="ew")
tk.Label(window, text="Name:").grid(row=1, column=0, padx=10, pady=10, sticky="w")
name_entry = tk.Entry(window, width=30)
name_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Label(window, text="Hobby:").grid(row=2, column=0, padx=10, pady=10, sticky="w")
hobby_entry = tk.Entry(window, width=30)
hobby_entry.grid(row=2, column=1, padx=10, pady=10)
frame = tk.Frame(window, bd=2, relief="groove")
frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
tk.Label(frame, text="About Me").pack()
about_text = tk.Text(frame, width=35, height=6)
about_text.pack()
def show_card():
    print("Name:", name_entry.get())
    print("Hobby:", hobby_entry.get())
    print("About Me:")
    print(about_text.get("1.0", "end"))
button = tk.Button(window, text="Show My Card", command=show_card)
button.grid(row=4, column=0, columnspan=2, padx=10)
window.mainloop()