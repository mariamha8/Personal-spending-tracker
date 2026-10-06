category_rules = {
    # Housing
    "rent": "Housing",
    "mortgage": "Housing",
    "property tax": "Housing",
    "home insurance": "Housing",

    # Utilities
    "electricity": "Utilities",
    "hydro": "Utilities",
    "water": "Utilities",
    "gas bill": "Utilities",
    "internet": "Utilities",
    "phone bill": "Utilities",
    "rogers": "Utilities",
    "bell": "Utilities",
    "telus": "Utilities",

    # Food
    "grocery": "Food",
    "groceries": "Food",
    "mcdonald": "Food",
    "starbucks": "Food",
    "tim hortons": "Food",
    "subway": "Food",
    "domino": "Food",
    "pizza": "Food",
    "restaurant": "Food",

    # Transportation
    "uber": "Transportation",
    "lyft": "Transportation",
    "taxi": "Transportation",
    "shell": "Transportation",
    "esso": "Transportation",
    "petro": "Transportation",
    "gas station": "Transportation",
    "transit": "Transportation",
    "metro": "Transportation",

    # Insurance & Medical
    "insurance": "Insurance & Medical",
    "pharmacy": "Insurance & Medical",
    "pharma": "Insurance & Medical",
    "dental": "Insurance & Medical",
    "doctor": "Insurance & Medical",
    "clinic": "Insurance & Medical",
    "hospital": "Insurance & Medical",

    # Savings & Investments
    "savings": "Savings & Investments",
    "investment": "Savings & Investments",
    "invest": "Savings & Investments",
    "tfsa": "Savings & Investments",
    "rrsp": "Savings & Investments",

    # Debt Repayment
    "loan": "Debt Repayment",
    "student loan": "Debt Repayment",
    "credit card payment": "Debt Repayment",
    "debt": "Debt Repayment",

    # Shopping
    "amazon": "Shopping",
    "walmart": "Shopping",
    "target": "Shopping",
    "costco": "Shopping",
    "clothing": "Shopping",
    "nike": "Shopping",
    "adidas": "Shopping",
    "apple store": "Shopping",
    "best buy": "Shopping",

    # Entertainment
    "netflix": "Entertainment",
    "spotify": "Entertainment",
    "youtube": "Entertainment",
    "disney": "Entertainment",
    "cinema": "Entertainment",
    "movie": "Entertainment",
    "concert": "Entertainment",
    "steam": "Entertainment",
    "playstation": "Entertainment",
    "xbox": "Entertainment",

    # Personal Care
    "salon": "Personal Care",
    "haircut": "Personal Care",
    "barber": "Personal Care",
    "gym": "Personal Care",
    "spa": "Personal Care",
    "skincare": "Personal Care",
    "sephora": "Personal Care",

    # Education
    "tuition": "Education",
    "university": "Education",
    "college": "Education",
    "school": "Education",
    "textbook": "Education",
    "course": "Education",
    "udemy": "Education",
    "coursera": "Education",
}
def categorize_transaction(note):
    note = str(note).lower()
    for keyword, category in category_rules.items():
        if keyword in note:
            return category
    return "Other"