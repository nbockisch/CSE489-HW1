# Running
Requires Python 3. To run the demo, symply run `python3 application.py`.

# Design
## Files
* application.py
Runs the demo, calls all the functions to run the procedure.
* ecash.py
Contains the information necessary for a single instance of an ecash. It contains a function to return it's values as a string.
* customer.py
Contains the functions for all of the customer's functionality, and the code to create a customer object.
* merchant.py
Contains the functions for all of the merchant's functionality, and the code to create a merchant object.
* bank.py
Contains the functions for all of the bank's functionality, and the code to create a bank object.

## Design Notes
The application uses the Python Crypto library for blinding, unblinding, and signing operations.
The ecash is exported as a string so it can be used with the crypto operations.
