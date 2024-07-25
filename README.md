# Introduction

Here is a Personal finance tracker application, a full-fledge CRUD application developed with Python, that allows a user to track their finances over a period of time and can also see a graph of their finance over a selected period of time.

The user can add entries, view entries, update as well as delete entries.

# Tools Used:

- **CSV:** CSV are effcient and lightweight for storing large datasets and because they are plain text files, they are compatible with different platforms and systems, making them easy to read, write, edit with minimal software requirements.

- **Python:** python is the number one choice for this project, the versatility and extensive library made it so. Python is easy to use and read and it has a large community that are active which provides extensive documentation, support and facilitating problem-solving.

- **Git and GitHub:** this is essential for version control and sharing my python application, it also allows for collaboration and project tracking.

# Application Key Elements:

The application contains three main files - [main.py](/python_files/main.py), [data_entry.py](/python_files/data_entry.py) and [finance_data.csv](/csv_load/finance_data.csv)

## Key Elements from main.py

- **CSV class:** this class handles all operations that relates to the CSV file and this includes - initializing, adding, retrieving, updating,and deleting entries.

- **add() Function:** the purpose ofthis function is to prompt the user to enter details of a new transaction and adds it to the CSV.

- **plot_transactions() Function:** this function plots the income and expense data over time using **'matplotlib'**

- **main() Function:** this enables the user to interact with the system using a command-line interface. It offers options such as add, view, delete, update transactions or exit.

- **get_transactions() Function:** this helps to retrieve transaction over a period of time which is going to be selected by the user.

- **update_entry:** this function helps to update an entry in the CSV file by identifying the entry with the row ID

- **delete_entry:** this function helps to delete an entry from the CSV file by identifying the entry with the row ID

## Key Elements from data_entry.py

- **date_format:** this specifies the format of the date to used for parsing and formatting ('%d-%m-%Y' stands for day-month-year)

- **CATEGORIES:** this is a dictionary mapping short-form inputs (E for expense and I for income) to full category names.

- **get_date():** this prompts the user toenter a date and valids the input according to the date format specified. If **allow_default** is set to **True** and the user presses enter without providing a date, the current date is returned.

- **get_amount():** this prompts the user to enter a positive and non-zero number, it checks and handles invalid and negative inputs.

- **get_category():** this enables the user to specify the category of their transaction, whether it is an income or an expense, it ensures inputs are valid and also provides corresponding category names.

- **get_description():** this allows the user to description of the transaction, this is completely optional.

## CLI (Command-Line Interface) screenshots:

### Main menu

![Main Menu](assets/main_menu.JPG)

_This is the main menu of the application, the user selects any option they want to make use of_

### Adding new entry

![Adding new entry](assets/option_1_in-use.JPG)

_This screenshot shows the option one (adding a new transaction) in use with all the parameters duly filled_

### Viewing transaction and Summary

![viewing transaction and summary](assets/option_2_in-use.JPG)

_This screenshot shows option two in use showing transactions and summary from 01-07-2024 to 20-07-2024_

![summary graph](assets/Figure_1_graph-of-period_selected-in-option_2.png)

_Here is the graph plotted for the same timeframe selected above_

### Delete a transaction

![Delete a transaction](assets/option_3_delete-in-use.JPG)

_This screenshot shows option three (deleting a transaction) which is done by seleting the rowID of the entry on the CSV file._

### Update a transaction

![Update a transaction](assets/option_4-update-in-use.JPG)

_This screenshot shows option four in use (updating a transaction) which is done by seleting the rowID of the entry on the CSV file._

### Terminating the application

![terminating the application](assets/option_5-exit-programme.JPG)

_Option five exits the application._

## Conclusion

The application can be extended to make use of GUI (that way it might be able to be used on mobile devices for easy accessibility) and another type of database management system such as SQL, this will be dependent on the use case.
