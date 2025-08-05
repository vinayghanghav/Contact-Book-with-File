
def add_contact(name, phone):
    with open("contacts.txt", "a") as f:
        f.write(f"{name},{phone}\n")

def view_contacts():
    try:
        with open("contacts.txt", "r") as f:
            for line in f:
                name, phone = line.strip().split(",")
                print(f"Name: {name}, Phone: {phone}")
    except FileNotFoundError:
        print("No contacts found!")

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        add_contact(input("Name: "), input("Phone: "))
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        break
    else:
        print("Invalid option")

