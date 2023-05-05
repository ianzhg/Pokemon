from flask import Flask, request, jsonify
from flask_cors import CORS
from shipping import shipping_estimation

app = Flask(__name__)
CORS(app)

@app.route('/fedex', methods=['POST'])
def get_fedex_data():
    data = request.json
    cards = data.get('cards')
    jp_zipcode = data.get('jp_zipcode', "120-0011")
    us_zipcode = data.get('us_zipcode', "90001")

    scraper = shipping_estimation(cards)  # You should initialize the scraper with any required arguments
    result = scraper.run_all()

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
