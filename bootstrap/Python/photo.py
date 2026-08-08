import tkinter as tk
from tkinter import messagebox
from PIL  import image, ImageTk
window = th.TK()
window.title("My Photo Album")
window.geometry("600x600")
file_name = "cat.jpg"
image = Image.open(file_name)
orignal_width, orignal_height = image_size
image_format = image.format
resized_image = image.resize((400, 300))
photo = ImageTk.PhotoImage(resized_image)
title_label = tk.Label(
    window,
    text="My Photo Album",
    font=("Arial", 20, "bold")
)
title_label.pack(pady=15)
image_label = tk.Label(
    window,
    image=photo
)
image_label.pack(pady=10)
def show_information():
    messagebox.showinfo(
        "Photo Information",
        "The photo has been loaded successfully!"
    )
def show_details():
    details_window = tk.Toplevel(window)
    details_window.title("Photo Details")
    details_window.geometry("350x250")
    details = (
        f"File: {file_name}\n"
        f"width: {orignal_width} pixels\n"
        f"height: {orignal_height} pixels\n"
        f"format: {image_format}"
    )
details_label = tk.Label(

details_window,

text=details,

font=("Arial", 12),

justify="left"

)

details_label.pack(pady=30)

close_button = tk.Button(

details_window,

text="Close",

command=details_window.destroy

)

close_button.pack()

info_button = tk.Button(

window,

text="Photo Information",

command=show_information

)

info_button.pack(pady=10)

details_button = tk.Button(

window,

text="Photo Details",

command=show_details

)

details_button.pack(pady=10)

window.mainloop()