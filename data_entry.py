from datetime import datetime

DATE_FORMAT = "%d-%m-%Y"
CATEGORIES = {
    "I": "Income",
    "E": "Expense"
}


def get_date(prompt, allow_default=False):
    date_str = input(prompt)

    #Use today as the date
    if allow_default and not date_str:
        return datetime.today().strftime(DATE_FORMAT)

    #Check to make sure date iven by user is in valid format
    try:
        valid_date = datetime.strptime(date_str, DATE_FORMAT)
        return valid_date.strftime(DATE_FORMAT)
    except ValueError:
        print("Invalid date format. Expected format is 'dd-mm-yyyy'")
        return get_date(prompt, allow_default)


def get_amount():
    #Try to get the amount from the user
    try:
        amount = float(input("Enter the amount: £"))
        #Ensure the amount is greater than 0
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        return amount
    #Except and recurse the get_amount method
    except ValueError:
        print(ValueError)
        return get_amount()


def get_category():
    #Get the category from the user
    category = input("Enter the category. ['I' for Income or 'E' for Expense]: ").upper()
    if category in CATEGORIES:
        return CATEGORIES[category]
    #Recurese the get_category method if the category entered is invalid

    print("Invalid category entered")
    return get_category()


def get_description():
    return input("Enter a description (optional): ")
