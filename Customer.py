from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Cust_Win:
    def __init__(self, root):  # Fixed constructor name
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1670x760+230+230")

        # ========== Variables ==========
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar()
        self.var_nationality = StringVar()
        self.var_address = StringVar()
        self.var_id_proof = StringVar()
        self.var_id_number = StringVar()

        # ========== Title ==========
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 40, "bold"),
                         bg="black", fg="white", bd=4, relief=RIDGE)
        lbl_title.place(x=0, y=0, width=1695, height=70)

        # ========== Logo ==========
        try:
            img2 = Image.open(r"C:\\Users\\Shivangi\\Downloads\\ChatGPT Image Mar 30, 2025, 02_22_13 PM.png")  # Update path to your image
            img2 = img2.resize((150, 70), Image.LANCZOS)
            self.photoimg2 = ImageTk.PhotoImage(img2)
            lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
            lblimg.place(x=0, y=0, width=150, height=70)
        except FileNotFoundError:
            messagebox.showwarning("Warning", "Hotel logo image not found")

        # ========== Left Frame ==========
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details",
                                   font=("arial", 18, "bold"), padx=2)
        labelframeleft.place(x=3, y=70, width=540, height=680)

        # ========== Labels and Entries ==========
        # Customer Ref
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref", font=("arial", 18, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)
        entry_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, font=("arial", 15, "bold"),
                             width=29, state="readonly")
        entry_ref.grid(row=0, column=1)

        # Customer Name
        cname = Label(labelframeleft, font=("arial", 18, "bold"), text="Customer Name:", padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        txtcname = ttk.Entry(labelframeleft, textvariable=self.var_cust_name, font=("arial", 15, "bold"), width=29)
        txtcname.grid(row=1, column=1)

        # Mother Name
        lblname = Label(labelframeleft, font=("arial", 18, "bold"), text="Mother Name:", padx=2, pady=6)
        lblname.grid(row=2, column=0, sticky=W)
        txtname = ttk.Entry(labelframeleft, textvariable=self.var_mother, font=("arial", 15, "bold"), width=29)
        txtname.grid(row=2, column=1)

        # Gender Combobox
        label_gender = Label(labelframeleft, font=("arial", 18, "bold"), text="Gender:", padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)
        combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_gender, font=("arial", 15, "bold"),
                                   width=27, state="readonly")
        combo_gender["values"] = ("Male", "Female", "Other")
        combo_gender.current(0)
        combo_gender.grid(row=3, column=1)

        # Postcode
        lblPostCode = Label(labelframeleft, font=("arial", 18, "bold"), text="PostCode:", padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)
        txtPostCode = ttk.Entry(labelframeleft, textvariable=self.var_post, font=("arial", 15, "bold"), width=29)
        txtPostCode.grid(row=4, column=1)

        # Mobile Number
        lblMobile = Label(labelframeleft, font=("arial", 18, "bold"), text="Mobile:", padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)
        txtMobile = ttk.Entry(labelframeleft, textvariable=self.var_mobile, font=("arial", 15, "bold"), width=29)
        txtMobile.grid(row=5, column=1)

        # Email
        lblEmail = Label(labelframeleft, font=("arial", 18, "bold"), text="Email:", padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)
        txtEmail = ttk.Entry(labelframeleft, textvariable=self.var_email, font=("arial", 15, "bold"), width=29)
        txtEmail.grid(row=6, column=1)

        # Nationality
        lblNationality = Label(labelframeleft, font=("arial", 18, "bold"), text="Nationality:", padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)
        combo_Nationality = ttk.Combobox(labelframeleft, textvariable=self.var_nationality,
                                       font=("arial", 15, "bold"), width=27, state="readonly")
        combo_Nationality["values"] = ("Indian", "Foreigner")
        combo_Nationality.current(0)
        combo_Nationality.grid(row=7, column=1)

        # ID Proof Type
        lblIdProof = Label(labelframeleft, font=("arial", 18, "bold"), text="Id Proof Type:", padx=2, pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)
        combo_IdProof = ttk.Combobox(labelframeleft, textvariable=self.var_id_proof, font=("arial", 15, "bold"),
                                    width=27, state="readonly")
        combo_IdProof["values"] = ("AdharCard", "DrivingLicence", "Passport", "Other Valid Proof")
        combo_IdProof.current(0)
        combo_IdProof.grid(row=8, column=1)

        # ID Number
        lblIdNumber = Label(labelframeleft, font=("arial", 18, "bold"), text="Id Number:", padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        txtIdNumber = ttk.Entry(labelframeleft, textvariable=self.var_id_number, font=("arial", 15, "bold"), width=29)
        txtIdNumber.grid(row=9, column=1)

        # Address
        lblAddress = Label(labelframeleft, font=("arial", 18, "bold"), text="Address:", padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)
        txtAddress = ttk.Entry(labelframeleft, textvariable=self.var_address, font=("arial", 15, "bold"), width=29)
        txtAddress.grid(row=10, column=1)

        # ========== Buttons ==========
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=580, width=535, height=60)
        
        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 16, "bold"),
                       bg="black", fg="white", width=9)
        btnAdd.grid(row=0, column=0, padx=6, pady=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update_data, font=("arial", 16, "bold"),
                          bg="black", fg="white", width=9)
        btnUpdate.grid(row=0, column=1, padx=2)

        btnDelete = Button(btn_frame, text="Delete", command=self.delete_data, font=("arial", 16, "bold"),
                          bg="black", fg="white", width=9)
        btnDelete.grid(row=0, column=2, padx=2)

        btnReset = Button(btn_frame, text="Reset", command=self.reset_data, font=("arial", 16, "bold"),
                         bg="black", fg="white", width=9)
        btnReset.grid(row=0, column=3, padx=2)

        # ========== Right Frame ==========
        Tabel_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details And Search System",
                                font=("arial", 18, "bold"), padx=2)
        Tabel_Frame.place(x=550, y=75, width=1110, height=680)

        # Search System
        lblSearchBy = Label(Tabel_Frame, font=("arial", 18, "bold"), text="Search By:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=3)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Tabel_Frame, textvariable=self.search_var, 
                                   font=("arial", 18, "bold"), width=23, state="readonly")
        combo_Search["values"] = ("Mobile", "Ref")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=3)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Tabel_Frame, textvariable=self.txt_search, font=("arial", 18, "bold"), width=23)
        txtSearch.grid(row=0, column=2, padx=3)

        btnSearch = Button(Tabel_Frame, text="Search", command=self.search_data,
                          font=("arial", 18, "bold"), bg="black", fg="white", width=9)
        btnSearch.grid(row=0, column=3, padx=2)

        btnShowAll = Button(Tabel_Frame, text="Show All", command=self.fetch_data,
                           font=("arial", 18, "bold"), bg="black", fg="white", width=9)
        btnShowAll.grid(row=0, column=4, padx=2)

        # ========== Data Table ==========
        details_table = Frame(Tabel_Frame, bd=10, relief=RIDGE)
        details_table.place(x=0, y=50, width=1100, height=600)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, columns=(
            "ref", "name", "mother", "gender", "post", "mobile", "email",
            "nationality", "idproof", "idnumber", "address"),
                                             xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref", text="Refer No")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("mother", text="Mother")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("post", text="PostCode")
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("idproof", text="Id Proof")
        self.Cust_Details_Table.heading("idnumber", text="Id Number")
        self.Cust_Details_Table.heading("address", text="Address")

        self.Cust_Details_Table["show"] = "headings"
        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # ========== Database Methods ==========
    def add_data(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="12345678",
                    database="management"
                )
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO customer VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nationality.get(),
                    self.var_id_proof.get(),
                    self.var_id_number.get(),
                    self.var_address.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="management"
        )
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]
        
        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_mother.set(row[2]),
        self.var_gender.set(row[3]),
        self.var_post.set(row[4]),
        self.var_mobile.set(row[5]),
        self.var_email.set(row[6]),
        self.var_nationality.set(row[7]),
        self.var_id_proof.set(row[8]),
        self.var_id_number.set(row[9]),
        self.var_address.set(row[10])

    def update_data(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Mobile number is required", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345678",
                database="management"
            )
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE customer SET Name=%s, Mother=%s, Gender=%s, PostCode=%s, Mobile=%s, Email=%s, Nationality=%s, IdProof=%s, IdNumber=%s, Address=%s WHERE Ref=%s", (
                self.var_cust_name.get(),
                self.var_mother.get(),
                self.var_gender.get(),
                self.var_post.get(),
                self.var_mobile.get(),
                self.var_email.get(),
                self.var_nationality.get(),
                self.var_id_proof.get(),
                self.var_id_number.get(),
                self.var_address.get(),
                self.var_ref.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Customer details updated successfully", parent=self.root)

    def delete_data(self):
        delete = messagebox.askyesno("Delete", "Are you sure you want to delete this customer?", parent=self.root)
        if delete:
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="12345678",
                database="management"
            )
            my_cursor = conn.cursor()
            query = "DELETE FROM customer WHERE Ref=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            conn.close()
            self.fetch_data()
            self.reset_data()
            messagebox.showinfo("Delete", "Customer deleted successfully", parent=self.root)

    def reset_data(self):
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))
        self.var_cust_name.set(""),
        self.var_mother.set(""),
        self.var_gender.set("Male"),
        self.var_post.set(""),
        self.var_mobile.set(""),
        self.var_email.set(""),
        self.var_nationality.set("Indian"),
        self.var_id_proof.set("AdharCard"),
        self.var_id_number.set(""),
        self.var_address.set("")

    def search_data(self):
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="management"
        )
        my_cursor = conn.cursor()
        
        if self.search_var.get() == "Mobile":
            my_cursor.execute("SELECT * FROM customer WHERE Mobile LIKE %s", ("%"+self.txt_search.get()+"%",))
        else:
            my_cursor.execute("SELECT * FROM customer WHERE Ref LIKE %s", ("%"+self.txt_search.get()+"%",))
            
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
        conn.close()

if __name__ == "__main__":  # Fixed main guard
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
