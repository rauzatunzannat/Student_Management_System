from tkinter import *
from tkinter import messagebox, ttk, filedialog
import time
import pymysql
from ttkthemes import ThemedTk
from PIL import Image, ImageTk
import csv

# Globals
con = None
mycursor = None


offline_students = [
    (1, "Kamrul Hasan", "01712345678", "kamrul@example.com", "Dhaka", "Male", "01-01-2000", "01-09-2025", "10:00:00"),
    (2, "Jui Sumaiya", "01812345678", "jui@example.com", "Dhaka", "Female", "05-05-2001", "02-09-2025", "11:00:00"),
    (3, "Arafat Hossain", "01911111111", "arafat@example.com", "Chittagong", "Male", "12-03-2000", "03-09-2025", "09:45:00"),
    (4, "Mitu Akter", "01722222222", "mitu@example.com", "Rajshahi", "Female", "23-07-2001", "04-09-2025", "10:30:00"),
    (5, "Sajid Khan", "01533333333", "sajid@example.com", "Sylhet", "Male", "14-02-2002", "05-09-2025", "12:00:00"),
    (6, "Ruma Sultana", "01844444444", "ruma@example.com", "Khulna", "Female", "19-09-2000", "06-09-2025", "11:30:00"),
    (7, "Rakibul Islam", "01755555555", "rakib@example.com", "Barisal", "Male", "08-11-1999", "07-09-2025", "09:15:00"),
    (8, "Nusrat Jahan", "01666666666", "nusrat@example.com", "Dhaka", "Female", "01-06-2001", "08-09-2025", "10:20:00"),
    (9, "Farhan Ahmed", "01977777777", "farhan@example.com", "Rangpur", "Male", "29-08-2000", "09-09-2025", "11:10:00"),
    (10, "Mim Chowdhury", "01788888888", "mim@example.com", "Comilla", "Female", "15-01-2002", "10-09-2025", "12:30:00"),
    (11, "Tanvir Rahman", "01899999999", "tanvir@example.com", "Bogura", "Male", "05-05-2000", "11-09-2025", "09:50:00"),
    (12, "Rokeya Begum", "01510101010", "rokeya@example.com", "Mymensingh", "Female", "17-12-2001", "12-09-2025", "10:40:00"),
    (13, "Jahidul Karim", "01720202020", "jahid@example.com", "Dhaka", "Male", "21-04-2002", "13-09-2025", "11:25:00"),
    (14, "Lamia Akter", "01930303030", "lamia@example.com", "Sylhet", "Female", "09-02-2001", "14-09-2025", "12:15:00"),
    (15, "Mehedi Hasan", "01840404040", "mehedi@example.com", "Chittagong", "Male", "02-07-1999", "15-09-2025", "09:35:00"),
    (16, "Shamima Khatun", "01650505050", "shamima@example.com", "Rajshahi", "Female", "30-10-2000", "16-09-2025", "10:55:00"),
    (17, "Arman Hossain", "01760606060", "arman@example.com", "Khulna", "Male", "11-08-2001", "17-09-2025", "11:45:00"),
    (18, "Salma Akter", "01570707070", "salma@example.com", "Barisal", "Female", "25-09-2002", "18-09-2025", "12:05:00"),
    (19, "Naimur Rahman", "01980808080", "naim@example.com", "Rangpur", "Male", "07-01-2000", "19-09-2025", "09:40:00"),
    (20, "Shila Begum", "01890909090", "shila@example.com", "Comilla", "Female", "19-05-2001", "20-09-2025", "10:35:00"),
    (21, "Asif Mahmud", "01711112222", "asif@example.com", "Dhaka", "Male", "10-12-1999", "21-09-2025", "11:15:00"),
    (22, "Parveen Akter", "01822223333", "parveen@example.com", "Chittagong", "Female", "14-03-2000", "22-09-2025", "12:10:00"),
    (23, "Hasan Mahmud", "01533334444", "hasan@example.com", "Sylhet", "Male", "22-06-2002", "23-09-2025", "09:25:00"),
    (24, "Nadia Rahman", "01644445555", "nadia@example.com", "Rajshahi", "Female", "03-09-2001", "24-09-2025", "10:45:00"),
    (25, "Faisal Karim", "01955556666", "faisal@example.com", "Khulna", "Male", "29-04-2000", "25-09-2025", "11:55:00"),
    (26, "Sumaiya Jahan", "01766667777", "sumaiya@example.com", "Mymensingh", "Female", "18-11-2002", "26-09-2025", "12:20:00"),
    (27, "Imran Hossain", "01877778888", "imran@example.com", "Bogura", "Male", "27-02-2001", "27-09-2025", "09:30:00"),
    (28, "Shamima Nasrin", "01588889999", "nasrin@example.com", "Barisal", "Female", "06-07-2000", "28-09-2025", "10:50:00"),
    (29, "Tareq Aziz", "01699990000", "tareq@example.com", "Dhaka", "Male", "12-10-2001", "29-09-2025", "11:35:00"),
    (30, "Sharmin Akter", "01910101111", "sharmin@example.com", "Chittagong", "Female", "25-05-2002", "30-09-2025", "12:25:00"),
    (31, "Rafiul Islam", "01712121212", "rafiul@example.com", "Sylhet", "Male", "01-01-2000", "01-10-2025", "09:20:00"),
    (32, "Mahira Chowdhury", "01813131313", "mahira@example.com", "Comilla", "Female", "15-04-2001", "02-10-2025", "10:15:00"),
    (33, "Sakib Hasan", "01514141414", "sakib@example.com", "Rangpur", "Male", "28-09-1999", "03-10-2025", "11:05:00"),
    (34, "Afroza Sultana", "01615151515", "afroza@example.com", "Khulna", "Female", "07-07-2002", "04-10-2025", "12:35:00"),
    (35, "Mamun Ahmed", "01916161616", "mamun@example.com", "Dhaka", "Male", "19-02-2001", "05-10-2025", "09:55:00"),
    (36, "Jannatul Ferdous", "01717171717", "jannatul@example.com", "Rajshahi", "Female", "22-08-2000", "06-10-2025", "10:25:00"),
    (37, "Shahriar Kabir", "01818181818", "shahriar@example.com", "Bogura", "Male", "03-12-2001", "07-10-2025", "11:50:00"),
    (38, "Moushumi Akter", "01519191919", "moushumi@example.com", "Mymensingh", "Female", "17-06-2002", "08-10-2025", "12:40:00"),
    (39, "Anisur Rahman", "01620202020", "anisur@example.com", "Comilla", "Male", "09-03-2000", "09-10-2025", "09:40:00"),
    (40, "Shaila Sultana", "01921212121", "shaila@example.com", "Barisal", "Female", "31-01-2001", "10-10-2025", "10:30:00"),
    (41, "Touhidul Islam", "01722223232", "touhid@example.com", "Dhaka", "Male", "13-09-2002", "11-10-2025", "11:20:00"),
    (42, "Rumana Khatun", "01823232323", "rumana@example.com", "Rajshahi", "Female", "24-11-2000", "12-10-2025", "12:15:00")
]


