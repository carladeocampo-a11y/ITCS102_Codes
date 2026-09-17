
age = int(input("Enter your age ---> "))
isEmployed = bool(input("Are you currently employed (true/false) ---> "))
credit_score = int(input("What is your credit score ---> "))
annual_income = float(input("What is your annual income ---> "))
hasCollateral = bool(input("Does it have collateral (true/false) ---> "))

base_rate = 0.0

if age >=21 and isEmployed == True :
    print("Accepted Baseline Criteria")
    if credit_score >= 750:
        print("Your have high credit score")
        if annual_income >= 100000:
            print("You have high salary")
            base_rate = 4.5
            print("Your base rate is ", base_rate)
        else:
            base_rate = 5.0
            print("Your base rate is ", base_rate)
    elif credit_score >= 600 and credit_score <750:
        print("Your credit score is less than 750")
        if hasCollateral == True:
            print("Your have collateral")
            base_rate = 7.0
            print("Your base rate is ", base_rate)
        elif annual_income <= 40000:
            print("Low annual income")
            base_rate = 9.5
            print("Your base rate is ", base_rate)
        else:
            base_rate = 8.0 
            print("Your base rate is ", base_rate)
    elif credit_score <= 600:
        print("rejected: Credit score too low")

    else:
        print("Invalid details")

