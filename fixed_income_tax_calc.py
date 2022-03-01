# start of code 
''' define given constants '''
flat_tax_rate = 0.2
standard_deduction = 10000
addtl_dependent_deduction = 3000

total_gross_income = float(input('Enter the gross income: '))
#use float to represent the decimal point(s)
total_dependents = int(input('Enter the number of dependents: '))
#don't use float because dependents will always be a whole number

#calculate the income tax
total_income_tax = flat_tax_rate * ((total_gross_income) - (standard_deduction) - (addtl_dependent_deduction) * (total_dependents))
# print the income tax 
print('The income tax is $' + str(total_income_tax))