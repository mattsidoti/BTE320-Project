Name = input('Hi, please enter your name: ')
Customer_type = input('Enter your customer type (n: new, e: existing)')
Deposit = float(input('Enter your deposit amount: $'))

if Customer_type == 'n':
  Interest=.03
else:
  if Deposit<=1000:
    Interest=float(.03)
  elif Deposit<=10000:
    Interest=float(.0325)
  elif Deposit>10000:
    Interest=float(.035)

Amount = (1 + Interest) * Deposit
print(f'{Name}, you will have ${round(Amount,2)} in your account.')