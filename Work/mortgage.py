# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0
extra_payment = 1000

'''
My solution fails, but I'm not sure why.

while principal > 0:
    month += 1
    if month < 13:
        principal = principal * (1+rate/12) - (payment + extra_payment)
        total_paid = total_paid + (payment + extra_payment)
        print(month, total_paid, principal)
        continue
    if payment >= principal:
        payment = principal * (1+rate/12)
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    
    print(month, round(payment), round(total_paid), 
          round(principal))

print('Total paid', total_paid)
'''


extra_payment = 1000.0
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 0:
    month = month + 1
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment
    
    if payment >= principal:
        payment = principal * (1+rate/12)
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

    print(month, round(total_paid,2), round(principal, 2))
    
print('Total paid', round(total_paid, 2))
print('Months', month)