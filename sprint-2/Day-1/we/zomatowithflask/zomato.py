# # here I am using pickle 

# import pickle
# from flask import Flask, jsonify, request, Response
# import json

# app = Flask(__name__)

# def load_data():
#     try:
#         with open("data.pickle", "rb") as file:
#             data = pickle.load(file)
#     except FileNotFoundError:
#         data = {
#             "dic_zom": [
#                 {
#                     "id": "1",
#                     'name': "Pizza",
#                     "price": "100",
#                     "available": "yes"
#                 },
#                 {
#                     "id": "2",
#                     'name': "Noodles",
#                     "price": "50",
#                     "available": "no"
#                 },
#                 {
#                     "id": "3",
#                     'name': "Pasta",
#                     "price": "150",
#                     "available": "yes"
#                 }
#             ],
#             "take_order": [],
#             "current_id": 0
#         }
#     return data

# def save_data(data):
#     with open("data.pickle", "wb") as file:
#         pickle.dump(data, file)

# data = load_data()
# dic_zom = data["dic_zom"]
# order_list = data["take_order"]
# current_id = data["current_id"]

# @app.route('/', methods=['GET'])
# def display_menu():
#     menu_json = jsonify(dic_zom)
#     menu_formatted = json.dumps(json.loads(menu_json.get_data()), indent=4)
#     response = Response(menu_formatted, content_type='application/json')
#     return response



# @app.route('/menu', methods=['POST'])
# def add_dish():
#     data = request.get_json()
#     dish_id = data.get('id')
#     dish_name = data.get('name')
#     dish_price = data.get('price')
#     dish_availability = data.get('available')
#     dish = {"id": dish_id, "name": dish_name,
#             "price": dish_price, "available": dish_availability}
#     dic_zom.append(dish)
#     save_data(data)
#     return jsonify({"message": "New dish added successfully!"}), 201


# @app.route('/menu/<dish_id>', methods=['DELETE'])
# def remove_dish(dish_id):   
#     dish = next((item for item in dic_zom if item["id"] == dish_id), None)
#     if dish:
#         dic_zom.remove(dish)
#         save_data(data)
#         return jsonify({"message": "Dish removed successfully"})
#     else:
#         return jsonify({"message": "This dish ID does not exist"}), 404


# @app.route('/order', methods=['POST'])
# def take_order():
#     data = request.get_json()
#     customer_name = data.get('customer_name')
#     dish_id = data.get('dish_id')
#     order = {"id": generate_id(), "dish_id": dish_id, "name": customer_name, "status": "received"}
#     order_list.append(order)
#     save_data(data)
#     return jsonify({"message": "Order placed successfully"}), 201


# @app.route('/menu/<dish_id>', methods=['PATCH'])
# def update_availability(dish_id):
#     dish = next((item for item in dic_zom if item["id"] == dish_id), None)
#     if dish:
#         dish["available"] = "no" if dish["available"] == "yes" else "yes"
#         save_data(data)
#         return jsonify({"message": "Availability updated successfully"})
#     else:
#         return jsonify({"message": "This dish ID does not exist"}), 404


# @app.route('/order/<order_id>', methods=['PATCH'])
# def update_order_status(order_id):
#     order = next((item for item in  order_list if item["id"] == int(order_id)), None)
#     if order:
#         data = request.get_json()
#         new_status = data.get('status')
#         order["status"] = new_status
#         save_data(data)
#         return jsonify({"message": "Order status updated successfully"})
#     else:
#         return jsonify({"message": "This order ID does not exist"}), 404


# @app.route('/order', methods=['GET'])
# def review_all_orders():
#     return jsonify({"orders":  order_list})


# def generate_id():
#     global current_id
#     current_id += 1
#     return current_id


# if __name__ == '__main__':
#     app.run()



# This code is without "pickle" or "json file"
# from flask import Flask, jsonify, request

# app = Flask(__name__)

# dic_zom = [
#     {
#         "id": "1",
#         'name': "Pizza",
#         "price": "100",
#         "available": "yes"
#     },
#     {
#         "id": "2",
#         'name': "Noodles",
#         "price": "50",
#         "available": "no"
#     },
#     {
#         "id": "3",
#         'name': "Pasta",
#         "price": "150",
#         "available": "yes"
#     }
# ]

# take_order = []
# current_id = 0


# @app.route('/menu', methods=['GET'])
# def display_menu():
#     return jsonify(dic_zom)


# @app.route('/menu', methods=['POST'])
# def add_dish():
#     data = request.get_json()
#     dish_id = data.get('id')
#     dish_name = data.get('name')
#     dish_price = data.get('price')
#     dish_availability = data.get('available')
#     dish = {"id": dish_id, "name": dish_name,
#             "price": dish_price, "available": dish_availability}
#     dic_zom.append(dish)
#     return jsonify({"message": "New dish added successfully!"}), 201


# @app.route('/menu/<dish_id>', methods=['DELETE'])
# def remove_dish(dish_id):
#     dish = next((item for item in dic_zom if item["id"] == dish_id), None)
#     if dish:
#         dish['available'] = 'no'
#         return jsonify({"message": "Dish removed successfully"})
#     else:
#         return jsonify({"message": "This dish ID does not exist"}), 404


