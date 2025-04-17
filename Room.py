from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk, messagebox
from datetime import datetime
import mysql.connector
from mysql.connector import Error

class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1670x760+230+230")

        # ========== Variables ==========
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noOfdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        # ========== Title ==========
        lbl_title = Label(self.root, text="ROOMBOOKING DETAILS", font=("times new roman", 40, "bold"),
                         bg="black", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1695, height=70)

        # ========== Logo ==========
        try:
            img2 = Image.open(r"C:\\Users\\Shivangi\\Downloads\\ChatGPT Image Mar 30, 2025, 02_22_13 PM.png")
            img2 = img2.resize((150, 70), Image.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)
            lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
            lblimg.place(x=0, y=0, width=150, height=70)
        except Exception as e:
            messagebox.showwarning("Warning", f"Logo image not found: {str(e)}")

        # ========== Left Frame ==========
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details",
                                  font=("arial", 18, "bold"), padx=2)
        labelframeleft.place(x=3, y=70, width=540, height=680)

        # Customer Contact
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact:", font=("arial", 18, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)
        entry_contact = ttk.Entry(labelframeleft, textvariable=self.var_contact, font=("arial", 13, "bold"), width=20)
        entry_contact.grid(row=0, column=1, sticky=W)

        # Fetch Data Button
        btnFetchData = Button(labelframeleft, command=self.Fetch_contact, text="Fetch Data", 
                            font=("arial", 16, "bold"), bg="black", fg="white", width=9)
        btnFetchData.place(x=400, y=4)

        # Check-in Date
        check_in_date = Label(labelframeleft, font=("arial", 18, "bold"), text="Check-In Date:", padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)
        entry_in_date = ttk.Entry(labelframeleft, textvariable=self.var_checkin, font=("arial", 15, "bold"), width=27)
        entry_in_date.grid(row=1, column=1)

        # Check-out Date
        lbl_check_out = Label(labelframeleft, font=("arial", 18, "bold"), text="Check-Out Date:", padx=2, pady=6)
        lbl_check_out.grid(row=2, column=0, sticky=W)
        entry_out_date = ttk.Entry(labelframeleft, textvariable=self.var_checkout, font=("arial", 15, "bold"), width=27)
        entry_out_date.grid(row=2, column=1)

        # Room Type
        label_RoomType = Label(labelframeleft, font=("arial", 18, "bold"), text="Room Type:", padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)
        combo_RoomType = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype,
                                     font=("arial", 18, "bold"), width=18, state="readonly")
        combo_RoomType["values"] = ("Single", "Double", "Luxury", "Deluxe", "Suite")
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        # Available Room
        lblRoomAvailable = Label(labelframeleft, font=("arial", 18, "bold"), text="Available Room:", padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)
        # Changed to Entry since room numbers might vary
        entry_RoomNo = ttk.Entry(labelframeleft, textvariable=self.var_roomavailable, 
                                font=("arial", 15, "bold"), width=27)
        entry_RoomNo.grid(row=4, column=1)

        # Meal
        lblMeal = Label(labelframeleft, font=("arial", 18, "bold"), text="Meal:", padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)
        combo_Meal = ttk.Combobox(labelframeleft, textvariable=self.var_meal, 
                                 font=("arial", 15, "bold"), width=25, state="readonly")
        combo_Meal["values"] = ("Breakfast", "Lunch", "Dinner", "Full Board")
        combo_Meal.current(0)
        combo_Meal.grid(row=5, column=1)

        # No. of Days
        lblNoOfDays = Label(labelframeleft, font=("arial", 18, "bold"), text="No of Days:", padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)
        txtNoOfDays = ttk.Entry(labelframeleft, textvariable=self.var_noOfdays, 
                               font=("arial", 15, "bold"), width=27, state="readonly")
        txtNoOfDays.grid(row=6, column=1)

        # Paid Tax
        lblPaidTax = Label(labelframeleft, font=("arial", 18, "bold"), text="Paid Tax:", padx=2, pady=6)
        lblPaidTax.grid(row=7, column=0, sticky=W)
        txtPaidTax = ttk.Entry(labelframeleft, textvariable=self.var_paidtax, 
                             font=("arial", 15, "bold"), width=27, state="readonly")
        txtPaidTax.grid(row=7, column=1)

        # Sub Total
        lblSubTotal = Label(labelframeleft, font=("arial", 18, "bold"), text="Sub Total:", padx=2, pady=6)
        lblSubTotal.grid(row=8, column=0, sticky=W)
        txtSubTotal = ttk.Entry(labelframeleft, textvariable=self.var_actualtotal, 
                              font=("arial", 15, "bold"), width=27, state="readonly")
        txtSubTotal.grid(row=8, column=1)

        # Total Cost
        lblTotalCost = Label(labelframeleft, font=("arial", 18, "bold"), text="Total Cost:", padx=2, pady=6)
        lblTotalCost.grid(row=9, column=0, sticky=W)
        txtTotalCost = ttk.Entry(labelframeleft, textvariable=self.var_total, 
                               font=("arial", 15, "bold"), width=27, state="readonly")
        txtTotalCost.grid(row=9, column=1)

        # Bill Button
        btnBill = Button(labelframeleft, text="Bill", command=self.total, 
                        font=("arial", 15, "bold"), bg="black", fg="white", width=10)
        btnBill.grid(row=11, column=0, padx=2, sticky=W)

        # Buttons Frame
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=580, width=535, height=60)
        
        btnAdd = Button(btn_frame, text="Add", command=self.add_data, 
                       font=("arial", 14, "bold"), bg="black", fg="white", width=10)
        btnAdd.grid(row=0, column=0, padx=2)

        btnUpdate = Button(btn_frame, text="Update", command=self.update_data, 
                         font=("arial", 14, "bold"), bg="black", fg="white", width=10)
        btnUpdate.grid(row=0, column=1, padx=2)

        btnDelete = Button(btn_frame, text="Delete", command=self.delete_data, 
                         font=("arial", 14, "bold"), bg="black", fg="white", width=10)
        btnDelete.grid(row=0, column=2, padx=2)

        btnReset = Button(btn_frame, text="Reset", command=self.reset_data, 
                        font=("arial", 14, "bold"), bg="black", fg="white", width=10)
        btnReset.grid(row=0, column=3, padx=2)

        # Right-side Image
        try:
            img3 = Image.open(r"C:\\Users\\Shivangi\\OneDrive\\Pictures\\Screenshots\\Screenshot 2025-03-25 230022.png")  
            img3 = img3.resize((800, 300), Image.LANCZOS)
            self.photoimg3 = ImageTk.PhotoImage(img3)
            lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
            lblimg.place(x=950, y=75, width=700, height=260)
        except Exception as e:
            messagebox.showwarning("Warning", f"Room image not found: {str(e)}")

        # Table Frame Search System
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System",
                                font=("arial", 15, "bold"), padx=2)
        Table_Frame.place(x=550, y=350, width=1100, height=400)
        
        lblSearchBy = Label(Table_Frame, font=("arial", 15, "bold"), text="Search By:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=3)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame, textvariable=self.search_var, 
                                  font=("arial", 15, "bold"), width=28, state="readonly")
        combo_Search["values"] = ("Contact", "Room")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=3)
        
        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, 
                            font=("arial", 15, "bold"), width=28)
        txtSearch.grid(row=0, column=2, padx=3)

        btnSearch = Button(Table_Frame, text="Search", command=self.search_data, 
                         font=("arial", 15, "bold"), bg="black", fg="white", width=10)
        btnSearch.grid(row=0, column=3, padx=2)

        btnShowAll = Button(Table_Frame, text="Show All", command=self.fetch_data, 
                          font=("arial", 15, "bold"), bg="black", fg="white", width=10)
        btnShowAll.grid(row=0, column=4, padx=2)

        # Details Table
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=1100, height=300)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.room_table = ttk.Treeview(details_table, columns=(
            "contact", "checkin", "checkout", "roomtype", "roomavailable", "meal", "noOfdays",
            "paidtax", "actualtotal", "total"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Check-In")
        self.room_table.heading("checkout", text="Check-Out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room No")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noOfdays", text="No Of Days")
        self.room_table.heading("paidtax", text="Paid Tax")
        self.room_table.heading("actualtotal", text="Sub Total")
        self.room_table.heading("total", text="Total")
        
        self.room_table["show"] = "headings"
        
        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noOfdays", width=100)
        self.room_table.column("paidtax", width=100)
        self.room_table.column("actualtotal", width=100)
        self.room_table.column("total", width=100)
        
        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

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
            messagebox.showerror("Database Error", f"Failed to connect to database: {str(e)}")
            return None

    def add_data(self):
        if not self.validate_inputs():
            return
            
        try:
            conn = self.get_db_connection()
            if conn is None:
                return
                
            my_cursor = conn.cursor()
            
            # Check if contact already exists
            my_cursor.execute("SELECT * FROM room WHERE contact=%s", (self.var_contact.get(),))
            existing = my_cursor.fetchone()
            
            if existing:
                messagebox.showerror("Error", "Customer already has a room booking", parent=self.root)
                return
                
            # Insert new record
            query = """INSERT INTO room (contact, checkin, checkout, roomtype, roomavailable, meal, noOfdays, paidtax, actualtotal, total) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
            values = (
                self.var_contact.get(),
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noOfdays.get(),
                self.var_paidtax.get(),
                self.var_actualtotal.get(),
                self.var_total.get()
            )
            
            my_cursor.execute(query, values)
            conn.commit()
            self.fetch_data()
            messagebox.showinfo("Success", "Room booking added successfully", parent=self.root)
            
        except Error as e:
            messagebox.showerror("Database Error", f"Failed to add room booking: {str(e)}", parent=self.root)
        finally:
            if conn and conn.is_connected():
                my_cursor.close()
                conn.close()

    def validate_inputs(self):
        if not self.var_contact.get():
            messagebox.showerror("Error", "Customer contact is required", parent=self.root)
            return False
            
        if not self.var_checkin.get():
            messagebox.showerror("Error", "Check-in date is required", parent=self.root)
            return False
            
        if not self.var_checkout.get():
            messagebox.showerror("Error", "Check-out date is required", parent=self.root)
            return False
            
        try:
            in_date = datetime.strptime(self.var_checkin.get(), "%d/%m/%Y")
            out_date = datetime.strptime(self.var_checkout.get(), "%d/%m/%Y")
            if out_date <= in_date:
                messagebox.showerror("Error", "Check-out date must be after check-in date", parent=self.root)
                return False
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Use DD/MM/YYYY", parent=self.root)
            return False
            
        if not self.var_roomavailable.get():
            messagebox.showerror("Error", "Room number is required", parent=self.root)
            return False
            
        return True

    def fetch_data(self):
        conn = None
        try:
            conn = self.get_db_connection()
            if conn is None:
                return
                
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM room")
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
            self.var_contact.set(row[0])
            self.var_checkin.set(row[1])
            self.var_checkout.set(row[2])
            self.var_roomtype.set(row[3])
            self.var_roomavailable.set(row[4])
            self.var_meal.set(row[5])
            self.var_noOfdays.set(row[6])
            self.var_paidtax.set(row[7] if len(row) > 7 else "")
            self.var_actualtotal.set(row[8] if len(row) > 8 else "")
            self.var_total.set(row[9] if len(row) > 9 else "")

    def update_data(self):
        if not self.var_contact.get():
            messagebox.showerror("Error", "Please select a booking to update", parent=self.root)
            return
            
        if not self.validate_inputs():
            return
            
        try:
            conn = self.get_db_connection()
            if conn is None:
                return
                
            my_cursor = conn.cursor()
            
            query = """UPDATE room SET 
                      checkin=%s, checkout=%s, roomtype=%s, 
                      roomavailable=%s, meal=%s, noOfdays=%s,
                      paidtax=%s, actualtotal=%s, total=%s
                      WHERE contact=%s"""
            values = (
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_roomavailable.get(),
                self.var_meal.get(),
                self.var_noOfdays.get(),
                self.var_paidtax.get(),
                self.var_actualtotal.get(),
                self.var_total.get(),
                self.var_contact.get()
            )
            
            my_cursor.execute(query, values)
            conn.commit()
            self.fetch_data()
            messagebox.showinfo("Success", "Room booking updated successfully", parent=self.root)
            
        except Error as e:
            messagebox.showerror("Database Error", f"Failed to update booking: {str(e)}", parent=self.root)
        finally:
            if conn and conn.is_connected():
                my_cursor.close()
                conn.close()

    def delete_data(self):
        if not self.var_contact.get():
            messagebox.showerror("Error", "Please select a booking to delete", parent=self.root)
            return
            
        confirm = messagebox.askyesno("Confirm", "Are you sure you want to delete this booking?", parent=self.root)
        if not confirm:
            return
            
        conn = None
        try:
            conn = self.get_db_connection()
            if conn is None:
                return
                
            my_cursor = conn.cursor()
            
            my_cursor.execute("DELETE FROM room WHERE contact=%s", (self.var_contact.get(),))
            conn.commit()
            self.fetch_data()
            self.reset_data()
            messagebox.showinfo("Success", "Booking deleted successfully", parent=self.root)
            
        except Error as e:
            messagebox.showerror("Database Error", f"Failed to delete booking: {str(e)}", parent=self.root)
        finally:
            if conn and conn.is_connected():
                my_cursor.close()
                conn.close()

    def reset_data(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("Single")
        self.var_roomavailable.set("")
        self.var_meal.set("Breakfast")
        self.var_noOfdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

    def Fetch_contact(self):
        if not self.var_contact.get():
            messagebox.showerror("Error", "Please enter Contact Number", parent=self.root)
            return
            
        conn = None
        try:
            conn = self.get_db_connection()
            if conn is None:
                return
                
            my_cursor = conn.cursor()
            
            # Fetch customer details
            query = """SELECT name, gender, email, nationality, address 
                       FROM customer WHERE mobile=%s"""
            my_cursor.execute(query, (self.var_contact.get(),))
            row = my_cursor.fetchone()
            
            if row is None:
                messagebox.showerror("Error", "Customer not found", parent=self.root)
                return
                
            # Display customer details in a new window
            customer_window = Toplevel(self.root)
            customer_window.title("Customer Details")
            customer_window.geometry("400x300+500+200")
            
            lblName = Label(customer_window, text="Name:", font=("arial", 14, "bold"))
            lblName.grid(row=0, column=0, sticky=W, padx=5, pady=5)
            lblNameValue = Label(customer_window, text=row[0], font=("arial", 14))
            lblNameValue.grid(row=0, column=1, sticky=W, padx=5, pady=5)
            
            lblGender = Label(customer_window, text="Gender:", font=("arial", 14, "bold"))
            lblGender.grid(row=1, column=0, sticky=W, padx=5, pady=5)
            lblGenderValue = Label(customer_window, text=row[1], font=("arial", 14))
            lblGenderValue.grid(row=1, column=1, sticky=W, padx=5, pady=5)
            
            lblEmail = Label(customer_window, text="Email:", font=("arial", 14, "bold"))
            lblEmail.grid(row=2, column=0, sticky=W, padx=5, pady=5)
            lblEmailValue = Label(customer_window, text=row[2], font=("arial", 14))
            lblEmailValue.grid(row=2, column=1, sticky=W, padx=5, pady=5)
            
            lblNationality = Label(customer_window, text="Nationality:", font=("arial", 14, "bold"))
            lblNationality.grid(row=3, column=0, sticky=W, padx=5, pady=5)
            lblNationalityValue = Label(customer_window, text=row[3], font=("arial", 14))
            lblNationalityValue.grid(row=3, column=1, sticky=W, padx=5, pady=5)
            
            lblAddress = Label(customer_window, text="Address:", font=("arial", 14, "bold"))
            lblAddress.grid(row=4, column=0, sticky=W, padx=5, pady=5)
            lblAddressValue = Label(customer_window, text=row[4], font=("arial", 14))
            lblAddressValue.grid(row=4, column=1, sticky=W, padx=5, pady=5)
            
        except Error as e:
            messagebox.showerror("Database Error", f"Failed to fetch customer details: {str(e)}", parent=self.root)
        finally:
            if conn and conn.is_connected():
                my_cursor.close()
                conn.close()

    def search_data(self):
        if not self.txt_search.get():
            messagebox.showerror("Error", "Please enter search criteria", parent=self.root)
            return
            
        conn = None
        try:
            conn = self.get_db_connection()
            if conn is None:
                return
                
            my_cursor = conn.cursor()
            
            if self.search_var.get() == "Contact":
                query = "SELECT * FROM room WHERE contact LIKE %s"
                value = ("%" + self.txt_search.get() + "%",)
            else:
                query = "SELECT * FROM room WHERE roomavailable LIKE %s"
                value = ("%" + self.txt_search.get() + "%",)
                
            my_cursor.execute(query, value)
            rows = my_cursor.fetchall()
            
            if len(rows) != 0:
                self.room_table.delete(*self.room_table.get_children())
                for row in rows:
                    self.room_table.insert("", END, values=row)
            else:
                messagebox.showinfo("Info", "No matching records found", parent=self.root)
                
        except Error as e:
            messagebox.showerror("Database Error", f"Failed to search data: {str(e)}", parent=self.root)
        finally:
            if conn and conn.is_connected():
                my_cursor.close()
                conn.close()

    def total(self):
        try:
            # Validate dates
            if not self.var_checkin.get() or not self.var_checkout.get():
                messagebox.showerror("Error", "Please enter both check-in and check-out dates", parent=self.root)
                return
                
            in_date = datetime.strptime(self.var_checkin.get(), "%d/%m/%Y")
            out_date = datetime.strptime(self.var_checkout.get(), "%d/%m/%Y")
            
            # Calculate number of days
            no_of_days = abs((out_date - in_date).days)
            if no_of_days == 0:
                no_of_days = 1  # Minimum 1 day stay
            self.var_noOfdays.set(str(no_of_days))
            
            # Define room rates
            room_rates = {
                "Single": 1000,
                "Double": 2000,
                "Luxury": 5000,
                "Deluxe": 10000,
                "Suite": 15000
            }
            
            # Define meal rates
            meal_rates = {
                "Breakfast": 200,
                "Lunch": 300,
                "Dinner": 400,
                "Full Board": 800
            }
            
            # Get selected room and meal types
            room_type = self.var_roomtype.get()
            meal_type = self.var_meal.get()
            
            # Calculate costs
            room_cost = room_rates.get(room_type, 0) * no_of_days
            meal_cost = meal_rates.get(meal_type, 0) * no_of_days
            subtotal = room_cost + meal_cost
            tax = subtotal * 0.09  # 9% tax
            total = subtotal + tax
            
            # Update display
            self.var_paidtax.set(f"Rs.{tax:.2f}")
            self.var_actualtotal.set(f"Rs.{subtotal:.2f}")
            self.var_total.set(f"Rs.{total:.2f}")
            
        except ValueError:
            messagebox.showerror("Error", "Invalid date format. Use DD/MM/YYYY", parent=self.root)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to calculate total: {str(e)}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
