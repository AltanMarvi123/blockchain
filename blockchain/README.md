# Blockchain Spring 2024

### HI EVERBODY

## Blockchain

### Endpoint Collections
  - [Basic Blockchain](https://nobles-blockchain.postman.co/workspace/New-Team-Workspace~6ee04c91-09b2-4066-a420-2d5e83667e0d/collection/24854847-a4059b9c-1111-4056-82e7-6c845caf1603?action=share&creator=24854847)
  - [Basic Blockchain Expanded](https://nobles-blockchain.postman.co/workspace/New-Team-Workspace~6ee04c91-09b2-4066-a420-2d5e83667e0d/collection/24854847-852421c2-4abb-4502-a0cf-e8117949fb49?action=share&creator=24854847)

### Running the Project
1. To run the application, use the following command: ```python basic_blockchain_expanded.py```. The application will start a Flask server on http://127.0.0.1:5000.
## Cryptocurrency

MontyCoin is a simple implementation of a blockchain and cryptocurrency.

### Endpoint Collections
  - [Cryptocurrency](https://nobles-blockchain.postman.co/workspace/New-Team-Workspace~6ee04c91-09b2-4066-a420-2d5e83667e0d/collection/24854847-5aaeccc5-c743-4bf6-a1a2-5f3ec30ad654?action=share&creator=24854847)
  - [Transaction Picker](https://nobles-blockchain.postman.co/workspace/Blockchain~6ee04c91-09b2-4066-a420-2d5e83667e0d/collection/31591599-4b3fe1aa-9f86-41a1-9705-ac6bd2beabe5?action=share&creator=24854847)

### Running the Project
1. Navigate to scripts directory
2. Run ```chmod +x run.sh``` and ```chmod +x stop.sh``` to make scripts executable
3. Run the servers (nodes) with ```./run.sh```. This will start 4 nodes on http://127.0.0.1:5000 - http://127.0.0.1:5003
4. Stop the nodes with  ```./stop.sh```

### Project Improvements
1. **Transaction Validation**:  Implement a system to validate transactions before they are added to the blockchain. This could include checking if the sender has enough balance to perform the transaction.
2. **Wallets**: Create a Wallet class that generates private and public keys for users. The private key can be used to sign transactions and the public key can be used as the user's address.
3. **Transaction Signing and Verification**: Implement a system where transactions are signed using the sender's private key and can be verified by others using the sender's public key. This ensures that only the owner of a wallet can make transactions from it.
4. **Improved Mining Process**: Modify the mining process. For example, you could implement a difficulty adjustment algorithm that adjusts the difficulty of the mining process based on the total computational power of the network.
5. **Custom Hashing Algorithm**: Implement a custom hashing algorithm for the blockchain. This could be a great way to learn about cryptographic hash functions.
6. **Peer-to-Peer Network**: Instead of manually adding nodes, implement a peer-to-peer network where nodes can discover each other.
7. **GUI**: Create a graphical user interface (GUI) for easier interaction with the blockchain.
8. **Error Handling**: Improve error handling and return appropriate HTTP status codes and messages when errors occur.
9. **Data Persistence**: Implement a system to store the blockchain data persistently.
10.** Reward System**: Implement a reward system for miners.

### Smart Contracts