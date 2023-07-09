from flask import Flask, jsonify, request
import json

weather_data = {
    'San Francisco': {'temperature': 14, 'weather': 'Cloudy'},
    'New York': {'temperature': 20, 'weather': 'Sunny'},
    'Los Angeles': {'temperature': 24, 'weather': 'Sunny'},
    'Seattle': {'temperature': 10, 'weather': 'Rainy'},
    'Austin': {'temperature': 32, 'weather': 'Hot'},
}


def create_app():
    app = Flask(__name__)

    @app.route("/weather/<string:city>", methods=['GET'])
    def get_Route(city):
        if city in weather_data:
            result = weather_data[city]
            return jsonify(result)
        else:
            return 'City not found'

    @app.route("/create", methods=['POST'])
    def post_route():
        new_weather = request.get_json()
        weather_data.update(new_weather)        
        return jsonify(new_weather), 201
    
    @app.route("/update/<city>",methods=["PUT"])
    def update_route(city):
        updated_weather=request.get_json()
        weather_data[city]=updated_weather
        return jsonify(updated_weather)
    
    @app.route("/delete/<city>",methods=['DELETE'])
    def delete_route(city):
        if city in weather_data:
            data=weather_data[city]
            del weather_data[city]
            return jsonify(data)
        else:
            return "City not Found"
    


    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

 
