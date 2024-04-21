def login():#To differentiate admin or customer, only admin able to change the stock
    print("Welcome to the Auto Car Store!")
    while True:
        user_type = input("Are you an admin? (y/n): ").lower()
        if user_type == 'y':
            return True
        elif user_type == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def display_menu(admin=False):#To display menu
    print("\nAUTO CAR STORE MENU:")
    print("1. Display car list and stock")
    if not admin:
        print("2. Buy a car")
        print("3. Rent a car")
        print("4. Sell a car")
        print("5. Exit")
    else:
        print("2. Add car")
        print("3. Remove car")
        print("4. Back to login")
        print("5. Exit")

def display_car_list(car_store, car_rent):#To display lists of car 
    print("\nCARS AVAILABLE FOR SALE:")
    for car_id, car_details in car_store.items():
        print(f"ID: {car_id} | Name: {car_details['name'].capitalize()} | Type: {car_details['type']} | Price: ${car_details['price']} | Stock: {car_details['stock']}")
    
    print("\nCARS AVAILABLE FOR RENT:")
    for car_id, car_details in car_rent.items():
        print(f"ID: {car_id} | Name: {car_details['name'].capitalize()} | Type: {car_details['type']} | Price: ${car_details['price']} | Stock: {car_details['stock']}")
def add_car():#To Add Car
    while True:
        car_name = input("\nEnter the name of the car to add: ").lower()
        if any(car_name == car_details['name'].lower() for car_details in car_store.values()):#To check if the car is already in the store
            print(f"{car_name.capitalize()} is already in the store!")
        else:
            car_type = input(f"Enter the type of {car_name.capitalize()} (e.g., sedan, SUV, truck): ").capitalize()
            price = float(input(f"Enter the price of {car_name.capitalize()} ($): "))
            stock = int(input(f"Enter the stock of {car_name.capitalize()}: "))
            option = input(f"Is the {car_name.capitalize()} for sale or for rent? (sale/rent): ").lower()#The car can be added into sale or rent options 
            if option == 'sale':
                car_id = len(car_store) + 1  # Generate a new ID for the car
                car_store[car_id] = {'name': car_name, 'type': car_type, 'price': price, 'stock': stock}
                print(f"{car_name.capitalize()} for sale, {car_type}, and stock {stock} has been added to the store.")
            elif option == 'rent':
                car_id = len(car_rent) + 1  # Generate a new ID for the car
                car_rent[car_id] = {'name': car_name, 'type': car_type, 'price': price, 'stock': stock}
                print(f"{car_name.capitalize()} for rent, {car_type}, and stock {stock} has been added to the store.")
            else:
                print("Invalid option. Please enter 'sale' or 'rent'.")
        break


def remove_car():#To remove Car
    while True:
        print("\nCars from buy option:")
        for car_id, car_details in car_store.items():
            print(f"ID: {car_id} | Name: {car_details['name'].capitalize()} | Type: {car_details['type']} | Price: ${car_details['price']} | Stock: {car_details['stock']}")
        print("\nCars from rent option:")
        for car_id, car_details in car_rent.items():
            print(f"ID: {car_id} | Name: {car_details['name'].capitalize()} | Type: {car_details['type']} | Price: ${car_details['price']} | Stock: {car_details['stock']}")
        option = input("which option do you want to remove the car from?(buy/rent:)").lower()
        while True:#To create loop, if the car is not from buy or rent option, the loop will be repeated
            if option == 'buy' or option == 'rent':
                car_id = int(input("\nEnter the car ID that you want to remove: "))
                if car_id in car_store:
                    del car_store[car_id]
                    print(f"Car with ID {car_id} removed from the store.")
                else:
                    print(f"Car with ID {car_id} is not available in the store.")
            elif option == 'rent':
                if car_id in car_rent:
                    del car_rent[car_id]
                    print(f"Car with ID {car_id} remove from the store")
                else:
                    print(f"Car with ID {car_id} is not available in the store.")
            else:
                print ("Invalid option. Please enter 'buy' or 'rent'")
                break
            return



def buy_car():#To Buy Car
    while True:
        print("\n Car Lists")
        for car_id, car_details in car_store.items():
            print(f"ID: {car_id} | Name: {car_details['name'].capitalize()} | Type: {car_details['type']} | Price: ${car_details['price']} | Stock: {car_details['stock']}")
        car_id_input = input("\nEnter the ID of the car to buy: ")
        if car_id_input.isdigit():#To ensure the car ID that was inputted is in valid format
            car_id = int(car_id_input)
            if car_id in car_store:
                quantity = int(input(f"Enter the quantity of {car_store[car_id]['name'].capitalize()} to buy: "))
                if quantity <= car_store[car_id]['stock']:
                    total_price = quantity * car_store[car_id]['price']
                    print(f"Total price for {quantity} {car_store[car_id]['name']}(s): ${total_price}")
                    amount_paid = float(input("Enter the amount of money you have: $"))
                    if amount_paid >= total_price:#To ensure the customer has sufficient fund
                        change = amount_paid - total_price
                        print(f"Thank you for your purchase! Your change is ${change:.2f}.")
                        car_store[car_id]['stock'] -= quantity
                        while True:#To give the option to the customer to go back to the main menu or exit the store
                            choice = input("Do you wish to go back to the main menu? (y/n):").lower()
                            if choice =='y':
                                return
                            elif choice =='n':
                                print("Exiting the car store. Goodbye! :)")
                                exit()
                            else:
                                print("Please enter a valid response (y/n)")  
                    else:
                        print("Sorry, you have insufficient funds.")
                else:
                    print(f"Sorry, only {car_store[car_id]['stock']} {car_id}(s) available.")
            else:
                print(f"There is no car with ID number {car_id} that is available in the store.")
        else:
            print("Invalid response, please enter valid response")

