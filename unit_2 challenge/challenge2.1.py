class BankAccount:
  def __init__(self,account_number,account_holder_name,initial_balance=0.0):
    self.__accound_number=account_number
    self.__account_holder_name=account_holder_name
    self.__account_balance=initial_balance
    def deposit(self,amount):
      if amount>0:
        self.__account_balance+=amount
        print("Deposited rup{}.new balance: rup{}".format(amount,self.__account_balance))
      else:
        print("Invalid deposit amount.please deposit a positive amount.")
        def withdraw(self,amount):
          if amount>0 and amount<=self.__account_balance:
            self.__account_balance-=amount
            print("Widthdraw rup{}.New balance:rup{}".format(amount,self.__account_balance))
          else:
            print("Invalid widthdraw amount or insfficent balance.")
            def display_balance(self):
              print("Account balance for{} (Account #{}:rup{}".format(self.__account_holder_name,self.__account_number,self.__account_balance))
account=BankAccount(account_number="123456789",account_holder_name="HARI PRAKASH",initial_balance=6000.0)       
account.display_balance()
account.deposit(500.0)
account.widthdraw(200.0)
account.display_balance()