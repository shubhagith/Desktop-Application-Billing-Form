import sys
import mysql.connector
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout
from PySide6.QtCore import Qt

# Connect to MySQL Database
def connect_db():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="mysqluser",
        password="mysqluser@123",  # Replace with your MySQL password
        database="billing_system"
    )

# Function to save customer and bill data into the database
def save_data(customer_name, customer_email, customer_phone, bill_date, bill_amount):
    db = connect_db()
    cursor = db.cursor()

    # Insert customer data
    cursor.execute("INSERT INTO customers (name, email, phone) VALUES (%s, %s, %s)",
                   (customer_name, customer_email, customer_phone))
    db.commit()

    # Get the customer ID of the last inserted customer
    cursor.execute("SELECT LAST_INSERT_ID()")
    customer_id = cursor.fetchone()[0]

    # Insert bill data for the customer
    cursor.execute("INSERT INTO bills (customer_id, date, amount) VALUES (%s, %s, %s)",
                   (customer_id, bill_date, bill_amount))
    db.commit()

    db.close()

# Function to load data from the database into the table widget
def load_data(table):
    db = connect_db()
    cursor = db.cursor()

    # Retrieve all bills and associated customer details
    cursor.execute("SELECT customers.name, customers.email, customers.phone, bills.date, bills.amount FROM bills "
                   "JOIN customers ON bills.customer_id = customers.id")
    result = cursor.fetchall()

    table.setRowCount(len(result))  # Set the number of rows in the table

    # Populate the table with the retrieved data
    for row_index, row in enumerate(result):
        for col_index, data in enumerate(row):
            table.setItem(row_index, col_index, QTableWidgetItem(str(data)))

    db.close()

# Create the main application window (billing form)
class BillingForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Billing Form")
        self.setGeometry(300, 200, 500, 400)

        # Create layout
        layout = QVBoxLayout()

        # Input fields for customer and bill information
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Customer Name")
        self.email_input = QLineEdit(self)
        self.email_input.setPlaceholderText("Customer Email")
        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Customer Phone")
        self.date_input = QLineEdit(self)
        self.date_input.setPlaceholderText("Bill Date (YYYY-MM-DD)")
        self.amount_input = QLineEdit(self)
        self.amount_input.setPlaceholderText("Bill Amount")

        # Buttons for saving and loading data
        save_button = QPushButton("Save", self)
        save_button.clicked.connect(self.save_data)

        load_button = QPushButton("Load Data", self)
        load_button.clicked.connect(self.load_data)

        # Table to display the customer and bill data
        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Customer Name", "Email", "Phone", "Bill Date", "Amount"])

        # Add widgets to layout
        layout.addWidget(self.name_input)
        layout.addWidget(self.email_input)
        layout.addWidget(self.phone_input)
        layout.addWidget(self.date_input)
        layout.addWidget(self.amount_input)
        layout.addWidget(save_button)
        layout.addWidget(load_button)
        layout.addWidget(self.table)

        self.setLayout(layout)

    # Function to save data entered by the user into the database
    def save_data(self):
        customer_name = self.name_input.text()
        customer_email = self.email_input.text()
        customer_phone = self.phone_input.text()
        bill_date = self.date_input.text()
        bill_amount = self.amount_input.text()

        # Save the data into the database
        save_data(customer_name, customer_email, customer_phone, bill_date, bill_amount)

        # Clear the input fields
        self.name_input.clear()
        self.email_input.clear()
        self.phone_input.clear()
        self.date_input.clear()
        self.amount_input.clear()

    # Function to load and display data from the database
    def load_data(self):
        load_data(self.table)

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = BillingForm()
    window.show()

    sys.exit(app.exec())
