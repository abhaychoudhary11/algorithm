import pandas as pd
import tkinter as tk
from tkinter import ttk, Canvas, Scrollbar

class Car:
    def __init__(self, company, model, variant, price, cc, fuel_type, mileage):
        self.company = company
        self.model = model
        self.variant = variant
        self.price = price
        self.cc = cc
        self.fuel_type = fuel_type
        self.mileage = mileage

class CarSearchSortSystem:
    def __init__(self, filename):
        self.cars = self.load_data(filename)

    def load_data(self, filename):
        try:
            df = pd.read_excel(filename)
            df.columns = df.columns.str.strip()  
            print(f"Data Loaded: {df.head()}")  
        except Exception as e:
            print(f"Error loading file: {e}")
            return []

        cars = []
        for _, row in df.iterrows():
            car = Car(
                row['Company'], row['Model'], row['Variant'],
                row['Price (INR)'], row['CC'], row['Fuel Type'], row['Mileage (km/l)']
            )
            cars.append(car)
        return cars

    def filter_cars(self, price_range=None, company=None, fuel_type=None):
        filtered = self.cars
        if price_range:
            filtered = [car for car in filtered if price_range[0] <= car.price <= price_range[1]]
        if company:     
            filtered = [car for car in filtered if car.company.lower() == company.lower()]
        if fuel_type:
            filtered = [car for car in filtered if car.fuel_type.lower() == fuel_type.lower()]
        return filtered

    # Merge Sort
    def merge(self, left, right, key):
        sorted_list = []
        i = j = 0
        while i < len(left) and j < len(right):
            if getattr(left[i], key) <= getattr(right[j], key):
                sorted_list.append(left[i])
                i += 1
            else:
                sorted_list.append(right[j])
                j += 1
        sorted_list.extend(left[i:])
        sorted_list.extend(right[j:])
        return sorted_list

    def mergesort(self, cars, key):
        if len(cars) <= 1:
            return cars
        mid = len(cars) // 2
        left = self.mergesort(cars[:mid], key)
        right = self.mergesort(cars[mid:], key)
        return self.merge(left, right, key)

class CarSearchGUI:
    def __init__(self, root, system):
        self.root = root
        self.system = system
        self.root.title("Car Search System")
        self.root.geometry("850x600")
        self.root.resizable(False,False)

        # Filters
        ttk.Label(root, text="Company:").grid(row=0, column=0, padx=5, pady=5)
        self.company_entry = ttk.Entry(root)
        self.company_entry.grid(row=0, column=1, padx=5, pady=5)

        ttk.Label(root, text="Fuel Type:").grid(row=0, column=2, padx=5, pady=5)
        self.fuel_entry = ttk.Entry(root)
        self.fuel_entry.grid(row=0, column=3, padx=5, pady=5)

        # Price Range (Fixed Min, Selectable Max)
        ttk.Label(root, text="Max Price Range:").grid(row=1, column=0, padx=5, pady=5)
        self.price_range_combo = ttk.Combobox(root, values=["500000", "1000000", "2000000", "3000000", "5000000", "10000000"])
        self.price_range_combo.grid(row=1, column=1, padx=5, pady=5)
        self.price_range_combo.current(0)  # Set default value


        # Sorting Option
        ttk.Label(root, text="Sort By:").grid(row=2, column=0, padx=5, pady=5)
        self.sort_by = ttk.Combobox(root, values=["price", "mileage", "cc"])
        self.sort_by.grid(row=2, column=1, padx=5, pady=5)
        self.sort_by.current(0)

        self.search_button = ttk.Button(root, text="Search", command=self.search_cars)
        self.search_button.grid(row=2, column=3, padx=5, pady=5)

        # Scrollable Frame for Tiles
        self.canvas = Canvas(root, height=400, width=800)
        self.scrollbar = Scrollbar(root, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.grid(row=3, column=0, columnspan=4, padx=5, pady=5)
        self.scrollbar.grid(row=3, column=4, sticky="ns")

    def search_cars(self):
        company = self.company_entry.get().strip() or None
        fuel_type = self.fuel_entry.get().strip() or None
    
    # Ensure max_price is properly retrieved
        try:
            max_price = int(self.price_range_combo.get().strip())  # Get selected max price
        except ValueError:
                max_price = None  # Handle case when nothing is selected

        price_range = (0, max_price) if max_price else None

    # Filtering
        filtered_cars = self.system.filter_cars(price_range=price_range, company=company, fuel_type=fuel_type)

    # Sorting
        sorted_cars = self.system.mergesort(filtered_cars, self.sort_by.get())

    # Clear old tiles
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        if not sorted_cars:  # Handle empty results
            frame = ttk.Frame(self.scrollable_frame, relief="ridge", borderwidth=2)
            frame.grid(row=0, column=0, padx=10, pady=10)
            label = ttk.Label(frame, text="No cars found matching criteria.", padding=5)
            label.pack()
            return

    # Display tiles for sorted cars
        for i, car in enumerate(sorted_cars):
            frame = ttk.Frame(self.scrollable_frame, relief="ridge", borderwidth=2)
            frame.grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky="nsew")

            label = ttk.Label(
                frame,
                text=f"{car.company} {car.model} ({car.variant})\n"
                    f"₹{car.price} - {car.fuel_type}\n"
                    f"CC: {car.cc} - Mileage: {car.mileage} km/l",
                padding=5
            )
            label.pack()



# Run the GUI
filename = r"C:\Users\abhis\OneDrive\Desktop\coding\algorithm\MULTI-COMPANY\car_data.xlsx"

system = CarSearchSortSystem(filename)
root = tk.Tk()
app = CarSearchGUI(root, system)
root.mainloop()