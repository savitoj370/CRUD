import pyodbc
import tkinter as tk
from tkinter import messagebox

server = 'LAPTOP-6OAGUS7Q' 
database = 'savbang' 

conn_str = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'  
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)

def update_data():
    id_val=id_entry.get()
    if not id_val:
        messagebox.showwarning("Input Error", "Please enter a valid user")
        return
    conn=pyodbc.connect(conn_str)
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM [dbo].[TblStudent] WHERE ID = ?",(id_val))
        conn.commit()
        messagebox.showinfo("Success", "Data Deleted successfully.")
    except pyodbc.Error as ex:
        messagebox.showerror("Database Error", f"Error: {ex}")
    finally:
        if conn:
            conn.close()
root = tk.Tk()
root.title("Remove Student ID Data")

tk.Label(root, text="ID:").pack(pady=5)
id_entry = tk.Entry(root)
id_entry.pack()

insert_button = tk.Button(root, text="Done", command=update_data).pack(pady=5)

root.mainloop()