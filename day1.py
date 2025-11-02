"""
#Temperature Converter

#convert from cels to fahren
def Celsius_Fahrenheit(c):
   return c * 9 / 5 + 32

# convert from fahren to cels 
def Fahrenheit_Celsius(f):
    return (f-32) * 5 / 9

#convert from cels to kelivn 
def Celsius_Kelvin(c):
    return c + 273.15

#convert from kelvin to cels 
def Kelvin_Celsius(k):
    return k - 273.15


# create menu to choose from :
while True:
    print("\nTemperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("0. Exit")
    
    ch = input("Enter your choice from [0-4]:").strip()
    
    if ch == '0':
        print("goodbye")
        break
    
    # validate choice in range 1 to 4
    if ch not in ['1', '2', '3', '4']:
        print("Invalid choice, please try again.")
        continue
    
    temp = float(input("Enter the value of temp:"))
    
    if ch == "1":
        res = Celsius_Fahrenheit(temp)
        print(f"{temp}°C = {res:.2f}°F")
        
    elif ch == '2':
        res = Fahrenheit_Celsius(temp)
        print(f"{temp}°F = {res:.2f}°C")
        
    elif ch == '3':
        res = Celsius_Kelvin(temp)
        print(f"{temp}°C = {res:.2f}K")
        
    elif ch == '4':
        res = Kelvin_Celsius(temp)
        print(f"{temp}K = {res:.2f}°C")
    """


"""
# List Manipulator        
numbers = input("Enter your numbers with space: ")
# using list comperhensive so we can convert them from character to inter numbers:
numbers = [int(x) for x in numbers.split()]
print(f"original list of number is: {numbers}")
# sum of numbers:
print("the sum of numbers :" , sum(numbers))
# average of numbers 
print("the avg of numbers :" ,sum(numbers) // len(numbers))
# max and min number 
print("max number and min number: ", max(numbers), min(numbers))
# remove duplicate:
print("list after remove duplicate: ", list(set(numbers)))
# sort asced and desced :
print(f"the  asc sorted array  without duplicate: ", sorted(set(numbers)))
print(f"the  des sorted array  without duplicate: ", sorted(set(numbers), reverse=True))

# filtering even and odd numbers using list comperhensive:
even_numbers = list(set([x for x in numbers if x % 2 == 0]))
print(even_numbers)
odd_numbers = list(set([x for x in numbers if x % 2 != 0]))
print(odd_numbers)"""

"""
#String Pattern Analyzer
from collections import Counter

text = input("Enter your string:").lower()
print("number of char includes spaces", len(text))
print("the number of char exclude spaces ", len(text.replace(" ", "")))
# character frequently count
freq = Counter(text.replace(" ", ""))
print(dict(freq))

#word count
word_count = text.split()
print(len(word_count))

# max freq character 
max_char = max(freq.values())
char_most_common = [ch for ch, count in freq.items() if count == max_char]
print(char_most_common)

# check plaindrom
is_plaindrom = text.replace(" ", "") == text.replace(" ", "")[::-1]
print(is_plaindrom)

#revere string
reversed_text = text[::-1]
print(reversed_text)"""

"""
# Number Guessing Game
import random 
while True:
    number = random.randint(1, 100)
    attempts = 7 
    tries = 0 
    while tries < attempts :
        user_guess = int(input("Enter your guessing number: "))
        tries+=1
        if user_guess == number:
            print(f"Congrats, you got that in {tries} attempts.")
            break
        elif user_guess < number:
            print("you are too low, try again")
        else:
            print("you are too high, try again.")
    else:
        print(f"Sorry, you've used all {attempts} attempts. The number was {number}.")
             
    play_again = input("Play again? (yes/no): ").lower()"""



