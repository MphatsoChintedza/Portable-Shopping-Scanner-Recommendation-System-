from tkinter import*
import tkinter as tk

splash_root=tk.Tk()
splash_root.title("PORTABLE SCANNER 😊")
splash_root.geometry("500x500+-1500+250")

splash_label = Label(splash_root, text="PORTABLE SHOPPING SCANNER",font=("Impact", 40, "bold"), fg="gold", bg="#074463",width="300", height="2")
splash_label.pack(pady=20)

def main_window():
    splash_root.destroy()
    root=tk.Tk()
    root.title('Portable Scanner')
    root.iconbitmap('/Users/Mphatso Chintedza/PycharmProjects/pythonProject/Splash.py')
    root.geometry("500x550+-1500+250")

    main_label = Label(root, text="Directing to main screen")
    main_label.pack(pady=20)

splash_root.after(5000, main_window)

mainloop()