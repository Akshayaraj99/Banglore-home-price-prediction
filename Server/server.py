# server.py
from flask_cors import CORS
from flask import Flask, request, jsonify
import util  # <-- Make sure this line is there

# 1. Create the Flask app
app = Flask(__name__)
CORS(app)
app.url_map.strict_slashes = False


# 2. Add your original routes
@app.route('/api/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/api/predict_home_price', methods=['POST'])
def predict_home_price():
    # Get data from the form that Postman will send
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    # Call your utility function to get the price
    response = jsonify({
        'estimated_price': util.get_estimated_price(location, total_sqft, bhk, bath)
    })

    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


# 3. The CRITICAL part: Run the server on the correct port
if __name__ == '__main__':
    print("Starting Python Flask Server for Home Price Prediction...")
    util.load_saved_artifacts()  # <-- This is important to load your model!
    app.run(port=5001)  # <-- MAKE SURE IT IS PORT 5001