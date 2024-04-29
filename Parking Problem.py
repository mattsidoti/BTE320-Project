def getParkingHours():
  hours=int(input(f'How many hours would you like to park for? '))
  return hours

def calcParkingFee(hours):
  if hours<3:
    print('Total=$6')
  elif hours>8:
    print('Total=$20')
  else:
    print(f'Total=${hours*2.5}')

hours=getParkingHours()
calcParkingFee(hours)

def GetParkingHours():
  return int(input('Enter number of hours: '))

def CalcParkingFee(hours):
  minfee = 6
  maxfee = 20
  parkingfee = 2.5*hours
  if parkingfee<=6:
    return minfee
  elif parkingfee>=20:
    return maxfee
  else:
    return parkingfee