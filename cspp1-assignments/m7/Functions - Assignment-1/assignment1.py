'''Functions | Assignment-1 - Paying Debt off in a Year

Write a program to calculate the credit card balance after one year
if a person only pays the minimum monthly payment required by the
credit card company each month.

The following variables contain values as described below:
balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal
monthlyPaymentRate - minimum monthly payment rate as a decimal

For each month, calculate statements on the monthly payment and remaining balance.
At the end of 12 months, print out the remaining
balance. Be sure to print out no more than two decimal digits of accuracy - so print

Remaining balance: 813.41
instead of
Remaining balance: 813.4141998135

So your program only prints out one thing:
the remaining balance at the end of the year in the format:
Remaining balance: 4784.0

A summary of the required math is found below:
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) +
(Monthly interest rate x Monthly unpaid balance)
@Author : Rohithmarktricks
'''

def paying_debt_off_in_a_year(balance_int, annual_interest_rate, monthly_payment_rate):
    '''
    This function will calculate the balance after end of year.
    '''
    updated_balance_each_month = balance_int
    monthly_interest_rate = annual_interest_rate/12.0
    for i in range(1, 13, 1):
        del i
        minimum_monthly_payment = monthly_payment_rate*updated_balance_each_month
        monthly_unpaid_balance = updated_balance_each_month - minimum_monthly_payment
        updated_balance_each_month = monthly_unpaid_balance+\
        (monthly_interest_rate*monthly_unpaid_balance)
    return round(updated_balance_each_month, 2)




def main():
    '''
    This main function will take the data and prints the
    remaining amount to be paid.
    '''
    data_int = input()
    data_int = data_int.split(' ')
    data_int = list(map(float, data_int))
    print("Remaining balance: %s" \
        %paying_debt_off_in_a_year(data_int[0], data_int[1], data_int[2]))

if __name__ == "__main__":
    main()
