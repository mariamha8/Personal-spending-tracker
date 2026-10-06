import pandas as pd 
#open CSV file and read the data
df = pd.read_csv("Dataset/transactions.csv")
#print the first 5 rows
print(df.head())
data = df[["Date", "Category", "Note", "Amount", "Income/Expense"]]
print(data.head())

def summarize_transactions(by="Category"):
              #Filters dataset to only include expenses #Groups expenses by a column and adds up all amounts in each group
    summary = data[data["Income/Expense"]=="Expense"].groupby(by)["Amount"].sum()
    #sorts cats by total spending from highest to lowest
    return summary.sort_values(ascending=False)
print(summarize_transactions())

print(data.dtypes)
print(data.isnull().sum())