# @app.route('/order', methods=['POST'])
# def take_order():
#     data = request.get_json()
#     customer_name = data.get('customer_name')
#     dish_id = data.get('dish_id')
#     order = {"id": generate_id(), "dish_id": dish_id, "name": customer_name, "status": "received"}
#     take_order.append(order)
#     return jsonify({"message": "Order placed successfully"}), 201


# @app.route('/menu/<dish_id>', methods=['PATCH'])
# def update_availability(dish_id):
#     dish = next((item for item in dic_zom if item["id"] == dish_id), None)
#     if dish:
#         dish["available"] = "no" if dish["available"] == "yes" else "yes"
#         return jsonify({"message": "Availability updated successfully"})
#     else:
#         return jsonify({"message": "This dish ID does not exist"}), 404


# @app.route('/order/<order_id>', methods=['PATCH'])
# def update_order_status(order_id):
#     order = next((item for item in take_order if item["id"] == int(order_id)), None)
#     if order:
#         data = request.get_json()
#         new_status = data.get('status')
#         order["status"] = new_status
#         return jsonify({"message": "Order status updated successfully"})
#     else:
#         return jsonify({"message": "This order ID does not exist"}), 404


# @app.route('/order', methods=['GET'])
# def review_all_orders():
#     orders = []
#     for order in take_order:
#         dish = next((item for item in dic_zom if item["id"] == order["dish_id"]), None)
#         if dish:
#             orders.append({
#                 "order_id": order["id"],
#                 "dish_name": dish["name"],
#                 "price": dish["price"],
#                 "status": order["status"]
#             })
#     return jsonify({"orders": orders})


# if __name__ == '__main__':
#     app.run()


# here this code with json files I have to created first two json files with name of 
# menu.json and orders.json in same folder


from flask import Flask, jsonify, request
import json

app = Flask(__name__)

MENU_FILE = 'menu.json'
ORDERS_FILE = 'orders.json'
current_id=0

def generate_id():
    global current_id
    current_id += 1
    return current_id

# Helper functions
def read_json_file(file_name):
    with open(file_name, 'r') as file:
        data = json.load(file)
    return data

def write_json_file(file_name, data):
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


@app.route('/', methods=['GET'])
def display_menu():
    menu = read_json_file(MENU_FILE)
    return jsonify(menu)


@app.route('/menu', methods=['POST'])
def add_dish():
    menu = read_json_file(MENU_FILE)
    data = request.get_json()
    dish_id = data.get('id')
    dish_name = data.get('name')
    dish_price = data.get('price')
    dish_availability = data.get('available')
    dish = {"id": dish_id, "name": dish_name, "price": dish_price, "available": dish_availability}
    menu.append(dish)
    write_json_file(MENU_FILE, menu)
    return jsonify({"message": "New dish added successfully!"}), 201


@app.route('/menu/<dish_id>', methods=['DELETE'])
def remove_dish(dish_id):
    menu = read_json_file(MENU_FILE)
    dish = next((item for item in menu if item["id"] == dish_id), None)
    if dish:
        dish['available'] = 'no'
        write_json_file(MENU_FILE, menu)
        return jsonify({"message": "Dish removed successfully"})
    else:
        return jsonify({"message": "This dish ID does not exist"}), 404


@app.route('/order', methods=['POST'])
def take_order():
    orders = read_json_file(ORDERS_FILE)
    data = request.get_json()
    customer_name = data.get('customer_name')
    dish_id = data.get('dish_id')
    order = {"id": generate_id(), "dish_id": dish_id, "name": customer_name, "status": "received"}
    orders.append(order)
    write_json_file(ORDERS_FILE, orders)
    return jsonify({"message": "Order placed successfully"}), 201


@app.route('/menu/<dish_id>', methods=['PATCH'])
def update_availability(dish_id):
    menu = read_json_file(MENU_FILE)
    dish = next((item for item in menu if item["id"] == dish_id), None)
    if dish:
        dish["available"] = "no" if dish["available"] == "yes" else "yes"
        write_json_file(MENU_FILE, menu)
        return jsonify({"message": "Availability updated successfully"})
    else:
        return jsonify({"message": "This dish ID does not exist"}), 404


@app.route('/order/<order_id>', methods=['PATCH'])
def update_order_status(order_id):
    orders = read_json_file(ORDERS_FILE)
    order = next((item for item in orders if item["id"] == int(order_id)), None)
    if order:
        data = request.get_json()
        new_status = data.get('status')
        order["status"] = new_status
        write_json_file(ORDERS_FILE, orders)
        return jsonify({"message": "Order status updated successfully"})
    else:
        return jsonify({"message": "This order ID does not exist"}), 404


@app.route('/order', methods=['GET'])
def review_all_orders():
    orders = read_json_file(ORDERS_FILE)
    menu = read_json_file(MENU_FILE)
    order_list = []
    for order in orders:
        dish = next((item for item in menu if item["id"] == order["dish_id"]), None)
        if dish:
            order_list.append({
                "order_id": order["id"],
                "dish_name": dish["name"],
                "price": dish["price"],
                "status": order["status"]
            })
    return jsonify({"orders": order_list})


if __name__ == '__main__':
    app.run()





# please explain this code step by step in easy manner.