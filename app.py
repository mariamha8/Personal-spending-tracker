import pandas as pd 
from categorization import categorize_transaction
#open CSV file and read the data
upload_file = input("Enter the path to your CSV file: ")
df = pd.read_csv(upload_file)
#print the first 5 rows
print(df.head())
print(df.columns)
def find_column(columns, possible_names):
    for column in columns:
        if column.strip().lower() in possible_names:
            return column
    return None
date_column = find_column(
    df.columns,
    ["date", "transaction date", "posting date"]
)
description_column = find_column(
    df.columns,
    ["description", "transaction description", "merchant", "title", "note"]
)
amount_column = find_column(
    df.columns, 
    ["amount", "transaction amount"]
)
withdrawal_column = find_column(
    df.columns,
    ["withdrawals", "withdrawal", "debit", "debits"]
)
deposit_column = find_column(
    df.columns,
    ["deposits", "deposit", "credit", "credits"]
)
category_column = find_column(
    df.columns,
    ["category"]
)
print("Date:", date_column)
print("Description:", description_column)
print("Amount:", amount_column)
print("Withdrawals:", withdrawal_column)
print("Deposits:", deposit_column)
print("Category:", category_column)
if amount_column is not None:
    print("Using Amount column.")
    data = df[[date_column, description_column, amount_column, "Income/Expense"]].copy()
    data.columns = ["Date", "Note", "Amount", "Income/Expense"]
    if category_column is not None:
        data["Category"] = df[category_column]
    else:
        data["Category"] = data["Note"].apply(categorize_transaction)
elif withdrawal_column is not None or deposit_column is not None:
    print("Using Withdrawals and Deposits columns.")
    data = df[[date_column, description_column]].copy()
    data["Amount"] = 0.0
    data["Income/Expense"] = "Expense"

    if withdrawal_column is not None:
        data.loc[df[withdrawal_column].notna(), "Amount"] = df[withdrawal_column]
        data.loc[df[withdrawal_column].notna(), "Income/Expense"] = "Expense"
    if deposit_column is not None:
        data.loc[df[deposit_column].notna(), "Amount"] = df[deposit_column]
        data.loc[df[deposit_column].notna(), "Income/Expense"] = "Income"
    data.columns = ["Date", "Note", "Amount", "Income/Expense"]
    data["Category"] = data["Note"].apply(categorize_transaction)
else:
    print("Could not find an amount format.")
    exit()

data["Date"] = pd.to_datetime(data["Date"])
print(data.head())

def summarize_transactions(by="Category"):
              #Filters dataset to only include expenses #Groups expenses by a column and adds up all amounts in each group
    summary = data[data["Income/Expense"]=="Expense"].groupby(by)["Amount"].sum()
    #sorts cats by total spending from highest to lowest
    return summary.sort_values(ascending=False)
print(summarize_transactions())

print(data.dtypes)
print(data.isnull().sum())