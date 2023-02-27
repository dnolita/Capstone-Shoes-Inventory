# CAPSTONE IV - Inventory

# Importing from library

from tabulate import tabulate


# ========Beginning of the class==========

# Creating Shoe class and class methods to return or print values in
# required formats

class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_cost(self):
        print(f'Cost of shoe: {self.cost}')

    def get_quantity(self):
        print(f'Quantity of shoes: {self.quantity}')

    def create_table(self):
        return [self.country, self.code, self.product, self.cost, self.quantity]

    def update_file(self):
        return f'{self.country},{self.code},{self.product},{self.cost},{self.quantity}'

    def __str__(self):
        return (f'Country: {self.country}\n'
                f'Code: {self.code}\n'
                f'Product: {self.product}\n'
                f'Cost: {self.cost}\n'
                f'Quantity: {self.quantity}\n')


# =================Shoe list Objects================

# List to store a list of shoe objects from functions below.

shoe_list = []

# ============Functions outside the class============


# Method to skip first line of textfile looked up on stackoverflow.com

# Function to read data from inventory textfile and create each shoe object to store in the shoe_list

def read_shoes_data():
    with open('inventory.txt', 'r') as shoes:
        shoes_data = shoes.readlines()[1:]

        try:
            for line in shoes_data:
                shoe_obj = line.strip('\n').split(',')
                shoe_ob = Shoe(shoe_obj[0], shoe_obj[1], shoe_obj[2], float(shoe_obj[3]), int(shoe_obj[4]))
                shoe_list.append(shoe_ob)

        except IndexError:
            pass


# Function to allow a user to capture new shoe data, create a shoe object with it and append object to shoe_list
# after appending the data to the inventory textfile

def capture_shoes():
    capture1 = input('Enter the details of the shoe: \n' 
                     'Country: \n')
    capture2 = input('Code: \n')
    capture3 = input('Product: \n')
    capture4 = int(input('Cost: \n'))
    capture5 = int(input('Quantity: \n'))

    with open('inventory.txt', 'a') as file_a:
        new = f'\n{capture1},{capture2},{capture3},{capture4},{capture5}'
        file_a.write(new)

    shoe_obj = Shoe(capture1, capture2, capture3, capture4, capture5)
    shoe_list.append(shoe_obj)
    print(f'New shoe item added: \n\n{shoe_list[-1]}')

# Function to view all items in the shoe_list and display the details in a table using tabulate
# Looked up tabulate method on pypi.org and stackoverflow.com

def view_all():

    view_list = []
    headers = ['Country', 'Code', 'Product', 'Cost', 'Quantity']
    for product in shoe_list:
        view_list.append(product.create_table())

    print(f'\n{tabulate(view_list, headers)}\n')


# Function to write to the inventory textfile following re-stocking of shoe item

def file_write():
        with open('inventory.txt', 'w') as file_w:
            file_w.write('Country,Code,Product,Cost,Quantity')
            for item in shoe_list:
                file_w.write(f'\n{item.update_file()}')


# Function to find the shoe object with the lowest quantity and ask user if they would like to add to
# the quantity to re-stock the shoe and then update the quantity in the inventory textfile.
# Method to find 'min' item in list of objects looked up on stackoverflow.com

def re_stock():

    low_stock = -1
    for stock in range(1, len(shoe_list)):
        if shoe_list[stock].quantity < shoe_list[low_stock].quantity:
            low_stock = stock

    print(f'Shoe item with the least stock level is: \n\n'
          f'{shoe_list[low_stock]}')

    while True:
        try:

            choice = input('Would you like to add to this quantity of shoes? \n').lower()

            if choice == 'yes':
                restock = int(input('Enter the re-stock quantity: \n'))
                shoe_list[low_stock].quantity = restock
                updated_stock = shoe_list[low_stock]
                print(f'Shoe item with updated stock: \n\n{updated_stock}')
                file_write()
                break

            elif choice == 'no':
                break

            else:
                print('You have entered an invalid value. Try again')

        except TypeError and ValueError:
            print('You have entered an invalid value. Try again')


# Function for using the shoe code to search for a shoe in the shoe_list and print

def search_shoe():
    shoe_code = input('Enter the shoe code you would like to search: \n\n').upper()
    pos = -1

    for i, shoe in enumerate(shoe_list):
        if shoe.code == shoe_code:
            pos = i
            print(f'Shoe item found: \n\n{shoe}')

    if pos == -1:
        print(f'Code: {shoe_code} could not be found.\n')


# Function to calculate and print the total value of each shoe item in the shoe_list

def value_per_item():

    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        print(f'{shoe}\n'
              f'Shoe item value is: {value}\n')


# Function to determine the shoe item with the highest quantity and print it as being on sale

def highest_qty():

    hi_stock = -1
    for stock in range(1, len(shoe_list)):
        if shoe_list[stock].quantity > shoe_list[hi_stock].quantity:
            hi_stock = stock

    print(f'Shoe item with highest stock quantity and NOW ON SALE: \n\n'
          f'{shoe_list[hi_stock]}')


# ==========Main Menu=============

# Main function called below, to present main menu to user to call the applicable
# functions defined above

def main():
    while True:

        user_menu = input('''Shoe Inventory menu - choose an option:     
        c - capture new shoe data
        va - view all shoe items
        rs - re-stock shoe item
        s - search for shoe item
        v - get total value of each shoe item
        hq - get shoe item with highest quantity
        e - exit
        ''').lower()

        if user_menu == 'c':
            capture_shoes()

        elif user_menu == 'va':
            view_all()

        elif user_menu == 'rs':
            re_stock()

        elif user_menu == 's':
            search_shoe()

        elif user_menu == 'v':
            value_per_item()

        elif user_menu == 'hq':
            highest_qty()

        elif user_menu == 'e':
            print('Goodbye')
            exit()

        else:
            print('You have made an invalid selection. Try again')
            continue

read_shoes_data()
main()

