'''
Assignment-2 - Paying Debt off in a Year

Now write a program that calculates the minimum fixed monthly payment
needed in order pay off a credit card balance within 12 months.
By a fixed monthly payment, we mean a single number which does not change each month,
but instead is a constant amount that will be
paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:
balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly
payment that will pay off all debt in under 1 year, for example:
Lowest Payment: 180

Assume that the interest is compounded monthly according to the
balance at the end of the month (after the payment for that month is
made).
The monthly payment must be a multiple of $10 and is the same for all months.
Notice that it is possible for the balance to become
negative using this payment scheme, which is okay.
A summary of the required math is found below:
Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
@Author : Rohithmarktricks
'''

def paying_debt_off_in_a_year(ba_lance, annual_interestrate):
    '''
    This function calculates the minimum amount to be paid every month!
    We make use of bisection method for this!
    '''
    if ba_lance < 0:
        return 0
    mi_ni = 10
    while True:
        in_it = 0
        ba_lance2 = ba_lance
        while in_it != 12:
            re_main = ba_lance2 - mi_ni
            ba_lance2 = re_main+(re_main*annual_interestrate/12)
            in_it = in_it + 1
        if ba_lance2 <= 0.5:
            break
        mi_ni += 10
    return mi_ni

        
def main():
    '''
    Main Function to calculate the minimum amount
    '''
    da_ta = input()
    da_ta = da_ta.split(' ')
    da_ta = list(map(float, da_ta))
    print("Lowest Payment: "+str(paying_debt_off_in_a_year(da_ta[0],da_ta[1])))

if __name__ == "__main__":
    main()
