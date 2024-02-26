# Basic Blockchain

This is a basic implementation of a blockchain in Python using Flask.

## Endpoints

### `GET /mine_block`

Mines a new block and adds it to the blockchain. Returns the new block as a JSON object.

### `GET /get_chain`

Returns the entire blockchain as a list of blocks, along with the length of the chain.

### `GET /confirm_chain`

Validates the blockchain and returns a JSON object indicating whether the chain is valid.

### `POST /add_transaction`

Adds a new transaction to the transaction pool. The transaction should be provided as a JSON object in the request body with the following format:

```json
{
    "sender": "sender username",
    "receiver": "receiver username",
    "amount": amount
}
```
Returns a JSON object indicating whether the transaction was successfully added to the pool.

### GET /get_transactions
Returns a JSON object containing the current transaction pool and the list of completed transactions.

### GET /get_users
Returns a JSON object containing all users.

### GET /get_user_balances
Returns a JSON object containing the balance of each user.

### POST /create_user
Creates a new user. The username should be provided as a JSON object in the request body with the following format:

```json
{
    "name": "username"
}
```
Returns a JSON object indicating the status of the new user.

### Running the Application
To run the application, use the following command:
```bash
python basic_blockchain_expanded.py
```
The application will start a Flask server on http://127.0.0.1:5000.
