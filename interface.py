
import sqlite3
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import *
from datetime import datetime, timedelta


conn = sqlite3.connect('airline_database.db')
c = conn.cursor()


class AirlineDatabaseGUI:
    def __init__(self, master):

        self.master = master
        master.title("Airline Database")

        master.minsize(width=1920, height=1080)

        self.content_frame = tk.Frame(master)
        self.content_frame.pack(fill="both", expand=True)

        self.main_page()

    def main_page(self):

        self.clear_content()

        self.title_label = tk.Label(self.content_frame, text="Airline Database System", font=("Arial", 24))
        self.title_label.pack(pady=20)

        button_width = 30
        button_height = 2 

        self.browse_flight_button = tk.Button(self.content_frame, text="Scheduled Flights", command=self.browse_flight, width=button_width, height=button_height)
        self.browse_flight_button.pack(pady=5)

        self.browse_aircraft_button = tk.Button(self.content_frame, text="Current Aircrafts", command=self.browse_aircraft, width=button_width, height=button_height)
        self.browse_aircraft_button.pack(pady=5)

        self.browse_pilot_button = tk.Button(self.content_frame, text="Current Pilots", command=self.browse_pilot, width=button_width, height=button_height)
        self.browse_pilot_button.pack(pady=5)

    def flight_duration(self,departure_time_local, departure_timezone, arrival_time_local, arrival_timezone):

        departure_time = datetime.strptime(departure_time_local, "%Y-%m-%d %H:%M")
        arrival_time = datetime.strptime(arrival_time_local, "%Y-%m-%d %H:%M")
    
        departure_offset = int(departure_timezone.replace("UTC", ""))
        arrival_offset = int(arrival_timezone.replace("UTC", ""))
    
        departure_utc_time = departure_time - timedelta(hours=departure_offset)
        arrival_utc_time = arrival_time - timedelta(hours=arrival_offset)
    
        duration = arrival_utc_time - departure_utc_time


        if duration.total_seconds() < 0:
            duration += timedelta(days=1)

        return str(duration)

    def browse_flight(self):
        
        self.clear_content()
        tk.Label(self.content_frame, text="Scheduled Flights", font=("Arial", 18)).pack(pady=10)

        c.execute(("""
            SELECT 
                f.FlightID,
                da.Country AS DepartureCountry,
                da.City AS DepartureCity,
                f.DepartureAirportCode,
                f.DepartureDateTime_Local,
                da.TimeZone AS DepartureTimeZone,
                aa.Country AS ArrivalCountry,
                aa.City AS ArrivalCity,
                f.ArrivalAirportCode,
                f.ArrivalDateTime_Local,
                aa.TimeZone AS ArrivalTimeZone,
                f.AircraftID,
                f.PilotID
            FROM 
                Flight f
            JOIN 
                Airport da ON f.DepartureAirportCode = da.AirportCode
            JOIN 
                Airport aa ON f.ArrivalAirportCode = aa.AirportCode
        """))
        flight_data = c.fetchall()

        flight_headers = ["Flight ID", "Departure Country", "City", "Airport", "Local Date/Time", "Time Zone", "Arrival Country", "City", "Airport", "Local Date/Time", "Time Zone", "Flight Duration", "Aircraft ID", "Pilot ID"]
        column_widths = [85, 150, 115, 65, 135, 75, 150, 115, 65, 135, 75, 105, 95, 95]

        tree = ttk.Treeview(self.content_frame, columns=tuple(range(14)), show="headings", height=30)
        for i, header in enumerate(flight_headers):
            tree.heading(i, text=header)
            tree.column(i, width=column_widths[i])
        for row in flight_data:
            flight_time = self.flight_duration(row[4], row[5], row[9], row[10])
            row_with_duration = row[:11] + (flight_time,) + row[11:]
            tree.insert("", "end", values=row_with_duration)    

        tree.pack()

        button_width=20
        #search_button = tk.Button(self.content_frame, text ="Search", command = self.search_flight, width=button_width)
        #search_button.pack(pady=5)
        edit_button= tk.Button(self.content_frame, text="Edit Selected Flight", command=lambda: self.edit_flight(tree), width=button_width)
        edit_button.pack(pady=5)
        delete_button = tk.Button(self.content_frame, text="Delete Selected Flight", command=lambda: delete_flight(tree), width=button_width)
        delete_button.pack(pady=5)
        new_button= tk.Button(self.content_frame, text="Add New Flight", command=self.new_flight, width=button_width)
        new_button.pack(pady=5)
        back_button= tk.Button(self.content_frame, text="Back", command=self.main_page, width=button_width)
        back_button.pack(pady=5)

        def delete_flight(tree):
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("No Selection", "Please select a flight to delete.")
                return
            
            flight_id = tree.item(selected_item)["values"][0]
            confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete flight {flight_id}?")
            if confirm:
                try:
                    c.execute("DELETE FROM Flight WHERE FlightID = ?", (flight_id,))
                    conn.commit()
                    messagebox.showinfo("Success", f"Flight {flight_id} has been deleted successfully.")
                    tree.delete(selected_item)
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {e}")

    def edit_flight(self,tree):
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a flight to edit.")
            return

        flight_data = tree.item(selected_item)["values"]
        self.clear_content()

        self.content_frame.grid_columnconfigure(0, weight=5)
        self.content_frame.grid_columnconfigure(1, weight=8)
        self.content_frame.grid_columnconfigure(2, weight=1) 
        self.content_frame.grid_columnconfigure(3, weight=1)
        self.content_frame.grid_columnconfigure(4, weight=1) 
        self.content_frame.grid_columnconfigure(5, weight=1)
        self.content_frame.grid_columnconfigure(6, weight=1) 
        self.content_frame.grid_columnconfigure(7, weight=8)
        
        
        tk.Label(self.content_frame, text=f"Edit Flight {flight_data[0]}", font=("Arial", 18)).grid(row=0, column=0, columnspan=8, pady=10)
        
        
        instructions = [
            "Departure Airport Code:",
            "Local Departure Date/Time:",
            "Arrival Airport Code:",
            "Local Arrival Date/Time:",
            "Aircraft ID:",
            "Pilot ID:"
        ]

        entries = {}
        
        for i, instruction in enumerate(instructions):
            label = tk.Label(self.content_frame, text=instruction)
            label.grid(row=i+1, column=1, padx=10, pady=5, sticky="e")

            if "Aircraft ID:" in instruction:
                c.execute("SELECT AircraftID FROM Aircraft")
                aircraft_ids = [row[0] for row in c.fetchall()]

                edit_aircraft_id = tk.StringVar(self.content_frame)
                entry = ttk.Combobox(self.content_frame, textvariable=edit_aircraft_id, state="readonly")
                entry['values'] = aircraft_ids
                edit_aircraft_id.set(flight_data[12])
                entry.grid(row=i+1, column=2, columnspan=5, padx=10, pady=5, sticky="w")

            elif "Pilot ID:" in instruction:
                c.execute("SELECT PilotID FROM Pilot")
                pilot_ids = [row[0] for row in c.fetchall()]

                edit_pilot_id = tk.StringVar(self.content_frame)
                entry = ttk.Combobox(self.content_frame, textvariable=edit_pilot_id, state="readonly")
                entry['values'] = pilot_ids
                edit_pilot_id .set(flight_data[13])
                entry.grid(row=i+1, column=2, columnspan=5, padx=10, pady=5, sticky="w")
            
            elif "Airport Code" in instruction:
                c.execute("SELECT AirportCode FROM Airport")
                airport_ids = [row[0] for row in c.fetchall()]

                edit_airport_id = tk.StringVar(self.content_frame)
                entry = ttk.Combobox(self.content_frame, textvariable=edit_airport_id, state="readonly")
                entry['values'] = airport_ids
                edit_airport_id.set(flight_data[3] if "Departure" in instruction else flight_data[8])
                entry.grid(row=i+1, column=2, columnspan=5, padx=10, pady=5, sticky="w")

            else:
                date_time_value = flight_data[4] if "Departure" in instruction else flight_data[9]
                year_ori, month_ori, day_ori = date_time_value.split()[0].split("-")
                hour_ori, minute_ori = date_time_value.split()[1].split(":")


                year_values = [str(y) for y in range(2010, 2051)]
                year_box = ttk.Combobox(self.content_frame, values=year_values, width=5, state="readonly")
                year_box.grid(row=i+1, column=2, padx=5, pady=5, sticky = "w")
                year_box.set(year_ori)

                month_values = [str(m).zfill(2) for m in range(1, 13)]
                month_box = ttk.Combobox(self.content_frame, values=month_values,width=3, state="readonly")
                month_box.grid(row=i+1, column=2, padx=5, pady=5, sticky = "e")
                month_box.set(month_ori) 


                day_values = [str(d).zfill(2) for d in range(1, 32)]
                day_box = ttk.Combobox(self.content_frame, values=day_values,width=3, state="readonly")
                day_box.grid(row=i+1, column=3, padx=5, pady=5, sticky = "w")
                day_box.set(day_ori)

                hour_values = [str(h).zfill(2) for h in range(0, 24)]
                hour_box = ttk.Combobox(self.content_frame, values=hour_values,width=3, state="readonly")
                hour_box.grid(row=i+1, column=3, padx=5, pady=5, sticky = "e")
                hour_box.set(hour_ori) 

                minute_values = [str(m).zfill(2) for m in range(0, 60)]
                minute_box = ttk.Combobox(self.content_frame, values=minute_values,width=3, state="readonly")
                minute_box.grid(row=i+1, column=4, padx=5, pady=5, sticky = "w")
                minute_box.set(minute_ori)

                entry = (year_box, month_box, day_box, hour_box, minute_box)
      
            entries[instruction] = entry

        def get_user_edit():
            user_inputs = {}
            for instruction, entry in entries.items(): 
                if isinstance(entry, tuple): 
                    datetime_value = f"{entry[0].get()}-{entry[1].get().zfill(2)}-{entry[2].get().zfill(2)} {entry[3].get().zfill(2)}:{entry[4].get().zfill(2)}"
                    user_inputs[instruction] = datetime_value
                else:
                    user_inputs[instruction] = entry.get()
            return user_inputs

        def submit_edits():
            user_inputs = get_user_edit()
            departure_airport_code_value = user_inputs["Departure Airport Code:"]
            departure_date_time_local_value = user_inputs["Local Departure Date/Time:"]
            arrival_airport_code_value = user_inputs["Arrival Airport Code:"]
            arrival_date_time_local_value = user_inputs["Local Arrival Date/Time:"]
            select_aircraft_id_value = user_inputs["Aircraft ID:"]
            select_pilot_id_value = user_inputs["Pilot ID:"]

            if not all([departure_airport_code_value, departure_date_time_local_value, 
                arrival_airport_code_value, arrival_date_time_local_value, 
                select_aircraft_id_value, select_pilot_id_value]):
                messagebox.showwarning("Incomplete Data", "Please fill out all fields.")
                return
        
            try:
                c.execute("""
                    UPDATE Flight SET 
                    DepartureAirportCode = ?, 
                    DepartureDateTime_Local = ?, 
                    ArrivalAirportCode = ?, 
                    ArrivalDateTime_Local = ?, 
                    AircraftID = ?, 
                    PilotID = ?
                    WHERE FlightID = ?
                    """, (
                        get_user_edit["Departure Airport Code:"],
                        get_user_edit["Local Departure Date/Time:"],
                        get_user_edit["Arrival Airport Code:"],
                        get_user_edit["Local Arrival Date/Time:"],
                        get_user_edit["Aircraft ID:"],
                        get_user_edit["Pilot ID:"],
                        get_user_edit["Flight ID:"]
                    ))
                conn.commit()
                messagebox.showinfo("Success", f"Flight {flight_data[0]} has been updated successfully.")
                self.browse_flight() 
            except Exception as e:
                conn.rollback() 
                messagebox.showerror("Error", f"An error occurred: {e}")
   
        submit_button = tk.Button(self.content_frame, text="Save", command=submit_edits)
        submit_button.grid(row=len(instructions)+1, column=0, columnspan=8, pady=10)

        back_button = tk.Button(self.content_frame, text="Back", command=self.browse_flight)
        back_button.grid(row=len(instructions)+2, column=0, columnspan=8, pady=10)



         
    def new_flight(self):

        self.clear_content()
        self.content_frame.grid_columnconfigure(0, weight=5)
        self.content_frame.grid_columnconfigure(1, weight=8)
        self.content_frame.grid_columnconfigure(2, weight=1) 
        self.content_frame.grid_columnconfigure(3, weight=1)
        self.content_frame.grid_columnconfigure(4, weight=1) 
        self.content_frame.grid_columnconfigure(5, weight=1)
        self.content_frame.grid_columnconfigure(6, weight=1) 
        self.content_frame.grid_columnconfigure(7, weight=8) 
        tk.Label(self.content_frame, text="Add New Flight", font=("Arial", 18)).grid(row=0, column=0, columnspan=8, pady=10)
        

        instructions = [
            "Flight ID:",
            "Departure Airport Code:",
            "Local Departure Date/Time:",
            "Arrival Airport Code:",
            "Local Arrival Date/Time:",
            "Aircraft ID:",
            "Pilot ID:"]
    
        entries = {}

        for i, instruction in enumerate(instructions):
            label = tk.Label(self.content_frame, text=instruction)
            label.grid(row=i+1, column=1, padx=10, pady=5, sticky="e")

            if "Aircraft ID:" in instruction:
                c.execute("SELECT AircraftID FROM Aircraft")
                aircraft_ids = [row[0] for row in c.fetchall()]

                select_aircraft_id = tk.StringVar(self.content_frame)
                entry = ttk.Combobox(self.content_frame, textvariable=select_aircraft_id, state="readonly")
                entry['values'] = aircraft_ids
                entry.grid(row=i+1, column=2, columnspan=5, padx=10, pady=5, sticky="w")

            elif "Pilot ID:" in instruction:
                c.execute("SELECT PilotID FROM Pilot")
                pilot_ids = [row[0] for row in c.fetchall()]

                select_pilot_id = tk.StringVar(self.content_frame)
                entry = ttk.Combobox(self.content_frame, textvariable=select_pilot_id, state="readonly")
                entry['values'] = pilot_ids
                entry.grid(row=i+1, column=2, columnspan=5, padx=10, pady=5, sticky="w")
            
            elif "Airport Code" in instruction:
                c.execute("SELECT AirportCode FROM Airport")
                airport_ids = [row[0] for row in c.fetchall()]

                select_airport_id = tk.StringVar(self.content_frame)
                entry = ttk.Combobox(self.content_frame, textvariable=select_airport_id, state="readonly")
                entry['values'] = airport_ids
                entry.grid(row=i+1, column=2, columnspan=5, padx=10, pady=5, sticky="w")
                

            elif "Date/Time" in instruction:
                year_values = [str(y) for y in range(2010, 2051)]
                year_box = ttk.Combobox(self.content_frame, values=year_values, width=5, state="readonly")
                year_box.grid(row=i+1, column=2, padx=5, pady=5, sticky = "w")
                year_box.set("2023")

                month_values = [str(m).zfill(2) for m in range(1, 13)]
                month_box = ttk.Combobox(self.content_frame, values=month_values,width=3, state="readonly")
                month_box.grid(row=i+1, column=2, padx=5, pady=5, sticky = "e")
                month_box.set("11") 


                day_values = [str(d).zfill(2) for d in range(1, 32)]
                day_box = ttk.Combobox(self.content_frame, values=day_values,width=3, state="readonly")
                day_box.grid(row=i+1, column=3, padx=5, pady=5, sticky = "w")
                day_box.set("03")

                hour_values = [str(h).zfill(2) for h in range(0, 24)]
                hour_box = ttk.Combobox(self.content_frame, values=hour_values,width=3, state="readonly")
                hour_box.grid(row=i+1, column=3, padx=5, pady=5, sticky = "e")
                hour_box.set("12") 

                minute_values = [str(m).zfill(2) for m in range(0, 60)]
                minute_box = ttk.Combobox(self.content_frame, values=minute_values,width=3, state="readonly")
                minute_box.grid(row=i+1, column=4, padx=5, pady=5, sticky = "w")
                minute_box.set("30")

                entry = (year_box, month_box, day_box, hour_box, minute_box)
            
        
            else:
                entry = tk.Entry(self.content_frame)
                entry.grid(row=i+1, column=2, columnspan=5, padx=10, pady=5, sticky="w")

      
            entries[instruction] = entry

        def get_user_input():
            user_inputs = {}
            for instruction, entry in entries.items(): 
                if isinstance(entry, tuple): 
                    datetime_value = f"{entry[0].get()}-{entry[1].get().zfill(2)}-{entry[2].get().zfill(2)} {entry[3].get().zfill(2)}:{entry[4].get().zfill(2)}"
                    user_inputs[instruction] = datetime_value
                else:
                    user_inputs[instruction] = entry.get()
            return user_inputs

        def submit_flight():
            user_inputs = get_user_input()
            flight_id_value = user_inputs["Flight ID:"]
            departure_airport_code_value = user_inputs["Departure Airport Code:"]
            departure_date_time_local_value = user_inputs["Local Departure Date/Time:"]
            arrival_airport_code_value = user_inputs["Arrival Airport Code:"]
            arrival_date_time_local_value = user_inputs["Local Arrival Date/Time:"]
            aircraft_id_value = user_inputs["Aircraft ID:"]
            pilot_id_value = user_inputs["Pilot ID:"]

            if not all([flight_id_value, departure_airport_code_value, departure_date_time_local_value, 
                arrival_airport_code_value, arrival_date_time_local_value, 
                aircraft_id_value, pilot_id_value]):
                messagebox.showwarning("Incomplete Data", "Please fill out all fields.")
                return
        
            try:
                c.execute("""
                    INSERT INTO Flight (FlightID, DepartureAirportCode, DepartureDateTime_Local, ArrivalAirportCode, ArrivalDateTime_Local, AircraftID, PilotID)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (flight_id_value, departure_airport_code_value, departure_date_time_local_value, arrival_airport_code_value, 
                    arrival_date_time_local_value, aircraft_id_value,pilot_id_value))
                conn.commit()
                messagebox.showinfo("Success", "Flight added successfully!")
            except Exception as e:
                conn.rollback() 
                messagebox.showerror("Error", f"An error occurred: {e}")
      
        submit_button = tk.Button(self.content_frame, text="Confirm", command=submit_flight)
        submit_button.grid(row=len(instructions) + 1, column=0, columnspan=8, pady=10)

        back_button = tk.Button(self.content_frame, text="Back", command=self.main_page)
        back_button.grid(row=len(instructions) + 2, column=0, columnspan=8, pady=10)

    def search_flight(self):

        self.clear_content()
        tk.Label(self.content_frame, text="Search Flight", font=("Arial", 18)).pack(pady=10)

        entity_label = tk.Label(self.content_frame, text="Label:")
        entity_label.pack()

        entity_var = tk.StringVar(self.content_frame)
        entities = ["Flight ID","Aircraft ID", "Pilot ID","Departure Country", "Departure City", "Departure Airport Code","Departure Local Date/Time", "Arrival Country", "Arrival City", "Arrival Airport Code", "Arrival Local Date/Time"]
        entity_dropdown = ttk.Combobox(self.content_frame, textvariable=entity_var, values=entities)
        entity_dropdown.pack()

        value_label = tk.Label(self.content_frame, text="Enter known information:")
        value_label.pack()

        value_entry = tk.Entry(self.content_frame)
        value_entry.pack()

        def submit_search():
            entity = entity_var.get()
            value = value_entry.get()
    
            c.execute(f'''
                SELECT * FROM Flight
                WHERE "{entity}" LIKE ?
            ''', ('%' + value + '%',))
      
            results = c.fetchall()

            self.clear_content()
            tk.Label(self.content_frame, text="Search Result", font=("Arial", 16)).pack(pady=10)
            
            headers = ["Flight ID", "Departure Country", "Departure City", "Departure Airport", "Departure Local Date/Time", "Departure Time Zone", "Arrival Country", "Arrival City", "Arrival Airport", "Arrival Local Date/Time", "Arrival Time Zone","Total Flight Time", "Aircraft ID", "Pilot ID"]

            tree = ttk.Treeview(self.content_frame)
            tree["columns"] = tuple(range(len(results[0])))  
            tree["show"] = "headings"

            for i, header in enumerate(headers):
                tree.heading(i, text=header)
                tree.column(i, width=50)  
          
            for result in results:
                tree.insert("", "end", values=result)

            tree.pack()

            back_button = tk.Button(self.content_frame, text="Back", command=self.search_flight)
            back_button.pack()

        submit_button = tk.Button(self.content_frame, text="Search", command=submit_search)
        submit_button.pack()
        back_button = tk.Button(self.content_frame, text="Back", command=self.main_page)
        back_button.pack()

    def browse_aircraft(self):

        self.clear_content()
        tk.Label(self.content_frame, text="Current Aircrafts", font=("Arial", 18)).pack(pady=10)

        c.execute("SELECT * FROM Aircraft")
        aircraft_data = c.fetchall()
        aircraft_headers = ["Aircraft ID", "Model", "Capacity", "Manufacture Date", "Last Maintainence Date"]
        column_widths = [85, 65, 75, 135, 135]

        tree = ttk.Treeview(self.content_frame, columns=tuple(range(len(aircraft_data[0]))), show="headings", height=30)
        for i, header in enumerate(aircraft_headers):
            tree.heading(i, text=header)
            tree.column(i, width=column_widths[i])
        for row in aircraft_data:
            tree.insert("", "end", values=row)
        tree.pack()


        button_width=10
        #search_button = tk.Button(self.content_frame, text ="Search", command = self.search_flight, width=button_width)
        #search_button.pack(pady=5)
        #edit_button= tk.Button(self.content_frame, text="Edit", command=self.main_page, width=button_width)
        #edit_button.pack(pady=5)
        new_button= tk.Button(self.content_frame, text="New Aircraft", command=self.new_aircraft, width=button_width)
        new_button.pack(pady=5)
        back_button= tk.Button(self.content_frame, text="Back", command=self.main_page, width=button_width)
        back_button.pack(pady=5)
        
    def new_aircraft(self):

        self.clear_content()
        self.content_frame.grid_columnconfigure(0, weight=5)
        self.content_frame.grid_columnconfigure(1, weight=8)
        self.content_frame.grid_columnconfigure(2, weight=1) 
        self.content_frame.grid_columnconfigure(3, weight=1)
        self.content_frame.grid_columnconfigure(4, weight=1) 
        self.content_frame.grid_columnconfigure(5, weight=1)
        self.content_frame.grid_columnconfigure(6, weight=1) 
        self.content_frame.grid_columnconfigure(7, weight=8) 
        tk.Label(self.content_frame, text="Add New Aircraft", font=("Arial", 18)).grid(row=0, column=0, columnspan=8, pady=10)
        

        instructions = [
            "Aircraft ID:",
            "Aircraft Model:",
            "Capacity:",
            "Manufacture Date:",
            "Last Maintainence Date:"
            ]
    
        entries = {}

        for i, instruction in enumerate(instructions):
            label = tk.Label(self.content_frame, text=instruction)
            label.grid(row=i+1, column=1, padx=10, pady=5, sticky="e")

            if "Date" in instruction:
                year_values = [str(y) for y in range(2000, 2024)]
                year_box = ttk.Combobox(self.content_frame, values=year_values, width=5, state="readonly")
                year_box.grid(row=i+1, column=2, padx=5, pady=5, sticky = "w")
                year_box.set("2023")

                month_values = [str(m).zfill(2) for m in range(1, 13)]
                month_box = ttk.Combobox(self.content_frame, values=month_values,width=3, state="readonly")
                month_box.grid(row=i+1, column=2, padx=5, pady=5, sticky = "e")
                month_box.set("11") 

                day_values = [str(d).zfill(2) for d in range(1, 32)]
                day_box = ttk.Combobox(self.content_frame, values=day_values,width=3, state="readonly")
                day_box.grid(row=i+1, column=3, padx=5, pady=5, sticky = "w")
                day_box.set("03")

                entry = (year_box, month_box, day_box)
        
            else:
                entry = tk.Entry(self.content_frame)
                entry.grid(row=i+1, column=2, columnspan=5, padx=10, pady=5, sticky="w")
      
            entries[instruction] = entry

        def get_user_input():
            user_inputs = {}
            for instruction, entry in entries.items(): 
                if isinstance(entry, tuple): 
                    date_value = f"{entry[0].get()}-{entry[1].get().zfill(2)}-{entry[2].get().zfill(2)}"
                    user_inputs[instruction] = date_value
                else:
                    user_inputs[instruction] = entry.get()
            return user_inputs

        def submit_aircraft():
            user_inputs = get_user_input()
            aircraft_id_value = user_inputs["Aircraft ID:"]
            aircraft_model_value = user_inputs["Aircraft Model:"]
            capacity_value = user_inputs["Capacity:"]
            manufacture_date_value = user_inputs["Manufacture Date:"]
            last_maintainence_date_value = user_inputs["Last Maintainence Date:"]

            if not all([aircraft_id_value, aircraft_model_value, capacity_value, manufacture_date_value, last_maintainence_date_value]):
                messagebox.showwarning("Incomplete Data", "Please fill out all fields.")
                return
        
            try:
                c.execute("""
                    INSERT INTO Aircraft (AircraftID,  AircraftModel, Capacity, ManufactureDate, LastMaintainenceDate)
                    VALUES (?, ?, ?, ?, ?)
                """, (aircraft_id_value, aircraft_model_value, capacity_value, manufacture_date_value, 
                     last_maintainence_date_value))
                conn.commit()
                messagebox.showinfo("Success", "Aircraft added successfully!")
            except Exception as e:
                conn.rollback() 
                messagebox.showerror("Error", f"An error occurred: {e}")
                
      
        submit_button = tk.Button(self.content_frame, text="Confirm", command=submit_aircraft)
        submit_button.grid(row=len(instructions) + 1, column=0, columnspan=8, pady=10)

        back_button = tk.Button(self.content_frame, text="Back", command=self.main_page)
        back_button.grid(row=len(instructions) + 2, column=0, columnspan=8, pady=10)
    
    def browse_pilot(self):

        self.clear_content()
        tk.Label(self.content_frame, text="Current Pilots", font=("Arial", 18)).pack(pady=10)

        c.execute("SELECT * FROM Pilot")
        pilot_data = c.fetchall()
        pilot_headers = ["Pilot ID", "License ID", "Name", "Nationality", "Gender", "Date of Birth", "Onboard Date"]
        column_widths = [95, 95, 155, 125, 55, 125, 125]

        tree = ttk.Treeview(self.content_frame, columns=tuple(range(len(pilot_data[0]))), show="headings", height=30)
        for i, header in enumerate(pilot_headers):
            tree.heading(i, text=header)
            tree.column(i, width=column_widths[i])
        for row in pilot_data:
            tree.insert("", "end", values=row)
        tree.pack()

        button_width=10
        #search_button = tk.Button(self.content_frame, text ="Search", command = self.search_flight, width=button_width)
        #search_button.pack(pady=5)
        #edit_button= tk.Button(self.content_frame, text="Edit", command=self.main_page, width=button_width)
        #edit_button.pack(pady=5)
        new_button= tk.Button(self.content_frame, text="New Pilot", command=self.new_pilot, width=button_width)
        new_button.pack(pady=5)
        back_button= tk.Button(self.content_frame, text="Back", command=self.main_page, width=button_width)
        back_button.pack(pady=5)
   
    def new_pilot(self):

        self.clear_content()
        self.content_frame.grid_columnconfigure(0, weight=5)
        self.content_frame.grid_columnconfigure(1, weight=8)
        self.content_frame.grid_columnconfigure(2, weight=1) 
        self.content_frame.grid_columnconfigure(3, weight=1)
        self.content_frame.grid_columnconfigure(4, weight=1) 
        self.content_frame.grid_columnconfigure(5, weight=1)
        self.content_frame.grid_columnconfigure(6, weight=1) 
        self.content_frame.grid_columnconfigure(7, weight=8) 
        tk.Label(self.content_frame, text="Add New Pilot", font=("Arial", 18)).grid(row=0, column=0, columnspan=8, pady=10)
        

        instructions = [
            "Pilot ID:",
            "License ID:",
            "Name:",
            "Nationality:",
            "Gender:",
            "Date of Birth:",
            "Onboard Date:"]

        entries = {}

        for i, instruction in enumerate(instructions):
            label = tk.Label(self.content_frame, text=instruction)
            label.grid(row=i+1, column=1, padx=10, pady=5, sticky="e")

            if "Gender:" in instruction:
                select_gender = tk.StringVar(self.content_frame)
                genders = ["F", "M", "NB"]
                entry = ttk.Combobox(self.content_frame, textvariable=select_gender, values=genders, state="readonly")
                entry.grid(row=i+1, column=2, columnspan=5, padx=10, pady=5, sticky="w")

            elif "Date" in instruction:
                year_values = [str(y) for y in range(1950, 2030)]
                year_box = ttk.Combobox(self.content_frame, values=year_values, width=5, state="readonly")
                year_box.grid(row=i+1, column=2, padx=5, pady=5, sticky = "w")
                year_box.set("1990")

                month_values = [str(m).zfill(2) for m in range(1, 13)]
                month_box = ttk.Combobox(self.content_frame, values=month_values,width=3, state="readonly")
                month_box.grid(row=i+1, column=2, padx=5, pady=5, sticky = "e")
                month_box.set("11") 

                day_values = [str(d).zfill(2) for d in range(1, 32)]
                day_box = ttk.Combobox(self.content_frame, values=day_values,width=3, state="readonly")
                day_box.grid(row=i+1, column=3, padx=5, pady=5, sticky = "w")
                day_box.set("03")

                entry = (year_box, month_box, day_box)

            else:
                entry = tk.Entry(self.content_frame)
                entry.grid(row=i+1, column=2, columnspan=5, padx=10, pady=5, sticky="w")

            entries[instruction] = entry

        def get_user_input():
            user_inputs = {}
            for instruction, entry in entries.items(): 
                if isinstance(entry, tuple): 
                    date_value = f"{entry[0].get()}-{entry[1].get().zfill(2)}-{entry[2].get().zfill(2)}"
                    user_inputs[instruction] = date_value
                else:
                    user_inputs[instruction] = entry.get()
            return user_inputs


        def submit_pilot():
            user_inputs = get_user_input()
            pilot_id_value = user_inputs["Pilot ID:"]
            license_id_value = user_inputs["License ID:"]
            name_value = user_inputs["Name:"]
            nationality_value = user_inputs["Nationality:"]
            gender_value = user_inputs["Gender:"]
            birth_value = user_inputs["Date of Birth:"]
            onboard_value = user_inputs["Onboard Date:"]

            if not all([pilot_id_value, license_id_value, name_value, nationality_value, gender_value, birth_value, onboard_value]):
                messagebox.showwarning("Incomplete Data", "Please fill out all fields.")
                return

            try:
                c.execute("""
                    INSERT INTO Pilot (PilotID, LicenseID, Name, Nationality,  Gender, DateofBirth, OnboardDate)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (pilot_id_value, license_id_value, name_value, nationality_value, 
                    gender_value, birth_value, onboard_value))
                conn.commit()
                messagebox.showinfo("Success", "Pilot added successfully!")
            except Exception as e:
                conn.rollback() 
                messagebox.showerror("Error", f"An error occurred: {e}")
      
        submit_button = tk.Button(self.content_frame, text="Confirm", command=submit_pilot)
        submit_button.grid(row=len(instructions) + 1, column=0, columnspan=8, pady=10)

        back_button = tk.Button(self.content_frame, text="Back", command=self.main_page)
        back_button.grid(row=len(instructions) + 2, column=0, columnspan=8, pady=10)

    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