"""
#Shopping Cart System
# creating functions for each choice 
#add items
def add_item(cart):
    name = input("Enter item name: ").capitalize()
    price = float(input("Enter item price: "))
    quantity = int(input("Enter quantity: "))

    if name in cart:
        cart[name]["quantity"] += quantity
    else:
        cart[name] = {"price": price, "quantity": quantity}

    print(f"{name} added successfully!")

#remove items
def remove_item(cart):
    name = input("Enter item name: ").capitalize()
    if name in cart:
        del cart[name]
        print(f"this {name} removed successfully")
    else:
        print(f"this {name} is not found in cart")

def update_quantity(cart):
    name = input("Enter item name: ")
    if name in cart:
        new_quantity = int(input("Enter new quantity: "))
        cart[name]["quantity"] = new_quantity
        print("The new quantity updated successfully")
    else :
        print("this {name} is not in the cart.")


def view_cart(cart):
    if not cart:
        print("cart is empty")
        return
    
    print("cart summary: ")
    
    for item, i in cart.items():
        p = i["price"]
        q= i["quantity"]
        total = p * q     
        
        # print cart content
        print("Item:", item)
        print("Quantity:", q)
        print("Price:", p)
        print("Total:", total)
    
        
def checkout(cart):
    if not cart:
        print("cart is empty, nothing to checkout")
        
    sub_tot = 0
    for item, i in cart.items():
        p = i["price"]
        q= i["quantity"]
        total = p * q     
        sub_tot+=total
    
     #calculate discount:
    if sub_tot > 100:
        discount = sub_tot* 0.10
    else:
        discount = 0
        
    t_after_dis = sub_tot - discount
    
    print("\nCheckout: ")
    print("Subtotal:", sub_tot)
    print("Discount:", discount)
    print("Total after discount:", t_after_dis)
    print("thanks for shopping")
    cart.clear()
    
    
            

import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    cart = {}

    while True:
        #clear_screen()
        print("\nShopping Cart Menu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Update quantity")
        print("4. View cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Choose an option (1–6): ")

        if choice == '1':
            add_item(cart)
        elif choice == '2':
            remove_item(cart)
        elif choice == '3':
            update_quantity(cart)
        elif choice == '4':
            view_cart(cart)
        elif choice == '5':
            checkout(cart)
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()"""


#Contact Book Manager
file_name = "contacts.txt"

def add_contact():
    name = input("Enter your name: ").strip()
    phone = input("Enter your phone number: ").strip()
    email = input("Enter your email: ")
    
    with open(file_name, "a") as f:
            f.write(f"{name} | {phone} | {email}\n")

    print(f"Contact '{name}' saved successfully!")



def view_contacts():
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()
            
        if not lines:
            print("No contacts found.")
            return
        
        print("All Contacts: ")
        for i, l in enumerate(lines, start=1):
            print(f"{i}. {l.strip()}")
            
    except FileNotFoundError:
        print("No contact file found yet. Please add a contact first.")



def search_contact():
    search_by_name = input("Enter name to search by: ").strip().lower()
    found = False
    try:
            with open(file_name, "r") as f:
                for l in f:
                    name, phone, email = [x.strip() for x in l.split("|")]
                    if search_by_name in name.lower():
                        print(f"Found: {name} | {phone} | {email}")
                        found = True

            if not found:
                print("No contact found with that name.")

    except FileNotFoundError:
            print("Contact file not found.")
            

def delete_contact():
    name_to_delete = input("Enter name to delete its contact: ")
    
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()
               
        delete_list = []
        deleted = False
            
        for line in lines:
            name = line.split("|")[0].strip()
            if name.lower() != name_to_delete:
                delete_list.append(line)
            else:
                deleted = True
        
        if deleted:
            with open(file_name, "w") as file:
                file.writelines(delete_list)
                print(f"Contact '{name_to_delete}' deleted successfully.")
        else:
            print("Contact not found.")

    except FileNotFoundError:
        print("No contact file found.")             


def update_contact():
    name_to_update = input("Enter the name of contact you want to update: ")
    try:
        with open(file_name, "r") as f:
            lines = f.readlines()
               
        update_list = []
        updated = False 
        
        for line in lines:
            name, phone, email = [x.strip() for x in line.split("|")]
            if name.lower() == name_to_update:
                print("Enter new data to update: ")
                
                new_name = input("Enter updated name:").strip() or name 
                new_phone = input("Enter updated phone: ").strip() or phone 
                new_email = input("Enter update email: ").strip() or email
                update_list.append(f"{new_name} | {new_phone} | {new_email}\n")
                updated = True
                   
            else:
                update_list.append(line)

        if updated:
            with open(file_name, "w") as file:
                file.writelines(update_list)
            print(f"Contact '{name_to_update}' updated successfully.")
        else:
            print("Contact not found.")
        
    except FileNotFoundError:
        print("No contact file found.")     

    

def main():
    while True:
        print("\nContact Book Manager")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")

        choice = input("Choose an option (1–6): ").strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            update_contact()
        elif choice == '6':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


# Run the program
if __name__ == "__main__":
    main()