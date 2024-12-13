from PyQt6.QtWidgets import *
from gui import *

class Logic(QMainWindow, Ui_MainWindow):



        def __init__(self):
                """Initializes the GUI and the user data dictionary."""
                super().__init__()
                self.error_message = None
                self.setupUi(self)
                self._user = None
                self.user_data = {"Jet Black_8932": 1895.57, "Robbie Klassen_1990": 559.23}

                self.search_button.clicked.connect(lambda: self.on_search_click())
                self.enter_button.clicked.connect(lambda: self.enter_click())
                self.exit_button.clicked.connect(lambda: self.exit())


        def enter_click(self):
                """ Handles the click events for the buttons. """
                if self.withdraw_button.isChecked():
                        self.withdraw()
                elif self.deposit_button.isChecked():
                        self.deposit()

        def withdraw(self):
                """Withdrawals from the user's balance."""
                try:
                        # Get the amount to withdraw
                        amount_to_withdraw = float(self.amount_box.toPlainText().strip())
                        if amount_to_withdraw <= 0:
                                self.error_message.setText("The amount must be positive.")
                                return

                        """ Checks if user is logged in"""
                        if self._user:

                                current_balance = self.user_data[self._user] # Get the user's balance

                                if amount_to_withdraw > current_balance:
                                        self.error_message.setText("Insufficient balance") # Insufficient funds
                                else:
                                        self.user_data[self._user] -= amount_to_withdraw # Subtract the amount and update the balance
                                        updated_balance = self.user_data[self._user]

                                        self.balance_message.setText(f"Your balance is ${updated_balance:.2f}.")
                                        self.error_message.setText(f"${amount_to_withdraw:.2f} has been withdrawn.")
                        else:
                                self.error_message.setText("No user is logged in.")
                except ValueError:
                        self.error_message.setText("Please enter a valid amount.")

        def deposit(self):
                """Deposits into the user's balance."""
                try:

                        amount_to_deposit = float(self.amount_box.toPlainText().strip()) # Retrieve the deposit amount from the input field


                        if amount_to_deposit <= 0:
                                self.error_message.setText("Please enter a positive amount.") # Ensure the amount is positive
                                return

                        if self._user:# Check if the current user is logged in

                                self.user_data[self._user] += amount_to_deposit # Access the user's current balance

                                updated_balance = self.user_data[self._user]
                                self.balance_message.setText(f"Your balance is ${updated_balance:.2f}.")
                                self.error_message.setText(f"${amount_to_deposit:.2f} has been deposited.")
                        else:
                                self.error_message.setText("No user is logged in.")
                except ValueError:
                        self.error_message.setText("Please enter a valid amount.")  # Invalid input (non-numeric or empty)

        def exit(self):
                """Clears the name, balance, and other relevant fields."""
                self.first_box.clear() # Clear error message
                self.last_box.clear()
                self.pin_box.clear()
                self.amount_box.clear()
                self.welcome_message.setText("")
                self.balance_message.setText("")
                self.error_message.setText("")

        def on_search_click(self):
                """User login and balance retrieval."""
                # Get user details from input fields
                first_name = self.first_box.toPlainText().strip()
                last_name = self.last_box.toPlainText().strip()
                pin = self.pin_box.text().strip()


                if first_name and last_name and pin: # Check if all fields are filled

                        user_key = f"{first_name} {last_name}_{pin}" # Create a unique key for the user based on name and pin

                        # Check if the user exists in the user_data dictionary
                        if user_key in self.user_data:
                                # Set the current user and display their balance
                                self._user = user_key
                                balance = self.user_data[user_key]
                                self.welcome_message.setText(f"Welcome {first_name} {last_name}!")
                                self.balance_message.setText(f"Your balance is ${balance:.2f}.")
                                self.error_message.setText("")  # Clear previous errors
                        else:
                                # Display an error message for incorrect PIN or user not found
                                self.error_message.setText("Incorrect PIN or user not found. Please try again.")
                else:
                        # Warn the user to fill all fields
                        self.error_message.setText("Please fill in all fields!")

##https://www.freecodecamp.org/news/python-lambda-function-explained/
#https://www.youtube.com/watch?v=8aW3tkIul-8

