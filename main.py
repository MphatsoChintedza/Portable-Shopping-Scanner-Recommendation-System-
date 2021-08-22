from tkinter import*
from PIL import ImageTk #pip install pillow
from tkinter import messagebox

class Login(Frame):
    def __init__(self,root):
        self.root=root
        self.root.wm_title("Login System")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)

        #====BG IMage=====
        #self.bg=ImageTk.PhotoImage(file="images/login.jpg")
        #self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        # Login Frame
        Frame_login = Frame(self.root, bg="#074463", highlightbackground="#074463", highlightthickness=5)
        Frame_login.place(x=150, y=150, height=340, width=500)

        title = Label(Frame_login, text="Login Here", font=("Impact", 35, "bold"), fg="gold", bg="#074463").place(x=72,y=20)
        desc = Label(Frame_login, text="Portable Scanner ", font=("times new roman", 15, "bold"), fg="gold",bg="#074463").place(x=72, y=80)

        lbl_user = Label(Frame_login, text="Username", font=("goudy old style", 15, "bold"), fg="black",bg="#074463").place(x=72, y=110)
        self.txt_user = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_user.place(x=72, y=140, width=350, height=35)

        lbl_passcode = Label(Frame_login, text="Password", font=("Goudy old style", 15, "bold"), fg="black",bg="#074463").place(x=72, y=180)
        self.txt_password = Entry(Frame_login, font=("times new roman", 15), bg="lightgray")
        self.txt_password.place(x=72, y=208, width=350, height=35)

        Register_button = Button(Frame_login, text="Don't have and account? Register here", bg="#074463", fg="black", bd=0,font=("times new roman", 12)).place(x=72, y=248)
        Login_button = Button(self.root,command=self.login_function,text="Login", fg="black", bg="#074463", bd=7,font=("times new roman", 20, "bold")).place(x=310, y=460, width=180)
        Exit_btn = Button(self.root,text="Exit Scanner App", bg="#074463", fg="black", bd=7, pady=15,width=20, font="arial 15 bold").grid(row=0, column=4, padx=2, pady=5)

    def login_function(self):
        if self.text_pass.get()== "" or self.text_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.text_pass.get()!="Mphatso" or self.text_user()!="123456":
            messagebox.showerror("Error","Invalid Username/Password",parent=self.root)
        else:
            messagebox.showinfo("Welcome",f"Welcome {self.text_user.get()}\nYour Password: {self.text_pass.get()}",parent=self.root)

root = Tk()
app = Login(root)
root.mainloop()