import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
root.geometry("1370x870")
root.title("Match play-off")
root.resizable(False,False)

image_file = Image.open("stadium.png")
image = ImageTk.PhotoImage(image_file)
image2_file = Image.open("ticket.png")
image2 = ImageTk.PhotoImage(image2_file)

image_label = tk.Label(root, image=image)
image_label.place(x=0, y=0, relwidth=1, relheight=1)


def button_clicked(button_number):
    window = tk.Toplevel()
    window.geometry("600x225")
    window.title("TICKET")
    window.resizable(False,False)
    image_label = tk.Label(window, image=image2)
    image_label.place(x=0, y=0, relwidth=1, relheight=1)
    message1 = f"TICKET NUMERO {button_number} "
    message_label = tk.Label(window, text=message1, font=("Arial", 12))
    message_label.place(relx=0.55, rely=0.1, anchor=tk.CENTER)
    message2 = f"PLAY-OFF MATCH DE RETOUR"
    message_label = tk.Label(window, text=message2, font=("Arial", 12))
    message_label.place(relx=0.55, rely=0.2, anchor=tk.CENTER)
    message = f"MARDI 09 MAI 2023 A 14:00H"
    message_label = tk.Label(window, text=message, font=("Arial", 10))
    message_label.place(relx=0.55, rely=0.95, anchor=tk.CENTER)
    cancel_button = tk.Button(window, text="valider La Réservation", command=window.destroy)
    cancel_button.place(relx=0.55, rely=0.8, anchor=tk.CENTER)
    buttons[button_number+1].configure(bg="red")

buttons = []

button_frame = tk.Frame(root, bg="#ECE5CB")
button_frame.pack(side=tk.TOP, pady=100)

for i in range(18):
    button = tk.Button(button_frame, text=f"Chaise {i+1}", bg="green", fg="white",
                       command=lambda num=i+1: button_clicked(num),width=8, height=3)
    button.grid(row=0, column=i, padx=5, pady=5)
    buttons.append(button)
for i in range(18):
    button = tk.Button(button_frame, text=f"Chaise {i+17}", bg="green", fg="white",
                       command=lambda num=i+17: button_clicked(num),width=8, height=3)
    button.grid(row=1, column=i, padx=5, pady=5)
    buttons.append(button)
for i in range(18):
    button = tk.Button(button_frame, text=f"Chaise {i+35}", bg="green", fg="white",
                       command=lambda num=i+35: button_clicked(num),width=8, height=3)
    button.grid(row=2, column=i, padx=5, pady=5)
    buttons.append(button)


cancel_button = tk.Button(root, text="pas maintenant !", bg="red", fg="white",width=15, height=3, command=root.destroy)
cancel_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

root.mainloop()
