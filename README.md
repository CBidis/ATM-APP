# Automatic Teller Machine (ATM) SIMULATION
#atm.py

The application  simulates the Backend logic of a cash dispensing Automatic Teller Machine (ATM).
Of course the application is not required to distribute money, but it should be able to simulate and report the out come of people requesting money.

This simulation will not require any authentication or PIN to access the ATM.
Rather it is to be focused on keeping track of the current cash of the ATM, and dispensing only the notes available. 

It  supports $20 and $50 notes.
It should be able to dispense only legal combinations of notes. For example, a request for $100 can be satisfied by either five $20 notes or two $50 notes. It is not required to present a list of options.

If a request cannot be satisfied due to failure to find a suitable combination of notes, it should report an error condition in some fashion. For example, in an ATM with only $20 and $50 notes, it is not possible to dispense $30.

Dispensing money reduces the amount of available cash in the machine.
Failure to dispense money due to an error does not reduce the amount of available cash in the machine. 

#atminitDB.py

It is the python module responsible for the creation and initialization of the table(SQLite) that keeps track of 
the notes available to dispense  and the available amount of  money.

#setup.py

This module creates the executable of the source-code for windows machines , it uses the Cx_freeze library. 
