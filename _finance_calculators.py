import math

print("Choose either 'investment or 'bond' from the menu below to proceed:\n\n ")

print("""

investment  -  to calculate the amount of interest you will earn on your investment

bond        -  to calculate the amount you will have to pay on a home loan

""")

# User is choosing either investment or bond so we need that input from them.

user_choice = (input("What would you like to choose please:\n\n"))

# If user chose investment:

if user_choice == "investment" or user_choice == "Investment" or user_choice == "INVESTMENT":

    # We are asking user to input the amount of money they will deposit:
    deposited_amount = float(input("Please enter the amount of money you are willing to deposit:\n\n"))

    # We are asking user for the interest rate:
    interest_rate = float(input("Please enter the interest rate you would be happy with:\n\n"))

    # We are asking user to enter number of years they are planning to invest:
    number_of_years = int(input("Please enter number of years you are planning to invest:\n\n"))

    # Asking user if they want simple or compound interest:
    interest = input("Do you want simple or compound interest?\n\n")
    
    # If user choose simple interest we will calculate return based on the formula:
    if interest == "simple":
        return_on_simple = deposited_amount * (1 + (interest_rate/100) * number_of_years)

        print(f"This is total return on your investment {return_on_simple.__round__(2)} ")

     # If user choose simple interest we will calculate return based on the formula:

    elif interest == "compound":
        return_on_compound = deposited_amount * math.pow((1 + (interest_rate/100)), number_of_years)
        
        print(f"This is total return on your investment {return_on_compound.__round__(2)} ")

# If user chose bond:

elif user_choice == "bond" or user_choice == "Bond" or user_choice == "BOND":

    # Asking user to input present value of the house:
    present_house_value = int(input("Please enter present value of your property:\n\n"))

    # Asking user to enter interest rate:
    interest_rate = float(input("Please enter the interest rate:\n\n"))

    # Asking user to enter number of months they are planning to repay the bond:
    number_of_months = int(input("Please enter number of months over which you will repay the bond:\n\n"))

    # We are calculating amount that will need to be repaid based on the formula:
    # power = math.pow(1 + interest_rate, (-number_of_months))

    # pow = math.pow(1 + interest_rate, - number_of_months)

    percent_rate = interest_rate/100

    repayment = (percent_rate/12) * (1/(1-(1+percent_rate/12)**(-number_of_months)))*present_house_value

    # Diaplaying how much money will user need to repay each month:
    print(f"You will have to pay {repayment.__round__(2)} each month")

# If user didn't choose any of the options (investment or bond) we will display error message:
else:
    print("Unfortunately you didn't choose any of the options.\n\n. If you want to use our services please make a choice")   

    

    



