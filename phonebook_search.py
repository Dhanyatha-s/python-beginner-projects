# requirements
# phone numbers 
# person's name



phonebook = {
    'Tom': {'name': 'Tom Holand', 'Address': '1 Farriland', 'phoneNO': "9900278273"},
    'Bob': {'name': 'Bob Mechiel', 'Address': '2 Harhod', 'phoneNO': "5724278711"}
}

def find_phone_number(name):
    if name in phonebook:
        return phonebook[name]['phoneNO']
    else:
        return f"No phone number found for {name}"

# Example usage:
name_to_find = input("Enter a name: ")
phone_number = find_phone_number(name_to_find)
print(phone_number)


# def search(name, phonebook):
#     for person , details in phonebook.items():
#         if details['name'] == name:
#             return details['phoneNo']
#     return f"Not found the Number under this {name}"
    
# name_to_find = 'Tom'
# result = search(name_to_find, phonebook)
# print(f"Phone number for{name_to_find}: {result}")