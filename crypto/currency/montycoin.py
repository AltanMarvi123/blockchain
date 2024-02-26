#from flask import Flask, render_template, request, session
import datetime
import hashlib
import json
from flask import Flask, jsonify, request
import requests
from uuid import uuid4
from urllib.parse import urlparse
import argparse


class Blockchain:
    

    #initializing user balances and creating a getter method, increasing method, and a decreasing method for each user
    def get_user_1_balance(self):
        return self.user_1_balance
    def increase_user_1_balance(self, amount):
        self.user_1_balance += amount
    def decrease_user_1_balance(self, amount):
        self.user_1_balance -= amount
    
    def get_user_2_balance(self):
        return self.user_2_balance
    def increase_user_2_balance(self, amount):
        self.user_2_balance += amount
    def decrease_user_2_balance(self, amount):
        self.user_2_balance -= amount
    
    def get_user_3_balance(self):
        return self.user_3_balance
    def increase_user_3_balance(self, amount):
        self.user_3_balance += amount
    def decrease_user_3_balance(self, amount):
        self.user_3_balance -= amount
    

    def __init__(self):
        self.chain = []
        self.transactions = []
        self.create_block(proof=1, previous_hash='0')
        self.nodes = set()
        self.user_1_balance = 100
        self.user_2_balance = 100
        self.user_3_balance = 100

    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 'transactions': self.transactions}
        self.transactions = []
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index += 1
        return True

    def add_transaction(self, sender, receiver, amount):
        self.transactions.append({'sender': sender,
                                  'receiver': receiver,
                                  'amount': amount})
        previous_block = self.get_previous_block()
        return previous_block['index'] + 1

    def add_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)

    def replace_chain(self):
        network = self.nodes
        longest_chain = None
        max_length = len(self.chain)
        for node in network:
            response = requests.get(f'http://{node}/get_chain')
            if response.status_code == 200:
                length = response.json()['length']
                chain = response.json()['chain']
                if length > max_length and self.is_chain_valid(chain):
                    max_length = length
                    longest_chain = chain
        if longest_chain:
            self.chain = longest_chain
            return True
        return False


# Creating a Web App
app = Flask(__name__)
#url = 'http://localhost:5000'

# Creating an address for the node on Port 4050
node_address = str(uuid4()).replace('-', '')

# Creating a Blockchain
blockchain = Blockchain()


@app.route('/mine_block', methods=['GET'])
# Mining a new block
def mine_block():
    previous_block = blockchain.get_previous_block()
    previous_proof = previous_block['proof']
    proof = blockchain.proof_of_work(previous_proof)
    previous_hash = blockchain.hash(previous_block)
    blockchain.add_transaction(
        sender=node_address, receiver='user1', amount=1)
    block = blockchain.create_block(proof, previous_hash)


    response = {'message': 'Congratulations, you just mined a block!',
                'index': block['index'],
                'timestamp': block['timestamp'],
                'proof': block['proof'],
                'previous_hash': block['previous_hash'],
                'transactions': block['transactions']}
    
    #NEW CODE: calculate everybody's balance by looping through the list of transactions
    all_transactions = []
    for block in blockchain.chain:
        all_transactions.extend(block['transactions'])

    for transaction in all_transactions:
        if transaction["receiver"] == "user1":
            blockchain.user_1_balance += transaction["amount"]
        elif transaction["receiver"] == "user2":
            blockchain.user_2_balance += transaction["amount"]
        elif transaction["receiver"] == "user3":
            blockchain.user_3_balance += transaction["amount"]

        if transaction["sender"] == "user1":
            blockchain.user_1_balance -= transaction["amount"]
        elif transaction["sender"] == "user2":
            blockchain.user_2_balance -= transaction["amount"]
        elif transaction["sender"] == "user3":
            blockchain.user_3_balance -= transaction["amount"]

    return jsonify(response), 200


@app.route('/get_chain', methods=['GET'])
# Getting the full Blockchain
def get_chain():
    response = {'chain': blockchain.chain,
                'length': len(blockchain.chain)}
    return jsonify(response), 200


@app.route('/confirm_chain', methods=['GET'])
# Checking if the Blockchain is valid
def is_valid():
    is_valid = blockchain.is_chain_valid(blockchain.chain)
    if is_valid:
        response = {'message': 'All good. The Blockchain is valid.'}
    else:
        response = {
            'message': 'Houston, we have a problem. The Blockchain is not valid.'}
    return jsonify(response), 200


@app.route('/add_transaction', methods=['POST'])
# Adding a new transaction to the Blockchain
def add_transaction():
    json = request.get_json()
    print(json)
    transaction_keys = ['sender', 'receiver', 'amount']
    if not all(key in json for key in transaction_keys):
        return 'Some elements of the transaction are missing', 400
    
    #are the sender and receiver valid?
    if(json['sender'] != "user1" and json['sender'] != "user2" and json['sender'] != "user3"):
        return 'Invalid sender'
    if(json['receiver'] != "user1" and json['receiver'] != "user2" and json['receiver'] != "user3"):
        return 'Invalid receiver'

    #does the sender have enough balance?
    user_1_value = blockchain.get_user_1_balance()
    user_2_value = blockchain.get_user_2_balance()
    user_3_value = blockchain.get_user_3_balance()

    if(json['sender'] == "user1"):
        if(user_1_value < json['amount']):
            return 'user1 does not have enough balance'
    elif(json['sender'] == "user2"):
        if(user_2_value < json['amount']):
            return 'user2 does not have enough balance'
    elif(json['sender'] == "user3"):
        if(user_3_value < json['amount']):
            return 'user3 does not have enough balance'
    
    #take money from the sender
    if(json['sender'] == "user1"):
        blockchain.decrease_user_1_balance(json['amount'])
    elif(json['sender'] == "user2"):
        blockchain.decrease_user_2_balance(json['amount'])
    elif(json['sender'] == "user3"):
        blockchain.decrease_user_3_balance(json['amount'])

    #give money to the receiver
    if(json['receiver'] == "user1"):
        blockchain.increase_user_1_balance(json['amount'])
    elif(json['receiver'] == "user2"):
        blockchain.increase_user_2_balance(json['amount'])
    elif(json['receiver'] == "user3"):
        blockchain.increase_user_3_balance(json['amount'])


    index = blockchain.add_transaction(
        json['sender'], json['receiver'], json['amount'])
    response = {'message': f'This transaction will be added to Block {index}'}
    return jsonify(response), 201


@app.route('/connect_node', methods=['POST'])
# Connecting new nodes
def connect_node():
    json = request.get_json()
    nodes = json.get('nodes')
    if nodes is None:
        return "No node", 400
    for node in nodes:
        blockchain.add_node(node)
    response = {'message': 'All the nodes are now connected. The Montycoin Blockchain now contains the following nodes:',
                'total_nodes': list(blockchain.nodes)}
    return jsonify(response), 201


@app.route('/replace_chain', methods=['GET'])
# Replacing the chain by the longest chain if needed
def replace_chain():
    is_chain_replaced = blockchain.replace_chain()
    if is_chain_replaced:
        response = {'message': 'The nodes had different chains so the chain was replaced by the longest one.',
                    'new_chain': blockchain.chain}
    else:
        response = {'message': 'All good. The chain is the largest one.',
                    'actual_chain': blockchain.chain}
    return jsonify(response), 200


parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int, default=4050, help='port to listen on')
args = parser.parse_args()

# Running the app
app.run(host='0.0.0.0', port=args.port)