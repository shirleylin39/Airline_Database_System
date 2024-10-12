import sqlite3
import tkinter as tk
from table import airline_table
from interface import AirlineDatabaseGUI

def main():
    conn = sqlite3.connect('airline_database.db')
    c = conn.cursor()

    airline_table(c)
     
    root = tk.Tk()
    AirlineDatabaseGUI(root)
    root.mainloop()

    conn.close()

if __name__ == "__main__":
    main()