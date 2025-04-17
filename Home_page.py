from tkinter import*
from PIL import Image, ImageTk
from customer import Cust_Win
from room import Roombooking
from details import DetailsRoom

class HotelMangementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Mangement System")
        self.root.geometry("1980x1800+0+0")

        # image of header
        img1=Image.open(r"C:\\Users\\Shivangi\\Downloads\\pexels-pixabay-258154.jpg")
        img1 = img1.resize((1850, 195), Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=100,y=0,width=1850,height=195)
         
        # logo
        img2=Image.open(r"C:\\Users\\Shivangi\\Downloads\\ChatGPT Image Mar 30, 2025, 02_22_13 PM.png")
        img2 = img2.resize((230, 195), Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=195)

        # title
        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("time new roman",40,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=200,width=1950,height=60)
        
        # main frame
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=250,width=2950,height=3000)

        # menu
        lbl_menu=Label(main_frame,text="MENU",font=("time new roman",20,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)

        # btn Frame
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=35,width=228,height=250)
        
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("time new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)
        
        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("time new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1) 
        
        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font=("time new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="REPORT",width=22,font=("time new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",width=22,font=("time new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)

        # right side image
        img3=Image.open(r"C:\\Users\\Shivangi\\Downloads\\pexels-kelly-1179532-2869215.jpg")
        img3 = img3.resize((1700 , 750), Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=230,y=0,width=1700,height=750)

        # down image
        img4=Image.open(r"C:\\Users\\Shivangi\\Downloads\\pexels-pixabay-258154 (1).jpg")
        img4 = img4.resize((230 , 230), Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=290,width=230,height=230)

        img5=Image.open(r"C:\\Users\\Shivangi\\Downloads\\tim-toomey-STqHLqMne3k-unsplash.jpg")
        img5 = img5.resize((230, 230), Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=520,width=230,height=230)
    
    # customer
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    # room
    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    # details
    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)




if __name__=="__main__":
    root=Tk()
    obj=HotelMangementSystem(root)
    root.mainloop()
