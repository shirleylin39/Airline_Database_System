
import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
import table



class AirlineDatabaseGUI:

    def __init__(self, master):
        self.master = master
        master.title("Airline Database")

        master.minsize(width=1000, height=600)

        self.title_label = tk.Label(master, text="Airline Database System", font=("Arial", 24))
        self.title_label.pack(pady=20)

        button_width = 20

        self.new_button = tk.Button(master, text="New Flight", command=self.new_flight, width=button_width)
        self.new_button.pack(pady=5)

        self.search_button = tk.Button(master, text ="Search Flight", command = self.search_flight, width=button_width)
        self.search_button.pack(pady=5)

        self.browse_flight_button = tk.Button(master, text="Browse Flights", command=self.browse_flight, width=button_width)
        self.browse_flight_button.pack(pady=5)

        self.browse_aircraft_button = tk.Button(master, text="Browse Aircrafts", command=self.browse_aircraft, width=button_width)
        self.browse_aircraft_button.pack(pady=5)

        self.browse_pilot_button = tk.Button(master, text="Browse Pilots", command=self.browse_pilot, width=button_width)
        self.browse_pilot_button.pack(pady=5)

    def new_flight(self):
        conn = sqlite3.connect('airline_database.db')
        c = conn.cursor()

        new_flight_window = tk.Toplevel(self.master)
        new_flight_window.title("New Flight")

        new_flight_window.minsize(width=500, height=900)

        instructions = [
            "Enter Flight ID:",
            "Enter Departure Country:",
            "Enter Departure City:",
            "Enter Departure Airport Code:",
            "Enter Local Departure Date/Time (YYYY-MM-DD HH:MM):",
            "Enter Departure Timezone:",
            "Enter Arrival Country:",  
            "Enter Arrival City:",
            "Enter Arrival Airport Code:",
            "Enter Local Arrival Date/Time (YYYY-MM-DD HH:MM):",
            "Enter Arrival Timezone:",
            "Enter Total Flight Time:",
            "Select Aircraft ID:",
            "Select Pilot ID:"]
    
        entries = {}

        for instruction in instructions:
            label = tk.Label(new_flight_window, text=instruction)
            label.pack()

            if "Select Aircraft ID:" in instruction:
                c.execute("SELECT AircraftID FROM Aircraft")
                aircraft_ids = [row[0] for row in c.fetchall()]

                selected_aircraft_id = tk.StringVar(new_flight_window)
                entry = ttk.Combobox(new_flight_window, textvariable=selected_aircraft_id)
                entry['values'] = aircraft_ids
                entry.pack()

            elif "Select Pilot ID:" in instruction:
                c.execute("SELECT PilotID FROM Pilot")
                pilot_ids = [row[0] for row in c.fetchall()]

                selected_pilot_id = tk.StringVar(new_flight_window)
                entry = ttk.Combobox(new_flight_window, textvariable=selected_pilot_id)
                entry['values'] = pilot_ids
                entry.pack()
      
            else:
                entry = tk.Entry(new_flight_window)
                entry.pack()
      
            entries[instruction] = entry

        def get_user_input():
            user_inputs = {key: entry.get() for key, entry in entries.items()}
            return user_inputs

        def submit_flight():
            user_inputs = get_user_input()
            flight_id_value = user_inputs["Enter Flight ID:"]
            departure_country_value = user_inputs["Enter Departure Country:"]
            departure_city_value = user_inputs["Enter Departure City:"]
            departure_airport_code_value = user_inputs["Enter Departure Airport Code:"]
            departure_date_time_local_value = user_inputs["Enter Local Departure Date/Time (YYYY-MM-DD HH:MM):"]
            departure_date_timezone_value = user_inputs["Enter Departure Timezone:"]
            arrival_country_value = user_inputs["Enter Arrival Country:"]
            arrival_city_value = user_inputs["Enter Arrival City:"]
            arrival_airport_code_value = user_inputs["Enter Arrival Airport Code:"]
            arrival_date_time_local_value = user_inputs["Enter Local Arrival Date/Time (YYYY-MM-DD HH:MM):"]
            arrival_date_timezone_value = user_inputs["Enter Arrival Timezone:"]
            total_flight_time_value = user_inputs["Enter Total Flight Time:"]
            selected_aircraft_id_value = user_inputs["Select Aircraft ID:"]
            selected_pilot_id_value = user_inputs["Select Pilot ID:"]
      

        submit_button = tk.Button(new_flight_window, text="Confirm", command=submit_flight)
        submit_button.pack()

        back_button_new = tk.Button(new_flight_window, text="Back", command=new_flight_window.destroy)
        back_button_new.pack()

    def search_flight(self):
        conn = sqlite3.connect('airline_database.db')
        c = conn.cursor()

        search_flight_window = tk.Toplevel(self.master)
        search_flight_window.title("Search Flight")

        search_flight_window.minsize(width=500, height=900)

        entity_label = tk.Label(search_flight_window, text="Label:")
        entity_label.pack()

        entity_var = tk.StringVar(search_flight_window)
        entities = ["Flight ID","Aircraft ID", "Pilot ID","Departure Country", "Departure City", "Departure Airport Code","Departure Local Date/Time", "Arrival Country", "Arrival City", "Arrival Airport Code", "Arrival Local Date/Time"]
        entity_dropdown = ttk.Combobox(search_flight_window, textvariable=entity_var, values=entities)
        entity_dropdown.pack()

        value_label = tk.Label(search_flight_window, text="Enter know information:")
        value_label.pack()

        value_entry = tk.Entry(search_flight_window)
        value_entry.pack()

        def submit_search():
            entity = entity_var.get()
            value = value_entry.get()
    
            c.execute(f'''
                SELECT * FROM Flight
                WHERE "{entity}" LIKE ?
            ''', ('%' + value + '%',))
      
            results = c.fetchall()

            search_results_window = tk.Toplevel(self.master)
            search_results_window.title("Search Results")

            headers = ["Flight ID", "Departure Country", "Departure City", "Departure Airport", "Departure Local Date/Time", "Departure Time Zone", "Arrival Country", "Arrival City", "Arrival Airport", "Arrival Local Date/Time", "Arrival Time Zone","Total Flight Time", "Aircraft ID", "Pilot ID"]

            tree = ttk.Treeview(search_results_window)
            tree["columns"] = tuple(range(len(results[0])))  
            tree["show"] = "headings"

            for i, header in enumerate(headers):
                tree.heading(i, text=header)
                tree.column(i, width=50)  
          
            for result in results:
                tree.insert("", "end", values=result)

            tree.pack()

            back_button = tk.Button(search_results_window, text="Back", command=search_results_window.destroy)
            back_button.pack()

        submit_button = tk.Button(search_flight_window, text="Search", command=submit_search)
        submit_button.pack()
        back_button_search = tk.Button(search_flight_window, text="Back", command=search_flight_window.destroy)
        back_button_search.pack()

    def browse_flight(self):

        conn = sqlite3.connect('airline_database.db')
        c = conn.cursor()



        browse_flight_window = tk.Toplevel(self.master)
        browse_flight_window.title("Browse Flights")

        browse_flight_window.minsize(width=500, height=900)

        c.execute("SELECT * FROM Flight")
        flight_data = c.fetchall()

        flight_headers = ["Flight ID", "Departure Country", "Departure City", "Departure Airport", "Departure Local Date/Time", "Departure Time Zone", "Arrival Country", "Arrival City", "Arrival Airport", "Arrival Local Date/Time", "Arrival Time Zone", "Total Flight Time", "Aircraft ID", "Pilot ID"]

        tree = ttk.Treeview(browse_flight_window, columns=tuple(range(len(flight_data[0]))), show="headings")
        for i, header in enumerate(flight_headers):
            tree.heading(i, text=header)
            tree.column(i, width=50)
        for row in flight_data:
            tree.insert("", "end", values=row)
        tree.pack()

        back_button_search = tk.Button(browse_flight_window, text="Back", command=browse_flight_window.destroy)
        back_button_search.pack()

    def browse_aircraft(self):

        conn = sqlite3.connect('airline_database.db')
        c = conn.cursor()

        browse_aircraft_window = tk.Toplevel(self.master)
        browse_aircraft_window.title("Browse Aircrafts")

        browse_aircraft_window.minsize(width=500, height=900)

        c.execute("SELECT * FROM Aircraft")
        aircraft_data = c.fetchall()
        aircraft_headers = ["Aircraft ID", "Aircraft Model", "Capacity", "Manufacture Date", "Last Maintainence Date"]

        tree = ttk.Treeview(browse_aircraft_window, columns=tuple(range(len(aircraft_data[0]))), show="headings")
        for i, header in enumerate(aircraft_headers):
            tree.heading(i, text=header)
            tree.column(i, width=100)
        for row in aircraft_data:
            tree.insert("", "end", values=row)
        tree.pack()

        back_button_search = tk.Button(browse_aircraft_window, text="Back", command=browse_aircraft_window.destroy)
        back_button_search.pack()

    def browse_pilot(self):
        conn = sqlite3.connect('airline_database.db')
        c = conn.cursor()

        browse_pilot_window = tk.Toplevel(self.master)
        browse_pilot_window.title("Browse Pilots")

        browse_pilot_window.minsize(width=500, height=900)

        c.execute("SELECT * FROM Pilot")
        pilot_data = c.fetchall()
        pilot_headers = ["Pilot ID", "License ID", "Name", "Nationality", "Gender", "Date of Birth", "Onboard Date"]

        tree = ttk.Treeview(browse_pilot_window, columns=tuple(range(len(pilot_data[0]))), show="headings")
        for i, header in enumerate(pilot_headers):
            tree.heading(i, text=header)
            tree.column(i, width=100)
        for row in pilot_data:
            tree.insert("", "end", values=row)
        tree.pack()

        back_button_search = tk.Button(browse_pilot_window, text="Back", command=browse_pilot_window.destroy)
        back_button_search.pack()
