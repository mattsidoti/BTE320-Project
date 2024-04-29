print(f'Ad$ Profit')

init_attendees = 20
fixed_cost = 200

for advertising in range (0,201,25):
  ad=float(advertising)
  attendees = float(2*round(advertising**0.5)+init_attendees)
  profit=float((attendees*10)-advertising-fixed_cost)
  print(f'{ad} ${profit}')