from flask import Flask, request, jsonify
from flask_cors import CORS
from shipping import run_all

app = Flask(__name__)
CORS(app)

@app.route('/runall', methods=['POST'])
def runall():
    data = request.json
    print("this is data: ", data)
    cards = int(data['cards'])
    jp_zipcode = data['jp_zipcode']
    us_zipcode = data['us_zipcode']

    print(cards, jp_zipcode, us_zipcode)
    # Call the runall function with the provided parameters
    result = run_all(cards, jp_zipcode, us_zipcode)

    print(result)
    return jsonify(result)

if __name__ == '__main__':
    app.run()
