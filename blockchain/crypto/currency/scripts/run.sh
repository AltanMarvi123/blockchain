#!/bin/bash

# Start 4 instances of montycoin.py on ports 5000-5003
for port in {5000..5003}
do
    python ../montycoin.py --port=$port &
done