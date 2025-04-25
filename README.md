# **Desktop-Application-Billing-Form Application with PySide6 and MySQL**

This is a **PySide6**-based desktop application that allows users to manage billing information. It connects to a **MySQL database** to store customer and bill data, with functionality to **save** new entries and **load** existing data into a table.

## **Features**
- **Customer Data Entry**: Enter customer details (name, email, phone).
- **Bill Data Entry**: Enter bill details (bill date, amount).
- **Save Data**: Store the entered data in a MySQL database.
- **Load Data**: Retrieve and display stored customer and bill data in a table.

## **Installation Instructions**

### 1. **Prerequisites**
- Python 3.5 or higher
- MySQL server installed and running

### 2. **Install Required Python Packages**
To get started, you will need to install **PySide6** and **mysql-connector-python**.

Use the following command to install dependencies:
```bash
pip install PySide6 mysql-connector-python
```

### 3. **Set Up MySQL Database**
Before running the application, you need to set up a **MySQL** database and tables.

#### SQL to Create Database and Tables:

```sql
CREATE DATABASE billing_system;

USE billing_system;

CREATE TABLE customers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15)
);

CREATE TABLE bills (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_id INT,
    date DATE,
    amount DECIMAL(10, 2),
    FOREIGN KEY (customer_id) REFERENCES customers(id)
);
```

Make sure your MySQL server is running, and you've created the `billing_system` database with the tables above.

## **Running the Application**

### 1. **Clone the Repository**
Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/shubhagith/Desktop-Application-Billing-Form.git
```

### 2. **Run the Python Application**
Navigate to the project folder and run the Python script:
```bash
python billing_app.py
```

This will launch the PySide6 GUI application.

### 3. **Using the Application**
- **Enter customer details** (name, email, phone).
- **Enter bill details** (bill date, amount).
- Click **Save** to save the data to the MySQL database.
- Click **Load Data** to display the saved customers and their bills in the table.

## **How the Application Works**

- **UI (User Interface)**: The main window consists of input fields for customer and bill details, along with buttons to save and load data. It also includes a table to display stored data.
- **Database Operations**: Data is saved to a MySQL database. The `save_data` function handles inserting customer and bill information, while the `load_data` function retrieves and displays it in a table.
  
### **Main Components**:
- **`BillingForm` Class**: This class creates the main window of the application, including input fields and the table.
- **`save_data()`**: This function saves the entered customer and bill data into the MySQL database.
- **`load_data()`**: This function retrieves and displays all stored data in the table.

## **Troubleshooting**

### 1. **MySQL Connection Issues**
- Ensure that MySQL is running and that the correct credentials (host, user, password) are used in the `connect_db()` function.
- Make sure the database (`billing_system`) and tables (`customers`, `bills`) exist.

### 2. **PySide6 Installation Issues**
- If you encounter errors while installing PySide6, make sure you are using a Python version of 3.5 or higher.

  You can install it with:
  ```bash
  pip install PySide6
  ```

### 3. **Database Errors**
- If you see database connection errors, check the MySQL configuration or credentials.
- Ensure your database tables are set up correctly.



