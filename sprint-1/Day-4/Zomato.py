dic_zom = [{
    "id": "1",
    'name': "Pizza",
    "price": "100",
    "available": "yes"
}, {
    "id": "2",
    'name': "Noodles",
    "price": "50",
    "available": "no"

}, {
    "id": "3",
    'name': "Pasta",
    "price": "150",
    "available": "yes"
}]
take_order = []

current_id = 0


def generate_id():
    global current_id
    current_id += 1
    return current_id


def displayMenu():
    x = len(dic_zom)
    print("Menu List\n================\n")
    for i in range(x):
        id = dic_zom[i]["id"]
        name = dic_zom[i]["name"]
        pr = dic_zom[i]['price']
        av = dic_zom[i]["available"]
        print(f"{id} {name} - Rs.{pr} available:({av})\n")


def addDish():
    dish_id = input("Enter the dish Id: ")
    dish_name = input("Enter the dish Name: ")
    dish_price = input("Enter the dish price: ")
    dish_availability = input("Is this dish available?(yes/no): ")
    dish = {"id": dish_id, "name": dish_name,
            "price": dish_price, "available": dish_availability}
    dic_zom.append(dish)
    print("New dish added successfully!\n")


def removeDish():
    dish_id = input("Enter the dish Id: ")
    if dish_id in dic_zom:
        dic_zom[dish_id]['available'] = 'no'
        print("Dish removed Successfully")
    else:
        print("This dish Id does not exists")


def takeOrder(x):
    print(dic_zom)
    customer_name = input("Enter customer name: ")
    dish_id = input("Enter dish id: ")
    order = {"id": x, "dish_id": dish_id,
             "name": customer_name, "status": "received"}
    take_order.append(order)
    print("Order placed Successfully")


def updateAvailability():
    x = len(dic_zom)
    count = 0
    dish_id = input("Enter dish Id: ")
    for i in range(x):
        y = dic_zom[i]["id"]
        if y == dish_id:
            count += 1
    if count == 0:
        print("Id does not exists")
    else:
        z = int(dish_id)
        avail = dic_zom[z-1]["available"]
        if avail == "yes":
            dic_zom[z-1]["available"] = "no"
            print("Availability updated successfully")
        else:
            dic_zom[z-1]["available"] = "no"
            print("Availability updated successfully")


def updateOrderStatus():
    x = len(take_order)
    count = 0
    order_id = input("Enter your Order Id: ")
    for i in range(x):
        y = take_order[i]["id"]
        if y == int(order_id):
            count += 1
    # print(take_order)
    if count == 0:
        print("Enter Correct OrderId")
    else:
        new_status = input("Enter new Status: ")
        z = int(order_id)
        take_order[z-1]["status"] = new_status
        print("Order Status Updated Successfully")


dish_id = []
status = []
order_id = []


def orderName():
    x = len(take_order)
    for i in range(x):
        dish_id.append(take_order[i]["dish_id"])
        status.append(take_order[i]["status"])
        order_id.append(take_order[i]["id"])
    return dish_id, status, order_id


def reviewAllOrder():
    x = len(take_order)
    y = len(dic_zom)
    name_list = []
    price_list = []
#    dish_id=""

    z = orderName()
    # print(z[0])
    length = len(z[0])

    for i in range(length):
        for j in range(y):            
            if z[0][i] == dic_zom[j]["id"]:
                name_list.append(dic_zom[j]["name"])
                price_list.append(dic_zom[j]["price"])
           
    print("Orders")
    print("-----\n")
    # print(name_list)
    for i in range(length):
        print(f"Orders Id: {order_id[i]}")
        print(f"Dish Name: {name_list[i]}")
        print(f"- Rs.{price_list[i]}")
        print(f"Status: {status[i]}\n")


def zomato():
    while True:
        print("Zomato Chronicles: The Great Food Fiasco")
        print("----------------------------")
        print("1 Display Menu")
        print("2 Add any Dish")
        print("3 Remove Dish")
        print("4 Take a new Order")
        print("5 Update dish availability")
        print("6 Update Order Status")
        print("7 Review All Orders")
        print("8 Exit\n")
        choice = input("Enter Your Choice: ")

        if choice == "1":
            displayMenu()
        elif choice == "2":
            addDish()
        elif choice == "3":
            removeDish()
        elif choice == "4":
            x = generate_id()
            takeOrder(x)
        elif choice == "5":
            updateAvailability()
        elif choice == "6":
            updateOrderStatus()
        elif choice == "7":
            reviewAllOrder()
        elif choice == "8":
            break
        else:
            break

    print("Thanks for Coming")


zomato()
