from RentalProperty_def import RentalProperty

def reqDollarAmount(prompt, error="Invalid input! Please input a dollar amount. Exclude commas."):
    usr_in = None
    while True:
        try:
            # get user input; if the input cannot be cast to an int, it is invalid and will throw an error
            usr_in = int(float(input(prompt).strip("$")))
            # if the input can be cast to an int, it is valid; break out of this loop
            break
        except:
            # if an error is caught, print 'error' message and continue loop
            print(error)
    return usr_in

# when the program is run, get input from the user about the property
print("~ Welcome to this Cash on Cash ROI calculator!\n~ This program will ask you about the income, expenses, and up-front costs for a property and give you an estimated percentage ROI at the end.\n~ Please answer all questions in dollar amounts.\n\n~ Let's start with projected income:")

# get user input for income
income_rent = reqDollarAmount("What's the total monthly income you will collect from rent? ")
income_misc = reqDollarAmount("What's the total monthly income you will collect from other sources? (laundry, storage, etc) ")
# calculate total income
income_total = sum([income_rent, income_misc])
print(f"Total income: ${income_total}")

# get user input for expenses
print("\n~ Now, let's move on to expenses:")
expense_tax = reqDollarAmount("How much will you pay each month in taxes? ")
expense_insurance = reqDollarAmount("How much will you pay each month for insurance? ")
expense_mortgage = reqDollarAmount("How much will your monthly mortgage payments be? ")
expense_management = reqDollarAmount("How much will you be paying each month for property management? ")
expense_savings = reqDollarAmount("How much will you be saving each month for expected future expenditures? (vacancy, repairs, capital expenditure, etc) ")
expense_misc = reqDollarAmount("How much will you pay each month for other expenses? (utilities, landscaping, etc) ")
# calculate total expenses
expenses_total = sum([expense_tax, expense_insurance, expense_mortgage, expense_management, expense_savings, expense_misc])
print(f"Total expenses: ${expenses_total}")

# get user input for investments
print("\n~ And finally, up-front costs:")
investment_downpayment = reqDollarAmount("What was the total cost of the down payment? ")
investment_misc = reqDollarAmount("What was the total cost of other up-front investments? (closing costs, rehab, etc) ")
# calculate total investments
investments_total = sum([investment_downpayment, investment_misc])
print(f"Total investments: ${investments_total}")

# finally, calculate and show the final output
print("\n~ Now, let's calculate that ROI...")
property = RentalProperty(income_total, expenses_total, investments_total)
print(f"The projected Cash on Cash ROI for the property you specified will be {property.calcROI() * 100}%.")