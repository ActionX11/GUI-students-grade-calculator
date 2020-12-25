from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import sqlite3
con = sqlite3.connect('Students.db')
c = con.cursor()


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Login Window")
        self.root.geometry("1350x700+0+0")

        #background image
        self.bg=ImageTk.PhotoImage(file="Image/astronomy-1867616_1920.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        self.top=ImageTk.PhotoImage(file="Image/Pngtree—user login or authenticate icon_50899.jpg")
        top=Label(self.root,image=self.top,bd=0).place(x=630,y=80)

        frame1=Frame(self.root,bg='Light Grey')
        frame1.place(x=530,y=170,width=300,height=450)

        title=Label(frame1,text="LOGIN PAGE",font=("Monotype Corsiva",20,"bold"),bg="light grey",fg="Dark Blue").place(x=62,y=30)

        email=Label(frame1,text="E-mail address",font=("Times New Roman",15,"bold"),bg="Light Grey",fg="black").place(x=80,y=100)
        self.txt_email=Entry(frame1,font=("Times New Roman",15),bg="White")
        self.txt_email.place(x=25,y=130,width=250)

        passw=Label(frame1,text="Password",font=("Times New Roman",15,"bold"),bg="Light Grey",fg="black").place(x=100,y=200)
        self.txt_passw=Entry(frame1,font=("Times New Roman",15),bg="White")
        self.txt_passw.place(x=25,y=230,width=250)

        self.btn_img=ImageTk.PhotoImage(file="Image/Login.png")
        btn_register=Button(frame1,bg='Light Grey',image=self.btn_img,bd=0,cursor="hand2",command=self.logi).place(x=40,y=330)

        btn_regi=Button(frame1,command=self.Resisterwindow,text="Register New Account",bg='light Grey',fg='red',font=("times New Roman",14),bd=0,cursor="hand2").place(x=60,y=280,width=180)

    def Resisterwindow(self):
        self.root.destroy()
        import Registrationpage

    def logi(self):
        if self.txt_email.get()=="" or self.txt_passw.get()=="":
            messagebox.showerror("Error","Fill all the required fields",parent=self.root)
        else:
            c.execute("select * from student where Email=? and password=?",[self.txt_email.get(),self.txt_passw.get()])
            row=c.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid Username or Password",parent=self.root)
            else:
                c.execute("select ma1,ma2,ma3,ma4 from student where Email=? and password=?",[self.txt_email.get(),self.txt_passw.get()])
                a1=int(row[4])
                a2=int(row[5])
                a3=int(row[6])
                a4=int(row[7])
                a5=(a1+a2+a3+a4)/4
                if a5>90:
                    messagebox.showinfo("Welcome","Welcome you got the grade O congratulations")
                elif a5>80:
                    messagebox.showinfo("Welcome","Welcome you got the grade A congratulations")
                elif a5>70:
                    messagebox.showinfo("Welcome","Welcome you got the grade B ")
                elif a5>60:
                    messagebox.showinfo("Welcome","Welcome you got the grade C ")
                elif a5>50:
                    messagebox.showinfo("Welcome","Welcome you got the grade D ")
                elif a5>40:
                    messagebox.showinfo("Welcome","Welcome you got the grade E")
                else:
                    messagebox.showinfo("Welcome","Welcome Sorry to say but you did not passed try again next time")



root=Tk()
obj=Login(root)
root.mainloop()
con.commit()