def sell_car():#For the customer to sell car(s)
    while True:
        car_name = input("\nEnter the name of the car that you want to sale: ").lower()
        car_id = None  # Initialize car_id to None before the loop
        found_car = False
        for id, car_details in car_store.items():
            if car_name == car_details['name'].lower():  # Check if the car exists in the store. If the car exists, it should be sold according to the store price
                found_car = True
                car_id = id  # Assign the ID of the matching car
                print(f"{car_name.capitalize()} is already in the store. Car can be sell with the price that already been set according to the car lists")
                confirm_sell = input("Do you wish to add stock for this car? (y/n): ").lower()
                if confirm_sell == 'y':
                    additional_stock = int(input(f"How many more {car_name.capitalize()} do you want to sell? "))
                    car_store[car_id]['stock'] += additional_stock
                    total_price = additional_stock * car_store[car_id]['price']
                    print(f"You just sold {additional_stock} {car_name.capitalize()} for ${total_price}.")
                elif confirm_sell == 'n':
                    print("No changes made. Returning to the main menu...")
                    return  # Return to the main menu
                else:
                    print("Invalid option. Please select 'y' or 'n'")
                break
        if not found_car:#If the car is not exists, the customer could sell according to their desired price
            car_type = input(f"Enter the type of {car_name.capitalize()} (e.g., sedan, SUV, truck): ").capitalize()
            price = float(input(f"Enter the price of {car_name.capitalize()} ($): "))
            stock = int(input(f"Enter the stock of {car_name.capitalize()}: "))
            car_id = len(car_store) + 1
            car_store[car_id] = {'name': car_name.capitalize(), 'type': car_type, 'price': price, 'stock': stock}
            print(f"{car_name.capitalize()} has been added to the store.")
        return  # Return to the main menu


def rent_car():
    while True:
        print("\nCAR LIST:")
        for car_id, car_details in car_rent.items():
            print(f"ID: {car_id} | Name: {car_details['name'].capitalize()} | Type: {car_details['type']} | Price: ${car_details['price']} | Stock: {car_details['stock']}")
        car_id = (input("\nEnter the ID of the car to rent: "))
        if car_id.isdigit():#To ensure the correct format inputted for the car ID
            car_id = int(car_id)
            quantity = int(input(f"Enter the quantity of {car_rent[car_id]['name'].capitalize()} to rent: "))
            if car_id in car_rent:
                days = int(input("Enter the number of days to rent the car: "))
                if quantity <= car_rent[car_id]['stock']:#To ensure the quantity does not exceed the existing stocks
                    total_price = quantity * car_rent[car_id]['price'] * days
                    print(f"Total price for {quantity} {car_rent[car_id]['name']}(s): ${total_price}")
                    print(f"You rented {car_id} for {days} days for a total of ${total_price}.")
                    car_rent[car_id]['stock'] -= 1
                    while True:
                        choice = input("Do you wish to go back to the main menu? (y/n):").lower()
                        if choice =='y':
                            return
                        elif choice =='n':
                            print("Exiting the car store. Goodbye! :)")
                            exit()
                        else:
                            print("Please enter a valid response (y/n)")
                            break # Exit the loop after successful rental 
                else:
                    print(f"Sorry, only {car_rent[car_id]['stock']} {car_id}(s) available.")
            else:
                print("Car ID is not available in the inventory")
        else:
            print("Please input the valid Car ID.")
# Main program loop
if login():
    admin = True
    print("Admin login successful.")
else:
    admin = False
    print("User login successful.")

car_store = {
    1: {'name': 'Toyota Innova', 'type': 'sedan', 'price': 15000, 'stock': 10},
    2: {'name': 'Honda CRV', 'type': 'sedan', 'price': 17000, 'stock': 15},
    3: {'name': 'Toyota Fortuner', 'type': 'SUV', 'price': 30000, 'stock': 15},
    4: {'name': 'Land Cruiser Prado', 'type': 'truck', 'price': 35000, 'stock': 5},
    5: {'name': 'Honda Jazz', 'type': 'hatchback', 'price':900,'stock':25},
    6: {'name': 'Mitsubishi Pajero', 'type': 'SUV','price':2800,'stock':15}
}

car_rent = {
    1: {'name': 'Honda Brio', 'type': 'hatchback', 'price': 60, 'stock': 10},
    2: {'name': 'Honda Jazz', 'type':'hatchback','price':80,'stock':10},
    3: {'name': 'Honda Civic', 'type': 'sedan', 'price': 100, 'stock': 10},
    4: {'name': 'Toyota Innova', 'type': 'MPV', 'price': 500, 'stock': 5},
    5: {'name': 'Honda CRV', 'type': 'SUV', 'price': 500, 'stock': 5}
}

while True:
    display_menu(admin)
    choice = input("Enter your choice: ")
    if  admin:
        if choice == '1':
            display_car_list(car_store,car_rent)
        elif choice == '2':
            add_car()
        elif choice == '3':
            remove_car()
        elif choice == '4':
            admin=login()
        elif choice == '5':
            print("Exiting the car store. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
    else:
        if choice == '1':
            display_car_list(car_store,car_rent)
        elif choice == '2':
            buy_car()
        elif choice == '3':
            rent_car()
        elif choice == '4':
            sell_car()
        elif choice == '5':
            print("Exiting the car store. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")