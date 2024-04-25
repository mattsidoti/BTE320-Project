
class Mortgage:
        def __init__(self, amount, maturity, interest):
            self.amount = amount
            self.maturity = maturity
            self.__interest = interest

        def __str__(self):
            return 'Initial loan amount: $' + str(self.amount) + '\n' + f'Maturity term: {self.maturity} Years' + '\n' + f'Interest rate: {self.__interest}%'

        def get_interest(self):
            return self.__interest

        def set_interest(self, newInterest):
            if newInterest >= 0:
                self.__interest = newInterest
            else:
                print("Interest must be positive!")

        def payment(self):
            term = self.maturity * 12
            r = self.__interest / 100
            return self.amount * (r * (1 + r) ** term) / ((1 + r) ** term - 1)


m = Mortgage(100000,30,6)

print(m.payment())

print(m.get_interest())

m.set_interest(-5)
print(m.get_interest())

print(m)




