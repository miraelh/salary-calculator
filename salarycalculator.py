months = []

sumelect=0
sumrent=0
sumsavings=0


monthname = input("Please enter the name of the month: ")
while monthname!= "stop":
    salary = int(input("Please enter your Salary for this month: "))
    percentagerent= int(input("Please enter the percentage allocated to Rent: "))
    percentagesavings= int(input("Please enter the percentage allocated to Savings: "))
    percentageelectricity= int(input("Please enter the percentage allocated to Electricity: "))

    savings = percentagesavings * salary / 100
    rent = percentagerent * salary / 100
    electricity = percentageelectricity * salary / 100


   
    month = {
        "month": monthname,
        "salary": salary,
        "amount allocated for rent": rent,
        "amount allocated for savings": savings,
        "amount allocated for electricity": electricity,
    }

    months.append(month)
    
    
    
    
    totalamountspent = savings + rent + electricity
    
    remainder = salary - totalamountspent


    print("The amount allocated for Savings for this month is: " + str(savings))
    print("The amount allocated for Rent for this month is: " + str(rent))
    print("The amount allocated for Electricity for this month is: " + str(electricity))
    print("The total amount spent is: " + str(totalamountspent))




    sumelect=sumelect + electricity
    sumrent = sumrent + rent
    sumsavings = sumsavings + savings




    monthname = input("Please enter the name of the month: ")


    
print (months)

print("The total amount allocated for Savings is: " + str(sumsavings))
print("The total amount allocated for Rent is: " + str(sumrent))
print("The total amount allocated for Electricity is: " + str(sumelect))

