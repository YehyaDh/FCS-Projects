class Delivery_system(self):
    def __init__(self):
        self.drivers = {}
        self.cities = {}
        self.frivers_id = 1
        
    def main_menu(self):
        while True:
            print("Hello! Please enter:")
            print("1. To go to the drivers menu")
            print("2. To go to the cities menu")
            print("3. To exit the system")
            choice = input("Enter your choice: ")
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
            choice = input("Enter your choice: ")
            if choice == 1:
                self.view_drivers()
            elif choice == 2:
                self.add_drivers()
            elif choice == 3:
                self.check_similar_drivers()
            elif choice == 4:
                break
            else:
                print("Invalid choice. Please try again.")