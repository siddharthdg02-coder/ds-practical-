size = int(input("Enter hash table size (minimum 2): "))

# Create hash table
hash_table = [None] * size

print("1. Linear Probing")
print("2. Quadratic Probing")
print("3. Double Hashing")

method = int(input("Choose collision method (1/2/3): "))


# Hash function
def hash_function(name):
    return sum(ord(ch) for ch in name) % size


# Second hash function for double hashing
def second_hash(name):
    return 1 + (sum(ord(ch) for ch in name) % (size - 1))


# Add contact
def add_contact():
    name = input("Enter client name: ")
    phone = input("Enter telephone number: ")

    h = hash_function(name)

    for i in range(size):

        if method == 1:
            index = (h + i) % size

        elif method == 2:
            index = (h + i * i) % size

        elif method == 3:
            index = (h + i * second_hash(name)) % size

        else:
            print("Invalid collision method.")
            return

        if hash_table[index] is None:
            hash_table[index] = (name, phone)
            print("Contact added successfully.")
            return

    print("Hash table is full!")


# Search contact
def search_contact():
    name = input("Enter client name to search: ")
    h = hash_function(name)

    for i in range(size):

        if method == 1:
            index = (h + i) % size

        elif method == 2:
            index = (h + i * i) % size

        else:
            index = (h + i * second_hash(name)) % size

        contact = hash_table[index]

        if contact is None:
            break

        if contact[0].lower() == name.lower():
            print("Telephone Number:", contact[1])
            return

    print("Contact not found.")


# Display directory
def display_directory():
    print("\nIndex | Name | Telephone Number")

    for i in range(size):
        if hash_table[i] is None:
            print(i, "| Empty")
        else:
            name, phone = hash_table[i]
            print(i, "|", name, "|", phone)


# Main menu
while True:

    print("\n1. Add Contact")
    print("2. Search Contact")
    print("3. Display Directory")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        add_contact()

    elif choice == 2:
        search_contact()

    elif choice == 3:
        display_directory()

    elif choice == 4:
        print("Exiting telephone directory.")
        break

    else:
        print("Invalid choice.")