# Functions
def show_students(offline=False):
    """Show all students from DB (if connected) or offline for users"""
    studentTable.delete(*studentTable.get_children())
    try:
        if offline or mycursor is None:
            for row in offline_students:
                studentTable.insert("", END, values=row)
            return
        mycursor.execute("SELECT * FROM student")
        data = mycursor.fetchall()
        for row in data:
            studentTable.insert("", END, values=row)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to load data:\n{e}")

def add_student():
    if mycursor is None:
        messagebox.showerror("Error", "Please connect to the database first.")
        return

    def save_student():
        if (idEntry.get().strip() == "" or nameEntry.get().strip() == "" or
            phoneEntry.get().strip() == "" or emailEntry.get().strip() == "" or
            addressEntry.get().strip() == "" or genderCombo.get().strip() == "" or
            dobEntry.get().strip() == ""):
            messagebox.showerror("Error", "All fields are required!", parent=add_window)
            return
        if not phoneEntry.get().isdigit():
            messagebox.showerror("Error", "Phone must be digits only.", parent=add_window)
            return

        try:
            current_date = time.strftime("%d-%m-%Y")
            current_time = time.strftime("%H:%M:%S")
            mycursor.execute(
                "INSERT INTO student (id, name, mobile, email, address, gender, dob, date, time) "
                "VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                (
                    idEntry.get().strip(),
                    nameEntry.get().strip(),
                    phoneEntry.get().strip(),
                    emailEntry.get().strip(),
                    addressEntry.get().strip(),
                    genderCombo.get().strip(),
                    dobEntry.get().strip(),
                    current_date,
                    current_time
                )
            )
            con.commit()
            messagebox.showinfo("Success", "Student Added Successfully!", parent=add_window)
            show_students()
            add_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add student:\n{e}", parent=add_window)

    add_window = Toplevel(root)
    add_window.title("Add Student")
    add_window.geometry("520x520+220+150")
    add_window.resizable(False, False)

    Label(add_window, text='ID:', font=('times new roman', 15, 'bold')).grid(row=0, column=0, padx=20, pady=10, sticky="w")
    idEntry = Entry(add_window, font=('times new roman', 15, 'bold'))
    idEntry.grid(row=0, column=1, padx=20, pady=10)

    Label(add_window, text="Name:", font=("times new roman", 15, "bold")).grid(row=1, column=0, padx=20, pady=10, sticky="w")
    nameEntry = Entry(add_window, font=("times new roman", 15, "bold"))
    nameEntry.grid(row=1, column=1, padx=20, pady=10)

    Label(add_window, text="Phone:", font=("times new roman", 15, "bold")).grid(row=2, column=0, padx=20, pady=10, sticky="w")
    phoneEntry = Entry(add_window, font=("times new roman", 15, "bold"))
    phoneEntry.grid(row=2, column=1, padx=20, pady=10)

    Label(add_window, text="Email:", font=("times new roman", 15, "bold")).grid(row=3, column=0, padx=20, pady=10, sticky="w")
    emailEntry = Entry(add_window, font=("times new roman", 15, "bold"))
    emailEntry.grid(row=3, column=1, padx=20, pady=10)

    Label(add_window, text="Address:", font=("times new roman", 15, "bold")).grid(row=4, column=0, padx=20, pady=10, sticky="w")
    addressEntry = Entry(add_window, font=('times new roman', 15, 'bold'))
    addressEntry.grid(row=4, column=1, padx=20, pady=10)

    Label(add_window, text="Gender:", font=("times new roman", 15, "bold")).grid(row=5, column=0, padx=20, pady=10, sticky="w")
    genderCombo = ttk.Combobox(add_window, values=("Male", "Female", "Other"),
                               font=("times new roman", 15, "bold"), state="readonly")
    genderCombo.grid(row=5, column=1, padx=20, pady=10)
    genderCombo.current(0)

    Label(add_window, text="D.O.B:", font=("times new roman", 15, "bold")).grid(row=6, column=0, padx=20, pady=10, sticky="w")
    dobEntry = Entry(add_window, font=('times new roman', 15, 'bold'))
    dobEntry.grid(row=6, column=1, padx=20, pady=10)

    Button(add_window, text="➕ ADD STUDENT", font=("times new roman", 15, "bold"),
           bg="lightgreen", width=20, command=save_student).grid(row=7, column=1, pady=20)

