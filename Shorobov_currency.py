''' 
Sardorbek Shorobov 
CIS2300NFA Final Project CurrencyConverter
'''

class Currency:
        #USD to EUR
    def usd_to_eur(self,u):
        return u*0.89
        #GBP to INR
    def gbp_to_inr(self,g):
        return g*113.61
        #JPY to USD
    def jpy_to_usd(self,j):
        return j*0.0069
        #EUR to GBP
    def eur_to_gbp(self,e):
        return e*0.85
    #Display the options
    def menu(self):
        print("(1) to convert USD to EUR")
        print("(2) to convert GPB to INR")
        print("(3) to convert JPY to USD")
        print("(4) to convert EUR to GBP")
        print("(5) to quit")
    #The Converter Function which also displays the data
    def action(self):
        self.menu()
        choice=int(input("Enter your desired action:\n"))
        while choice !=5:
            if choice>5 or choice<=0:
            choice=int(input("Wrong input. Enter option 1-5:\n"))
            if choice==1:
                i="$"
            elif choice==2:
                i="£"
            elif choice==3:
                i="¥"
            elif choice==4:
                i="€"
            amount=float(input(f"Enter the amount you are converting:\n{i}"))
            if choice==1:
                converted=self.usd_to_eur(amount)
                result="€"
            elif choice==2:
                converted=self.gbp_to_inr(amount)
                result="₹"
            elif choice==3:
                converted=self.jpy_to_usd(amount)
                result="$"
            elif choice==4:
                converted=self.eur_to_gbp(amount)
                result="£"
            else:
                print("Invalid Choice")
            #(Your currency: $00.0)
            print(f"Your currency:{result}{round(converted,2)}")
            #Repeat
            self.menu()
            choice=int(input("Enter your desired action:\n"))
        if choice==5:
            print("Exiting...")
#Main
def main():
    currency1=Currency()
    currency1.action()

main()