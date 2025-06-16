import pyodbc
import tkinter as tk
from tkinter import messagebox
#import random as ra

server = 'LAPTOP-6OAGUS7Q' 
database = 'savbang' 

connection_string = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'  
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)

def insert_data():
    #id_val=ra.randint(10, 100)
    name = name_entry.get()
    age = age_entry.get()
    gender = gender_entry.get()
    roll_no = roll_no_entry.get()
    
    if not name or not age or not gender or not roll_no :
        messagebox.showwarning("Input Error", "Please enter a valid user")
        return

    conn = pyodbc.connect(connection_string)
    try:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO [dbo].[TblStudent] (Name, Age, Gender, RollNo) VALUES (?, ?, ?, ?)",(name, age, gender, roll_no))
        conn.commit()
        messagebox.showinfo("Success", "Data inserted successfully.")
        name = name_entry.delete(0, tk.END)
        age = age_entry.delete(0, tk.END)
        gender = gender_entry.delete(0, tk.END)
        roll_no = roll_no_entry.delete(0, tk.END)

    except pyodbc.Error as ex:
        messagebox.showerror("Database Error", f"Error: {ex}")
    finally:
        if conn:
            conn.close()

root = tk.Tk()
root.title("Insert Student Data")

tk.Label(root, text="Name:").pack(pady=5)
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root,text="Age:").pack(pady=5)
age_entry = tk.Entry(root)
age_entry.pack()

tk.Label(root,text="Gender").pack(pady=5)
gender_entry=tk.Entry(root)
gender_entry.pack()

tk.Label(root, text="Roll No:").pack(pady=5)
roll_no_entry = tk.Entry(root)
roll_no_entry.pack()

insert_button = tk.Button(root, text="Insert Student Data", command=insert_data).pack(pady=5)

root.mainloop()
