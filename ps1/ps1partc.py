house_total_cost = 0.0
portion_down_payment = 0.25
annual_return_rate = 0.04
annual_salary = 0.0
months = 36

annual_salary = float(input("Enter your annual salary: "))
house_total_cost = 1000000
semi_annual_raise = 0.07

epsilon = 100
numGuesses = 0
low = 0
high = 10000
ans = 0
savings = 0
y = 0

while True:
    numGuesses += 1
    if savings < house_total_cost*portion_down_payment:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
    i = 0
    savings = 0
    curr_annual_salary = annual_salary
    for i in range(0, months):
        savings += savings * annual_return_rate / 12 + curr_annual_salary / 12 * (ans/10000.0)
        i += 1
        if i % 6 is 0:
            curr_annual_salary += semi_annual_raise*curr_annual_salary
    if abs(savings - house_total_cost*portion_down_payment) < epsilon:
        print('Best savings rate:', ans / 10000)
        print('Steps in bisection search:', numGuesses)
        break
    if low == high:
        print("Not possible")
        break







