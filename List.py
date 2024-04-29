List = []
while True:
  userInput=int(input('Entr an integer to append to the list: '))
  if userInput==0:
    break
  List.append(userInput)
  print(f'Here is your current list: {List}')

print(f'Here is your list: {List}')