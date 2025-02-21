months = []


monthname = input("Please enter the name of the month: ")


sumelect=0
sumrent=0
sumsavings=0


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




    sumelect=sumelect + electricity
    sumrent = sumrent + rent
    sumsavings = sumsavings + savings


    monthname = input("Please enter the name of the month: ")