def search_student(offline=False):
    search_window = Toplevel(root)
    search_window.title("Search Student")
    search_window.geometry("400x200+300+200")

    Label(search_window, text="Search by ID or Name:", font=("times new roman", 14, "bold")).pack(pady=10)
    searchEntry = Entry(search_window, font=("times new roman", 14))
    searchEntry.pack(pady=5)

    def perform_search():
        query = searchEntry.get().strip()
        if query == "":
            messagebox.showerror("Error", "Please enter a search term.", parent=search_window)
            return
        try:
            studentTable.delete(*studentTable.get_children())
            if offline or mycursor is None:
                for row in offline_students:
                    if str(row[0]) == query or query.lower() in row[1].lower():
                        studentTable.insert("", END, values=row)
            else:
                mycursor.execute("SELECT * FROM student WHERE id=%s OR name LIKE %s", (query, f"%{query}%"))
                data = mycursor.fetchall()
                for row in data:
                    studentTable.insert("", END, values=row)
            search_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Search failed:\n{e}", parent=search_window)

    Button(search_window, text="SEARCH", font=("times new roman", 14, "bold"),
           bg="lightblue", command=perform_search).pack(pady=10)

def delete_student():
    selected = studentTable.focus()
    if not selected:
        messagebox.showerror("Error", "Please select a student to delete.")
        return
    values = studentTable.item(selected, 'values')
    student_id = values[0]
    confirm = messagebox.askyesno("Confirm Delete", f"Delete student ID {student_id}?")
    if confirm:
        try:
            mycursor.execute("DELETE FROM student WHERE id=%s", (student_id,))
            con.commit()
            show_students()
            messagebox.showinfo("Success", "Student deleted successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete:\n{e}")

