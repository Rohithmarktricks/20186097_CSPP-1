# Exercise: PowerRecr
# Write a Python function, recurPower(base, exp), that takes in two numbers and returns the base^(exp) of given base and exp.

# This function takes in two numbers and returns one number.
i = 0
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
    returns: int or float, base^exp
    '''
    
    global i
    print(i)
    if i <= exp:
        if exp == 1:
            return base
        
        else: i += 1
        print(i)
        return base*recurPower(base,i)

    

def main():
    data = input()
    data = data.split()
    print(recurPower(float(data[0]), int(data[1])))   

if __name__ == "__main__":
    main()