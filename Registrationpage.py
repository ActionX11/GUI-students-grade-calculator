from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import sqlite3
con= sqlite3.connect ('Students.db')
c = con.cursor()
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")

#background image
        self.bg=ImageTk.PhotoImage(file="Image/13862.jpg")
        bg=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
#foreground left image
        self.li=ImageTk.PhotoImage(file="Image/lefti.jpg")
        li=Label(self.root,image=self.li).place(x=80,y=100,width=400,height=550)

#Registration Frame
        frame1=Frame(self.root,bg='White')
        frame1.place(x=480,y=100,width=700,height=550)

        title=Label(frame1,text="REGISTER HERE",font=("Times New Roman",20,"bold"),bg="white",fg="Dark Blue").place(x=50,y=30)


        # self.var_fname=StringVar()
        fname=Label(frame1,text="First name",font=("Times New Roman",15,"bold"),bg="white",fg="black").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("Times New Roman",15),bg="light grey")
        self.txt_fname.place(x=50,y=130,width=250)

        lname=Label(frame1,text="Last name",font=("Times New Roman",15,"bold"),bg="white",fg="black").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("Times New Roman",15),bg="light grey")
        self.txt_lname.place(x=370,y=130,width=250)

        email=Label(frame1,text="E-mail address",font=("Times New Roman",15,"bold"),bg="white",fg="black").place(x=200,y=170)
        self.txt_email=Entry(frame1,font=("Times New Roman",15),bg="light grey")
        self.txt_email.place(x=200,y=200,width=250)

        passw=Label(frame1,text="Password",font=("Times New Roman",15,"bold"),bg="white",fg="black").place(x=200,y=240)
        self.txt_passw=Entry(frame1,font=("Times New Roman",15),bg="light grey")
        self.txt_passw.place(x=200,y=270,width=250)

        m1=Label(frame1,text="Subject 1 Marks",font=("Times New Roman",15,"bold"),bg="white",fg="black").place(x=50,y=310)
        self.txt_m1=Entry(frame1,font=("Times New Roman",15),bg="light grey")
        self.txt_m1.place(x=50,y=340,width=250)

        m2=Label(frame1,text="Subject 2 Marks",font=("Times New Roman",15,"bold"),bg="white",fg="black").place(x=370,y=310)
        self.txt_m2=Entry(frame1,font=("Times New Roman",15),bg="light grey")
        self.txt_m2.place(x=370,y=340,width=250)

        m3=Label(frame1,text="Subject 3 Marks",font=("Times New Roman",15,"bold"),bg="white",fg="black").place(x=50,y=380)
        self.txt_m3=Entry(frame1,font=("Times New Roman",15),bg="light grey")
        self.txt_m3.place(x=50,y=410,width=250)

        m4=Label(frame1,text="Subject 4 Marks",font=("Times New Roman",15,"bold"),bg="white",fg="black").place(x=370,y=380)
        self.txt_m4=Entry(frame1,font=("Times New Roman",15),bg="light grey")
        self.txt_m4.place(x=370,y=410,width=250)

        self.btn_img=ImageTk.PhotoImage(file="Image/clipart150801.png")
        btn_register=Button(frame1,bg='white',image=self.btn_img,bd=0,cursor="hand2",command=self.regi).place(x=200,y=470)

       # btn_login=Button(self.root,text="Log In",bg='white',font=("times New Roman",20),bd=0,cursor="hand2").place(x=200,y=380,width=180)

        self.btn_login=ImageTk.PhotoImage(file="Image/i.png")
        btn_login=Button(self.root,command=self.Loginwindow,bg="black",image=self.btn_login,bd=0,cursor="hand2").place(x=164,y=340,height=60)

    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_email.delete(0,END)
        self.txt_passw.delete(0,END)
        self.txt_m1.delete(0,END)
        self.txt_m2.delete(0,END)
        self.txt_m3.delete(0,END)
        self.txt_m4.delete(0,END)

    def Loginwindow(self):
        self.root.destroy()
        import Loginpage

    def regi(self):
        if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.txt_passw.get()=="" or self.txt_m1.get()=="" or self.txt_m2.get()=="" or self.txt_m3.get()=="" or self.txt_m4.get()=="":
            messagebox.showerror("Error","All Necessary Fields Are Required To Be Filled",parent=self.root)
        else:
            c.execute("select * from student where Email=?",[self.txt_email.get()])
            row=c.fetchone()
            if row!=None:
                messagebox.showerror("Error","This Email already exists",parent=self.root)
            else:
                c.execute("insert into student(Fname,Lname,Email,password,ma1,ma2,ma3,ma4)values(?,?,?,?,?,?,?,?)",(self.txt_fname.get(),self.txt_lname.get(),self.txt_email.get(),self.txt_passw.get(),self.txt_m1.get(),self.txt_m2.get(),self.txt_m3.get(),self.txt_m4.get()))
                print("data added")
                messagebox.showinfo("Registered","Registration Successfull",parent=self.root)
                self.clear()

root=Tk()
obj=Register(root)
root.mainloop()
con.commit()