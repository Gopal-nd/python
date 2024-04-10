class Vehical:
    def __init__(self,first,stock):
        self.first=first
        self.stock=stock

    def buy(self):
        print(f"buy this {self.stock}")
    

market = Vehical('itc','apple')

market.buy()
print(market.stock)



print('\n\n\n')
