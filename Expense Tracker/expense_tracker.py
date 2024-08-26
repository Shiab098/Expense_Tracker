from expense import Expense
from datetime import datetime
import calendar

def main():
    budget = 100000
    print(f"Running Expense tracker💵")
    exepnse_file_path = "expenses.csv"
    expense = get_user_expense()
    print(expense)
    save_expense_to_file(expense,exepnse_file_path )

    summarize_expense(exepnse_file_path,budget)    
    
   
   

def get_user_expense():
    print(f"Getting user expense")
    expense_name = input(f"Enter expense Name: ")
    expense_amount = float(input(f"Enter expense Amount: "))
    print( f"You've Entered: {expense_name} , {expense_amount}")
    
    expense_categories =[
        "Food🍔", 
        "Home🏠", 
        "Work🏢", 
        "Fun🎉", 
        "Misc💫" 
    ]
    while  True:
        print("Select Category: ")
        for i , category_name in enumerate(expense_categories):
            print(f" {i+1}. {category_name}")

        value_range = f"[1 to {len(expense_categories)}]"
        selected_index = int(input(f"Enter the Category Number {value_range}: "))-1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            new_expense = Expense(name=expense_name , category = selected_category, amount=expense_amount)
            return new_expense
        else:
            print("Invalid Category,Please Try Again !!")
        




def save_expense_to_file(expense : Expense , exepnse_file_path):
    print(f"Saving user {expense} to {exepnse_file_path}")
    with open(exepnse_file_path,"a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")
    # pass



def summarize_expense(exepnse_file_path,budget):
    print(f"Summarizing user expense:")
    with open(exepnse_file_path, "r", encoding="utf-8") as f:
        expenses: list[Expense] = []
        lines = f.readlines()
        for line in lines:
            # stripped_lines = line.strip()
            expense_name, expense_ammount, expense_category =line.strip().split(",")
            line_expense = Expense(
                name = expense_name, amount=float(expense_ammount), category=expense_category
            )
            # print(line_expense)
            expenses.append(line_expense)
    # print(expenses) 
    amount_by_category = {}
    for expense in expenses:
        key = expense.category
        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount
    # print(amount_by_category)
    print("Expense By Category: ")
    for key , amount in amount_by_category.items():
        print(f"  {key} : ${amount:.2f}")
    
    total_spent = sum([x.amount for x in expenses])
    print(f"Total Spent: ${total_spent:.2f}")

    remaining_budget = budget - total_spent
    print(f"Remaining Budget: ${remaining_budget:.2f}")
    # Get today's date
    today = datetime.today()

    # Get the total number of days in the current month
    total_days_in_month = calendar.monthrange(today.year, today.month)[1]

    # Calculate the remaining days
    remaining_days = total_days_in_month - today.day

    print(f"Remaining days in the current month: {remaining_days}")
    daily_budget = remaining_budget / remaining_days
    print(f"Budget Per Day : ${daily_budget}")

if __name__ == "__main__":
    main()
