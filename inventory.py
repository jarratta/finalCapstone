"""
Author: Alistair Jarratt
Student ID: AJ22110004854
Task: T32
Capstone project to create a shoe stock management program
"""
# Import the moduels required to run the program

import math
from tabulate import tabulate

#========The beginning of the class==========
class Shoe:

# Create the definition of the Shoe class
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    def get_code(self):
        return self.code
    
    def get_product(self):
        return self.product

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

# Create a method to print an instance of a class
    def __str__(self):
        output = f'-----------Shoe data--------------\n'
        output += f'Country: {self.country}\n'
        output += f'Code: {self.code}\n'
        output += f'Product: {self.product}\n'
        output += f'Cost: GBP{self.cost}\n'
        output += f'Quantity: {self.quantity} pairs of shoes\n'
        output += f'---------------------------------'
        return output

#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============

# Function to read the inventory text file and create instances of the shoe class
def read_shoes_data():
    
    shoe_data_list =[]        

# Read the inventory.txt file to create the class instances
    while True:
        try:
            with open ('inventory.txt','r',encoding="utf-8") as shoe_data_file:
                shoe_data = shoe_data_file.readlines()[1:]                                    

            for row in shoe_data:
                items = row.split(",")
                shoe_data_list.append(items)
                country = items[0].strip()
                code = items[1].strip()
                product = items[2].strip()
                cost = items[3].strip()
                quantity = items[4].strip()
                
                shoe = Shoe(country,code, product, cost, quantity)
                
                shoe_list.append(shoe)
            print(
                    f'The inventory.txt has been successfully read. There are {len(shoe_data)} items loaded.'
                )            
            break
# Exception if the inventory text file does not exist
        except FileNotFoundError: 
            print ("The file does not exist.")
            break

    '''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
# Function to manually enter shoe data
def capture_shoes():
    shoe_code = ""
    shoe_cost = ""
    shoe_quantity = ""
    shoe_product=""

# Loop to enter the data and validate the inputs
    while True:
        shoe_country = input("Enter the shoe country of origin: ").title()
        shoe_name = input("Enter the shoe product name: ").title()
        
        while True:
            try:
                shoe_code = int(input("Enter the numeric shoe product code: SKU"))
                shoe_product = f'SKU{shoe_code}'
                break
            except ValueError:
                print("Enter a numberic product code")
        
        while True:        
            try:
                shoe_cost = int(input("Enter the cost of the shoe: GBP"))
                break
            except ValueError:
                print("Enter a numeric cost")         

        while True:
            try:
                shoe_quantity = int(input("Enter the quantity of pairs in stock: "))
                break
            except ValueError:
                print("Enter a numeric quantity")

# Print entered data to ensure it is correct.  Loop to manage exceptions if the entered data isn't correct
        print (
        f'New shoe details are:\n',
        'Country: ',(shoe_country),'\n',
        'Shoe Name: ',(shoe_name),'\n', 
        'Shoe Code: ',(shoe_product),'\n', 
        'Shoe Cost: ', (str(shoe_cost)),'\n',                  
        'Shoe Quantity: ',(shoe_quantity),'\n'
            )
        correct = str(input(f'Do you want to submit (Y,N or Q to return to main menu)?: ')).upper()

        if correct =="Y":
            shoe = Shoe(shoe_country, shoe_product, shoe_name, str(shoe_cost), str(shoe_quantity))
            shoe_list.append(shoe)

            new_shoe_list = ["\n" + shoe_country + ",", shoe_product + ",", shoe_name + ",", str(shoe_cost) + ",", str(shoe_quantity)]

            f = open("inventory.txt", "a", encoding="UTF-8")
            for i in new_shoe_list:
                f.write(i)
            f.close()

        elif correct == "N":
            capture_shoes()

        elif correct == "Q":
            menu()

        else:
            continue


    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''
#Function to view all the shoes in a list, then the detail of a chosen shoe
def view_all():
    # if len(shoe_list) == 0:
    #     read_shoes_data()

    for index, shoe in enumerate(shoe_list,1):
        print (f"{index}. {shoe.get_product()}")

    choice = int(input("Enter Product: ")) -1

    shoe = shoe_list[choice]
    print (shoe)
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function.
    '''
# Function to view the lowest stock items and add more quantities of them
def re_stock():
    # if len(shoe_list) == 0:
    #     read_shoes_data()
    
    min_stock = shoe_list[0]

    for shoe_stock in shoe_list:
        if int(shoe_stock.quantity) < int(min_stock.quantity):
            print (f'Index{shoe_stock.quantity} vs Min Stock{min_stock.quantity}')
            min_stock = shoe_stock

    print(f"\n========== LOW STOCK ============"
          f"\n{min_stock}")

    add_stock = input("\nEnter Y/N to update the shoes stock: ").lower()

