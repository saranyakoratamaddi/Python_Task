#11. Payment System (Runtime Polymorphism) 
#An online store supports multiple payment methods: CreditCard, UPI, and NetBanking. Create a base class Payment with a method process_payment() and 
#override it in each payment type.





class Payment:
    def process_payment(self,amount):
        print(f"Processing the payment of Rs{amount}")
class CreditCard(Payment):
    def process_payment(self,amount):
        print(f"Processing Credit Card Rs{amount} Verifiying Credit Card ")
class Upi(Payment):
    def process_payment(self,amount):
        print(f"Processing UPI payment of Rs{amount}")
class NetBanking(Payment):
    def process_payment(self,amount):
        print(f"Processing NetBanking payment of Rs{amount}")
def display(payment_method:Payment,amount:float):
        payment_method.process_payment(amount)
credit=CreditCard()
upi=Upi()
netbank=NetBanking()
display(credit,3000)
display(upi,650)
display(netbank,4000)
