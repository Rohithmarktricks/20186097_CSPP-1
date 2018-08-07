'''
Assignment 3 : Calculate the minimum amount to be paid,
using Bisection search!!!
@Author : Rohithmarktricks
'''

def paying_debt_off_in_a_year(ba_lance, annual_interest_rate):
    '''
    This function will calculate minimum amount
    '''
    monthly_interest_rate= (annual_interest_rate) / 12.0
    monthly_payment_lower_bound = ba_lance / 12
    monthly_payment_upper_bound = (ba_lance * (1 + monthly_interest_rate)**12) / 12.0
    temp_balance = ba_lance
    epsilon = 0.001
    guess = (monthly_payment_upper_bound + monthly_payment_lower_bound)/2
    while True:
        duration = 1
        while duration <= 12:
            temp_balance = temp_balance - guess
            temp_balance = temp_balance + (monthly_interest_rate * temp_balance)
            duration += 1
        if temp_balance > 0 and temp_balance > epsilon:
            monthly_payment_lower_bound = guess
            temp_balance = ba_lance
        elif temp_balance < 0 and temp_balance < -epsilon:
            monthly_payment_upper_bound = guess
            temp_balance = ba_lance
        else:
            return guess
        guess = (monthly_payment_lower_bound + monthly_payment_upper_bound)/2

def main():
    '''
    main function!
    '''
    data = input()
    # data = "4773 0.2"
    data = data.split(' ')
    data = list(map(float, data))
    print("Lowest Payment: "+str(round(paying_debt_off_in_a_year(data[0],data[1]),2)))
    
if __name__ == "__main__":
    main()
