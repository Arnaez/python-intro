house_total_cost = 0.0
portion_down_payment = 0.25
current_savings = 0.0
annual_return_rate = 0.04
annual_salary = 0.0
portion_salary_saved = 0.1

annual_salary = float(input("Enter your annual salary: "))
portion_salary_saved = float(input("Enter the portion of your salary saved, as a decimal: "))
house_total_cost = float(input("Enter the cost of your dream house: "))

months = 0

while current_savings < house_total_cost * portion_down_payment:
    current_savings += current_savings*annual_return_rate/12 + annual_salary/12 * portion_salary_saved
    months += 1

print(months, " months.")





