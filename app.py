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
category_column = find_column(
    df.columns,
    ["category"]
)
print("Date:", date_column)
print("Description:", description_column)
print("Amount:", amount_column)
print("Category:", category_column)
if category_column is not None:
    print("Category column found.")
    data = df[[date_column, category_column, description_column, amount_column, "Income/Expense"]].copy()
    data.columns = ["Date", "Category", "Note", "Amount", "Income/Expense"]
else:
    print("No category column found.")
    data = df[[date_column, description_column, amount_column, "Income/Expense"]].copy()
    data.columns = ["Date", "Note", "Amount", "Income/Expense"]
    data["Category"] = data["Note"].apply(categorize_transaction)
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