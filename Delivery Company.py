class Delivery_system:
    def __init__(self):
        self.drivers = {}
        self.cities = {}
        self.drivers_id_counter = 1  
        self.city_connections = {
            "Beirut": ["Jbeil", "Zahle", "Sidon"],
            "Jbeil": ["Beirut"],
            "Zahle": ["Beirut"],
            "Sidon": ["Beirut", "Tripoli"],
            "Tripoli": ["Sidon"],
        }
    
    def main_menu(self):
        while True:
            print("Hello! Please enter:")
            print("1. To go to the drivers menu")
            print("2. To go to the cities menu")
            print("3. To exit the system")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.drivers_menu()
            elif choice == 2:
                self.cities_menu()
            elif choice == 3:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
    
    def drivers_menu(self):
        while True:
            print("Enter:")
            print("1. To view all the drivers")
            print("2. To add a driver")
            print("3. Check similar drivers")
            print("4. To go back to the main menu")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.view_drivers()
            elif choice == 2:
                self.add_drivers()
            elif choice == 3:
                self.checkSimilarDrivers()
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please try again.")
                
    def generateID(self):
        driver_id = f"ID{self.drivers_id_counter:03}"
        self.drivers_id_counter += 1
        return driver_id
    
    def view_drivers(self):
        if not self.drivers:
            print("There are no drivers in the system.")
        else:
            for driver_id,(name,start_city) in self.drivers.items():
                print(f"{driver_id},{name},{start_city}")
                
    def add_drivers(self):
        name = input("Enter the driver's name: ")
        city = input("Enter the driver's start city: ")
        if city not in self.cities:
            choice = input("The city is not in the system. Do you want to add it? y/n")
            if choice.lower() == "y":
                self.cities[city] = []
                print(f"City {city} added to the system.")
            else:
                print("The city is not in the system.")
        driver_id = self.generateID()
        self.drivers[driver_id] = (name,city)
        print(f"Driver {name} is added with ID {driver_id}")
            
    def checkSimilarDrivers(self):
        city_drivers={}
        for driver_id,(name,startCity) in self.drivers.items():
            if startCity not in city_drivers:
                city_drivers[startCity] = []  # Initialize with an empty list if the city is not in the dictionary
            city_drivers[startCity].append(name)  # Append the driver's name to the city's list of drivers
        print("/n Similar drivers by city")
        for city,drivers in city_drivers.items():
            print(f"{city}: {','.join(drivers)}")
            
    def cities_menu(self):
        while True:
            print("Hello! Please enter:")
            print("1. Show cities")
            print("2. Search city")
            print("3. Print neighboring cities ")
            print("4. Print Drivers delivering to city ")
            print("5. To go back to the main menu")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.show_cities()
            elif choice == 2:
                self.search_city()
            elif choice == 3:
                self.print_neighboring_cities()
            elif choice == 4:
                self.print_drivers()
            elif choice == 5:
                break
            else:
                print("Invalid choice. Please try again.")
            
    def show_cities(self):
        if not self.cities:
            print("No cities in the system.")
        else:
            sort_cities = sorted(self.cities.keys(), reverse=True)
        for city in sort_cities:
            print(city)
    
    def search_city(self):
        key = input("Enter a search key: ").lower()
        for city in self.cities.keys():
            if key in city.lower():
                print(f"City found: {city}")
            else:
                print("City not found")
                
    def print_neighboring_cities(self):
        target_city = input("Enter a city: ").lower()  
        found = False  
        for city, neighbors in self.city_connections.items():
            if city.lower() == target_city:  
                print(f"Neighboring cities of {city}: {', '.join(neighbors)}")
                found = True  
                break  
        if not found:
            print("City not found.")  
            
   

res = Delivery_system()
res.main_menu()
                
        
                
    
                
    