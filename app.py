import pyodbc
import tkinter as tk
from tkinter import scrolledtext

server = 'LAPTOP-6OAGUS7Q' 
database = 'savbang' 

connection_string = (
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'  
    f'SERVER={server};'
    f'DATABASE={database};'
    f'Trusted_Connection=yes;'
)

def fetch_data():
    conn = pyodbc.connect(connection_string)
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM [dbo].[TblStudent]")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
        text_area.delete(1.0, tk.END)
        
        for row in rows:
            text_area.insert(tk.END, f"ID: {row.ID}, Name: {row.Name}, AGE: {row.Age}, GENDER: {row.Gender}, Roll No: {row.Rollno}, \n")

    except pyodbc.Error as ex:
        text_area.insert(tk.END, f"Error: {ex}\n")
    finally:
        if conn:
            conn.close()

root = tk.Tk()
root.title("Student Data")

#fetch_button = tk.Button(root, text="Fetch Student Data", command=fetch_data)
#fetch_button.pack(pady=10)

text_area = scrolledtext.ScrolledText(root, width=100, height=50)
text_area.pack(pady=10)
fetch_data()
root.mainloop()
