class Bank_account:
    def __init__(self,acc_no,name,acc_type,balance):
        self.acc_no=acc_no
        self.name=name
        self.acc_type=acc_type
        self.balance=balance
        print("Account created!")
    def deposit(self,amount):
        if amount>0 :
            self.balance=self.balance+amount
            return True
        else:
            return False
    def withdraw(self,amount):
        if amount>0 :
            self.balance=self.balance-amount
            return True
        else:
            return False
    def get_acc_no(self):
        return self.acc_no
    def get_balance(self):
        return self.balance
    def get_name(self):
        return self.name
    def get_acc_type(self):
        return self.acc_type
acc_no=int(input("Enter account number: "))
name=input("Enter account holder name: ")
acc_type=input("What type of account do you want? Zero balance/savings: ")
balance=int(input("Enter an initial amount: "))
acc_one=Bank_account(acc_no,name,acc_type,balance)
flag=True
while(flag):
    choice=int(input("Enter a choice:\n0.Exit\n1.Deposit\n2.Withdraw\n3.Show account info\n"))
    if(choice==0):
        flag=False
        break
    elif choice==1:
        amount=int(input("Enter an amount to deposit: "))
        result=Bank_account.deposit(acc_one,amount)
        if(result):
            print("Account balance: ",Bank_account.get_balance(acc_one))
        else:
            print("Please enter a valid amount!")
    elif choice==2:
        amount=int(input("Enter an amount to withdraw: "))
        current_balance=Bank_account.get_balance(acc_one)
        if amount>current_balance :
            print("Not enough balance!")
        else:
            result=Bank_account.withdraw(acc_one,amount)
            print("Account balance: ",Bank_account.get_balance(acc_one))
    elif choice==3:
        print("Account number: ",Bank_account.get_acc_no(acc_one))
        print("Account holder name: ",Bank_account.get_name(acc_one))
        print("Account type: ",Bank_account.get_acc_type(acc_one))
        print("Current balance: ",Bank_account.get_balance(acc_one))
