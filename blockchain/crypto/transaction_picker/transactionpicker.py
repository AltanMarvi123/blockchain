# Import Libraries
from flask import Flask, jsonify
from data import transactions_list


# Create Web App
app = Flask(__name__)


@app.route('/get_transactions', methods=['GET'])
# returns list of transactions
def get_transactions():
    response = {'Transactions': transactions_list}
    return jsonify(response), 200


@app.route('/get_ten_highest_fees', methods=['GET'])
# Returns list of 10 transactions with highest fees
def get_ten_highest_fees():
    response = {}  # placeholder
    return jsonify(response), 200


@app.route('/get_ten_lowest_fees', methods=['GET'])
# Returns list of 10 transactions with lowest fees
def get_ten_lowest_fees():
    response = {}  # placeholder
    return jsonify(response), 200


@app.route('/get_next_highest_total', methods=['GET'])
# Returns second highest total fee sum after picking 10 transactions
def get_next_highest_total():
    response = {}  # placeholder
    return jsonify(response), 200


# Run app
app.run(host='0.0.0.0', port=5050)