def update_student():
    selected = studentTable.focus()
    if not selected:
        messagebox.showerror("Error", "Please select a student to update.")
        return
    values = studentTable.item(selected, 'values')

    update_window = Toplevel(root)
    update_window.title("Update Student")
    update_window.geometry("520x520+220+150")

    # Labels & Entries
    Label(update_window, text='ID:', font=('times new roman', 15, 'bold')).grid(row=0, column=0, padx=20, pady=10, sticky="w")
    idEntry = Entry(update_window, font=('times new roman', 15, 'bold'))
    idEntry.grid(row=0, column=1, padx=20, pady=10)
    idEntry.insert(0, values[0])
    idEntry.config(state='disabled')

    Label(update_window, text="Name:", font=("times new roman", 15, "bold")).grid(row=1, column=0, padx=20, pady=10, sticky="w")
    nameEntry = Entry(update_window, font=('times new roman', 15, 'bold'))
    nameEntry.grid(row=1, column=1, padx=20, pady=10)
    nameEntry.insert(0, values[1])

    Label(update_window, text="Phone:", font=("times new roman", 15, "bold")).grid(row=2, column=0, padx=20, pady=10, sticky="w")
    phoneEntry = Entry(update_window, font=('times new roman', 15, 'bold'))
    phoneEntry.grid(row=2, column=1, padx=20, pady=10)
    phoneEntry.insert(0, values[2])

    Label(update_window, text="Email:", font=("times new roman", 15, "bold")).grid(row=3, column=0, padx=20, pady=10, sticky="w")
    emailEntry = Entry(update_window, font=('times new roman', 15, 'bold'))
    emailEntry.grid(row=3, column=1, padx=20, pady=10)
    emailEntry.insert(0, values[3])

    Label(update_window, text="Address:", font=("times new roman", 15, "bold")).grid(row=4, column=0, padx=20, pady=10, sticky="w")
    addressEntry = Entry(update_window, font=('times new roman', 15, 'bold'))
    addressEntry.grid(row=4, column=1, padx=20, pady=10)
    addressEntry.insert(0, values[4])

    Label(update_window, text="Gender:", font=("times new roman", 15, "bold")).grid(row=5, column=0, padx=20, pady=10, sticky="w")
    genderCombo = ttk.Combobox(update_window, values=("Male", "Female", "Other"),
                               font=("times new roman", 15, "bold"), state="readonly")
    genderCombo.grid(row=5, column=1, padx=20, pady=10)
    genderCombo.set(values[5])

    Label(update_window, text="D.O.B:", font=("times new roman", 15, "bold")).grid(row=6, column=0, padx=20, pady=10, sticky="w")
    dobEntry = Entry(update_window, font=('times new roman', 15, 'bold'))
    dobEntry.grid(row=6, column=1, padx=20, pady=10)
    dobEntry.insert(0, values[6])

    def save_update():
        try:
            mycursor.execute(
                "UPDATE student SET name=%s, mobile=%s, email=%s, address=%s, gender=%s, dob=%s WHERE id=%s",
                (nameEntry.get().strip(), phoneEntry.get().strip(), emailEntry.get().strip(),
                 addressEntry.get().strip(), genderCombo.get().strip(), dobEntry.get().strip(), values[0])
            )
            con.commit()
            show_students()
            messagebox.showinfo("Success", "Student updated successfully.")
            update_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update:\n{e}")

    Button(update_window, text="UPDATE STUDENT", font=("times new roman", 15, "bold"),
           bg="lightblue", width=20, command=save_update).grid(row=7, column=1, pady=20)

