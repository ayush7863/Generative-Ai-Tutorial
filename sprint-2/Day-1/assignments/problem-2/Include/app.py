

from flask import Flask, request

app = Flask(__name__)

form_list = []


@app.route("/")
def message():
    return "Welcome!"


@app.route('/create', methods=['POST'])
def create():
    data = request.get_json()
    form_list.append(data)
    return f"The data received is: {data}"


@app.route('/read', methods=['GET'])
def read():
    return {'forms': form_list}


@app.route('/update/<int:id>', methods=['PATCH'])
def update(id):
    data = request.get_json()
    for form in form_list:
        if form['id'] == id:
            form.update(data)
            return f"The Updated data is: {form}"
    return "Invalid Id"


@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    for form in form_list:
        if form['id'] == id:
            form_list.remove(form)
            return "Deleted Successfully"
    return "Invalid Id"


if __name__ == '__main__':
    app.run()
