Modifying the add_transaction method by making it update the balance of the sender and reciever:
1) Defined class variables 'user_1_balance,' 'user_2_balance,' and 'user_3_balance,' and set them each to 100
2) Created class methods to access, increase, and decrease user balances
3) Inside the add_transaction method, make sure that the sender and receiver are both one of the users.
   Return an error message if they are not.
4) Using the methods defined earlier, add the transaction amount to the balance of the receiver and subtract it
   from the balance of the sender.
5) Add the transaction information to the blockchain.

Transaction validation:
1) Within the add_transaction method, if the transaction amount is greater than the sender's balance, do not
   make the transaction. Return a message saying "Not enough balance" if this is the case.