# If stock is added, update the data to the inventory.txt file
    if add_stock == "y":
        update_stock = int(input("Please enter quantity for restocking: "))
        min_stock.quantity = int(min_stock.quantity) + update_stock

        with open('inventory.txt', 'w') as f:
            f.write('Country,Code,Product,Cost,Quantity\n')
        with open('inventory.txt', 'a') as f:
            for line in shoe_list:
                f.write(str(line.country) + ',' + str(line.code) + ',' + str(line.product) + ',' + str(line.cost) + ',' + str(line.quantity) + '\n')

    else:
        exit

    print(f"\n========= NEW STOCK QUANTITY =========="
              f"\n{min_stock}")

    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''

# Function to seach for a specific show and show the results
def seach_shoe():
    # if len(shoe_list) == 0:
    #     read_shoes_data()

    shoe_search = input("Enter product ID you want to search for: ")
    for shoe in shoe_list:
        if shoe.get_code() == shoe_search:
            print(shoe)
            return shoe
    return f'Enter a valid product ID'

'''
This function will search for a shoe from the list
using the shoe code and return this object so that it will be printed.
'''

# Function to calculate the total shoe value (qty x cost) and display the results in a table
def value_per_item():
    # if len(shoe_list) == 0:
    #     read_shoes_data()

    print_shoe_list =[]

    for shoe in shoe_list:
        
        stock_value = int(shoe.cost) * int(shoe.quantity)

        temp = [shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity, stock_value]

        print_shoe_list.append(temp)
    
    print(tabulate(print_shoe_list, headers = ["Country Code", "Product Code", "Product Name", "Product Cost", "Quantity", "Value"]))

    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''

# Function to find the show with the largest quanity in stock 
def highest_qty():
#     if len(shoe_list) == 0:
#         read_shoes_data()

    highest_stock = shoe_list[0]

    for shoe_qty in shoe_list:
        if int(shoe_qty.quantity) > int(highest_stock.quantity):
            highest_stock = shoe_qty

    print(f"\n========= STOCK ON SALE ==========="

          f"\n{highest_stock}")

    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============

# Function to create a menu of the functions
def menu():

    menu_select =""

    while menu_select != "q":
        #read_shoes_data()
        if     len(shoe_list) != 0:
            output = f'——————————————————[SELECT AN OPTION]—————————————————————\n'
            output += f'Section a function: \n'
            output += f'1: READ data from inventory.txt file \n'
            output += f'2: ADD a new shoe to the inventory list \n'
            output += f'3: VIEW the inventory list \n'
            output += f'4: RESTOCK the inventory list \n'
            output += f'5: SEARCH for a shoe on the inventory list \n'
            output += f'6: SHOW stock valuation for shoes on the inventory list \n'
            output += f'7: DISPLAY stock with the most quantity on hand \n'                
            output += f'q: QUIT the program \n'        
            output += f'—————————————————————————————————————————————————————————\n'
            print (output)
            #read_shoes_data
            menu_select = input("Select a function: ").lower()   
            if menu_select in ('1','2','3','4','5','6','7','q'):
                if menu_select == "1":
                    read_shoes_data()
                if menu_select == "2":
                    capture_shoes()
                elif menu_select == "3":
                    view_all()
                elif menu_select == "4":
                    re_stock ()
                elif menu_select == "5":
                    seach_shoe ()
                elif menu_select == "6":
                    value_per_item ()
                elif menu_select == "7":
                    highest_qty ()
                elif menu_select == "q":
                    print("Thank-you for using Inventory Manager")
                    quit()
        else:
            print ("Choose a valid function")
            output = f'——————————————————[SELECT AN OPTION]—————————————————————\n'
            output += f'Section a function: \n'
            output += f'ADD inventory.txt the:\n'                
            output += f'1: READ data from inventory.txt file  \n'
            output += f'Or:\n'  
            output += f'2: ADD a new shoe to the inventory list \n'  
            output += f'q: QUIT the program \n'        
            output += f'—————————————————————————————————————————————————————————\n'
            print (output)
            menu_select = input("Select a function: ").lower()   
            if menu_select in ('1','2','q'):
                if menu_select == "1":
                    read_shoes_data()
                elif menu_select == "2":
                    capture_shoes()
                elif menu_select == "q":
                    print("Thank-you for using Inventory Manager")
                    quit()
            else:
                print ("Choose a valid function")

menu()

'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''