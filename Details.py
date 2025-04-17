from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
import mysql.connector
from mysql.connector import Error

class DetailsRoom:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1670x760+230+230")

        # ========== Variables ==========
        self.var_floor = StringVar()
        self.var_RoomNo = StringVar()
        self.var_RoomType = StringVar()

        # ========== Title ==========
        lbl_title = Label(self.root, text="ROOM DETAILS", font=("times new roman", 40, "bold"),
                         bg="black", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1695, height=70)

        # ========== Logo ==========
        img2 = Image.open(r"C:\\Users\\Shivangi\\Downloads\\ChatGPT Image Mar 30, 2025, 02_22_13 PM.png")  # Changed to relative path
        img2 = img2.resize((150, 70), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=0, y=0, width=150, height=70)
 
        # ========== Left Frame ==========
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add",
                                  font=("arial", 18, "bold"), padx=2)
        labelframeleft.place(x=3, y=70, width=840, height=500)

        # Floor
        lbl_floor = Label(labelframeleft, text="Floor:", font=("arial", 18, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)
        entry_floor = ttk.Entry(labelframeleft, textvariable=self.var_floor, 
                               font=("arial", 13, "bold"), width=20)
        entry_floor.grid(row=0, column=1, sticky=W)

        # Room No
        lbl_RoomNo = Label(labelframeleft, text="Room No:", font=("arial", 18, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W)
        entry_RoomNo = ttk.Entry(labelframeleft, textvariable=self.var_RoomNo,
                                font=("arial", 13, "bold"), width=20)
        entry_RoomNo.grid(row=1, column=1, sticky=W)
        
        # Room Type
        lbl_RoomType = Label(labelframeleft, text="Room Type:", font=("arial", 18, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky=W)
        self.combo_RoomType = ttk.Combobox(labelframeleft, textvariable=self.var_RoomType,
                                         font=("arial", 13, "bold"), width=18, state="readonly")
        self.combo_RoomType["values"] = ("Single", "Double", "Luxury","Deluxe", "Suite")
        self.combo_RoomType.current(0)
        self.combo_RoomType.grid(row=2, column=1, sticky=W)

        # Buttons Frame
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=300, width=535, height=55)
        
        btnAdd = Button(btn_frame, text="Add", command=self.add_data,
                      font=("arial", 15, "bold"), bg="black", fg="white", width=10)
        btnAdd.grid(row=0, column=0, padx=2)

        btnUpdate = Button(btn_frame, text="Update", command=self.update_data,
                          font=("arial", 15, "bold"), bg="black", fg="white", width=10)
        btnUpdate.grid(row=0, column=1, padx=2)

        btnDelete = Button(btn_frame, text="Delete", command=self.delete_data,
                          font=("arial", 15, "bold"), bg="black", fg="white", width=10)
        btnDelete.grid(row=0, column=2, padx=2)

        btnReset = Button(btn_frame, text="Reset", command=self.reset_data,
                         font=("arial", 15, "bold"), bg="black", fg="white", width=10)
        btnReset.grid(row=0, column=3, padx=2)

        # Table Frame
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details",
                               font=("arial", 18, "bold"), padx=2)
        Table_Frame.place(x=900, y=70, width=700, height=500)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(Table_Frame, columns=("floor", "roomno", "roomType"),
                                      xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("floor", text="Floor")
        self.room_table.heading("roomno", text="Room No")
        self.room_table.heading("roomType", text="Room Type")
        
        self.room_table["show"] = "headings"
        
        self.room_table.column("floor", width=100)
        self.room_table.column("roomno", width=100)
        self.room_table.column("roomType", width=100)
        
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # ========== Database Methods ==========
    def get_db_connection(self):
        try:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345678",
                database="management"
            )
            return conn
        except Error as e:
            messagebox.showerror("Database Error", f"Failed to connect to database: {str(e)}", parent=self.root)
            return None

    def validate_inputs(self):
        if not self.var_floor.get():
            messagebox.showerror("Error", "Floor is required", parent=self.root)
            return False
        if not self.var_RoomNo.get():
            messagebox.showerror("Error", "Room number is required", parent=self.root)
            return False
        if not self.var_RoomType.get():
            messagebox.showerror("Error", "Room type is required", parent=self.root)
            return False
        return True

    def add_data(self):
        if not self.validate_inputs():
            return
            
        try:
            conn = self.get_db_connection()
            if conn is None:
                return
                
            my_cursor = conn.cursor()
            
            # Check if room already exists
            my_cursor.execute("SELECT * FROM details WHERE roomno=%s", (self.var_RoomNo.get(),))
            existing = my_cursor.fetchone()
            
            if existing:
                messagebox.showerror("Error", "Room already exists", parent=self.root)
                return
                
            # Insert new room
            query = "INSERT INTO details (floor, roomno, roomType) VALUES (%s, %s, %s)"
            values = (
                self.var_floor.get(),
                self.var_RoomNo.get(),
                self.var_RoomType.get()
            )
            
            my_cursor.execute(query, values)
            conn.commit()
            self.fetch_data()
            messagebox.showinfo("Success", "Room added successfully", parent=self.root)
            self.reset_data()
            
        except Error as e:
            messagebox.showerror("Database Error", f"Failed to add room: {str(e)}", parent=self.root)
        finally:
            if conn and conn.is_connected():
                my_cursor.close()
                conn.close()

    def fetch_data(self):
        try:
            conn = self.get_db_connection()
            if conn is None:
                return
                
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM details")
            rows = my_cursor.fetchall()
            
            if len(rows) != 0:
                self.room_table.delete(*self.room_table.get_children())
                for row in rows:
                    self.room_table.insert("", END, values=row)
                    
        except Error as e:
            messagebox.showerror("Database Error", f"Failed to fetch data: {str(e)}", parent=self.root)
        finally:
            if conn and conn.is_connected():
                my_cursor.close()
                conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]
        
        if row:
            self.var_floor.set(row[0])
            self.var_RoomNo.set(row[1])
            self.var_RoomType.set(row[2])

    def update_data(self):
        if not self.var_RoomNo.get():
            messagebox.showerror("Error", "Please select a room to update", parent=self.root)
            return
            
        if not self.validate_inputs():
            return
            
        try:
            conn = self.get_db_connection()
            if conn is None:
                return
                
            my_cursor = conn.cursor()
            
            query = "UPDATE details SET floor=%s, roomType=%s WHERE roomno=%s"
            values = (
                self.var_floor.get(),
                self.var_RoomType.get(),
                self.var_RoomNo.get()
            )
            
            my_cursor.execute(query, values)
            conn.commit()
            self.fetch_data()
            messagebox.showinfo("Success", "Room details updated successfully", parent=self.root)
            
        except Error as e:
            messagebox.showerror("Database Error", f"Failed to update room: {str(e)}", parent=self.root)
        finally:
            if conn and conn.is_connected():
                my_cursor.close()
                conn.close()

    def delete_data(self):
        if not self.var_RoomNo.get():
            messagebox.showerror("Error", "Please select a room to delete", parent=self.root)
            return
            
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this room?", parent=self.root)
        if not confirm:
            return
            
        try:
            conn = self.get_db_connection()
            if conn is None:
                return
                
            my_cursor = conn.cursor()
            
            my_cursor.execute("DELETE FROM details WHERE roomno=%s", (self.var_RoomNo.get(),))
            conn.commit()
            self.fetch_data()
            self.reset_data()
            messagebox.showinfo("Success", "Room deleted successfully", parent=self.root)
            
        except Error as e:
            messagebox.showerror("Database Error", f"Failed to delete room: {str(e)}", parent=self.root)
        finally:
            if conn and conn.is_connected():
                my_cursor.close()
                conn.close()

    def reset_data(self):
        self.var_floor.set("")
        self.var_RoomNo.set("")
        self.var_RoomType.set("")


if __name__ == "__main__":
    root = Tk()
    obj = DetailsRoom(root)
    root.mainloop()