def export_data():
    if mycursor is None:
        messagebox.showerror("Error", "Please connect to the database first.")
        return
    try:
        mycursor.execute("SELECT * FROM student")
        data = mycursor.fetchall()
        if not data:
            messagebox.showinfo("No Data", "No data to export.")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".csv",
                                                 filetypes=[("CSV files", "*.csv")])
        if file_path:
            with open(file_path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["ID","Name","Mobile","Email","Address","Gender","DOB","Date","Time"])
                writer.writerows(data)
            messagebox.showinfo("Success", f"Data exported to {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to export data:\n{e}")

# Database Connection
def open_connect_window():
    connectWindow = Toplevel(root)
    connectWindow.geometry('470x300+730+230')
    connectWindow.title("Database Connection")
    connectWindow.resizable(False, False)

    Label(connectWindow, text="Host name", font=("Arial", 14, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky="w")
    hostnameEntry = Entry(connectWindow, font=("roman", 15, "bold"), bd=5)
    hostnameEntry.grid(row=0, column=1, padx=10, pady=10)

    Label(connectWindow, text="User name", font=("Arial", 14, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky="w")
    usernameEntry = Entry(connectWindow, font=("roman", 15, "bold"), bd=5)
    usernameEntry.grid(row=1, column=1, padx=10, pady=10)

    Label(connectWindow, text="Password", font=("Arial", 14, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky="w")
    passwordEntry = Entry(connectWindow, font=("roman", 15, "bold"), bd=5, show="*")
    passwordEntry.grid(row=2, column=1, padx=10, pady=10)

    def connect_database():
        try:
            global con, mycursor
            con = pymysql.connect(
                host=hostnameEntry.get(),
                user=usernameEntry.get(),
                password=passwordEntry.get()
            )
            mycursor = con.cursor()
            mycursor.execute("CREATE DATABASE IF NOT EXISTS studentmanagementsystem")
            mycursor.execute("USE studentmanagementsystem")
            mycursor.execute('''CREATE TABLE IF NOT EXISTS student(
                                    id INT PRIMARY KEY,
                                    name VARCHAR(30),
                                    mobile VARCHAR(10),
                                    email VARCHAR(30),
                                    address VARCHAR(100),
                                    gender VARCHAR(20),
                                    dob VARCHAR(20),
                                    date VARCHAR(50),
                                    time VARCHAR(50))''')
            messagebox.showinfo("Success", "Database Connected Successfully!", parent=connectWindow)

            # Enable Admin buttons
            addstudentButton.config(state=NORMAL)
            searchstudentButton.config(state=NORMAL)
            deletestudentButton.config(state=NORMAL)
            updatestudentButton.config(state=NORMAL)
            showstudentButton.config(state=NORMAL)
            exportstudentButton.config(state=NORMAL)

            connectWindow.destroy()
            show_students()
        except Exception as e:
            messagebox.showerror("Error", f"Database connection failed:\n{e}", parent=connectWindow)

    ttk.Button(connectWindow, text="CONNECT", command=connect_database).grid(row=3, column=1, pady=20)

# GUI Setup
root = ThemedTk(theme="radiance")
root.geometry("1174x700+200+50")
root.title("Student Management System")
root.resizable(False, False)

# Clock
datetimeLabel = Label(root, font=("times new roman", 14, "bold"))
datetimeLabel.place(x=5, y=5)
def clock():
    current_time = time.strftime("%H:%M:%S")
    current_date = time.strftime("%d-%m-%Y")
    datetimeLabel.config(text=f"Date: {current_date}\nTime: {current_time}")
    datetimeLabel.after(1000, clock)
clock()

# Marquee
s = "Welcome to Student Management System"
count = 0
text = ''
sliderLabel = Label(root, font=("times new roman", 28, "italic bold"),
                    relief=RIDGE, borderwidth=4, width=35, bg="lightblue")
sliderLabel.place(x=200, y=0)
def slider():
    global text, count
    if count >= len(s):
        text = ''
        count = 0
    text += s[count]
    sliderLabel.config(text=text)
    count += 1
    sliderLabel.after(200, slider)
slider()

# Connect Button
connectButton = Button(root, text="Connect Database", command=open_connect_window,
                       font=("times new roman", 14, "bold"), relief=RIDGE,
                       borderwidth=4, bg="lightgreen")
connectButton.place(x=980, y=0)

# Left Frame Buttons
leftFrame = Frame(root, relief=RIDGE, borderwidth=4, bg="lightyellow")
leftFrame.place(x=50, y=80, width=300, height=600)

try:
    logo_img = Image.open("stu.png")
    logo_img = logo_img.resize((200, 200))
    logo_photo = ImageTk.PhotoImage(logo_img)
    logoLabel = Label(leftFrame, image=logo_photo, bg="lightyellow")
    logoLabel.pack(pady=10)
except:
    Label(leftFrame, text="Student\nManagement\nSystem", font=("times new roman", 18, "bold"), bg="lightyellow").pack(pady=20)

# Buttons
addstudentButton = Button(leftFrame, text="Add Student", width=25,
                          font=("times new roman", 14, "bold"),
                          state=DISABLED, command=add_student)
addstudentButton.pack(pady=5)

searchstudentButton = Button(leftFrame, text="Search Student", width=25,
                             font=("times new roman", 14, "bold"),
                             command=lambda: search_student(offline=True))
searchstudentButton.pack(pady=5)

deletestudentButton = Button(leftFrame, text="Delete Student", width=25,
                             font=("times new roman", 14, "bold"),
                             state=DISABLED, command=delete_student)
deletestudentButton.pack(pady=5)

updatestudentButton = Button(leftFrame, text="Update Student", width=25,
                             font=("times new roman", 14, "bold"),
                             state=DISABLED, command=update_student)
updatestudentButton.pack(pady=5)

showstudentButton = Button(leftFrame, text="Show Student", width=25,
                           font=("times new roman", 14, "bold"),
                           command=lambda: show_students(offline=True))
showstudentButton.pack(pady=5)

exportstudentButton = Button(leftFrame, text="Export Data", width=25,
                             font=("times new roman", 14, "bold"),
                             state=DISABLED, command=export_data)
exportstudentButton.pack(pady=5)

exitButton = Button(leftFrame, text="Exit", width=25,
                    font=("times new roman", 14, "bold"), command=root.destroy)
exitButton.pack(pady=5)

# Right Frame (Treeview)
rightFrame = Frame(root, relief=RIDGE, borderwidth=4, bg="lightblue")
rightFrame.place(x=400, y=80, width=750, height=600)

scroll_x = Scrollbar(rightFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(rightFrame, orient=VERTICAL)
studentTable = ttk.Treeview(
    rightFrame,
    columns=("id", "name", "mobile", "email", "address", "gender", "dob", "date", "time"),
    xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set
)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studentTable.xview)
scroll_y.config(command=studentTable.yview)

for col in ("id", "name", "mobile", "email", "address", "gender", "dob", "date", "time"):
    studentTable.heading(col, text=col.capitalize())
studentTable['show'] = 'headings'
studentTable.pack(fill=BOTH, expand=1)


show_students(offline=True)

root.mainloop()
