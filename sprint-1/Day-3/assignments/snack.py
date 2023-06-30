
snackInventory = {}


def addSnacks():
    snack_Id = input("Enter snack Id: ")
    if snack_Id in snackInventory:
        print("SnackId is already Exists try another Id \n")
        return
    snack_name = input("Enter Your Snack name: ")
    price = float(input("Enter Snack Price: "))
    availability = input("Enter Snack Availability (yes/no): ")
    snack = {"snack_id": snack_Id, "snack_name": snack_name,
             "price": price, "availability": availability}
    snackInventory[snack_Id] = snack
    print(f"Snack {snack_name} is added Successfully \n")


def removeSnack():
    snack_Id = input("Enter snack Id: ")
    if snack_Id in snackInventory:
        n = snackInventory[snack_Id]["name"]
        del snackInventory[snack_Id]
        print(f"Snack {n} removed from the inventory.\n")
    else:
        print("Snack ID does not exist in the inventory.\n")
        return


def updateSnack():
    snack_Id = input("Enter snack Id: ")
    if snack_Id in snackInventory:
        availability = input("Enter New Availability (yes/no): ").lower()
        if availability in ["yes", "no"]:
            snackInventory[snack_Id]["availability"] = availability
            print(f"Snack {snack_Id} availability updated Successfully")
        else:
            print("Invalid input Please Enter only yes or no \n")
    else:
        print("Snack id not exists \n")


def recordSales():
    snack_Id = input("Enter SnackId: ")
    if snack_Id in snackInventory:
        if snackInventory[snack_Id]["availability"] == "yes":
            n = snackInventory[snack_Id]['name']
            print(f"Sold {n}")
        else:
            print("Snack is not available for sale.\n")
    else:
        print("Snack Id does not exists.\n")


def main():
    while True:
        print("1 Add Snacks")
        print("2 Remove snacks")
        print("3 Update snack availability")
        print("4 Sales Record")
        print("5 Exit")
        print(snackInventory)
        choice = input("Enter your Choice: ")

        if choice == "1":
            addSnacks()
        elif choice == "2":
            removeSnack()
        elif choice == "3":
            updateSnack()
        elif choice == "4":
            recordSales()
        elif choice == "5":
            break
        else:
            break
    print("Thanks for Coming")


main()
