class BankAccount:
    def initial(self):
        self.name,self.acno,self.actype,self.bal="",0,"",0
    def user(self,an,ano,aty):
        self.name=an
        self.acno=ano
        self.actype=aty
    def deposit(self,am):
        print("Previous Balance:",self.bal)
        self.bal+=am
        print("Updated Balance:",self.bal)
    def withdraw(self,am):
        if(self.bal>=am and self.bal!=0):
            print("Previous Balance:",self.bal)
            self.bal-=am
            print("Updated Balance:",self.bal)
        else:
            print("Your Current Balance is",self.bal)
            print("Account UnderFlow")
    def display(self):
        print("Name:",self.name)
        print("Account Number:",self.acno)
        print("Account Type:",self.actype)
        print("Balance:",self.bal)
n=input("\nEnter Account Holder's Name: ")
acno=int(input("Enter Account Number: "))
actype=input("Enter Account Type: ")
print("\n\nEnter 1 to Deposit.\nEnter 2 to Withdraw.")
print("Enter 3 to View Account Details.\nEnter 4 to Exit.")
b=BankAccount()
b.initial()
b.user(n,acno,actype)
while(True):
    ch=int(input("\nEnter your Choice: "))
    if ch==1:
        amt=float(input("Enter Amount to Deposit: "))
        b.deposit(amt)
    elif ch==2:
        amt=float(input("Enter Amount to Withdraw: "))
        b.withdraw(amt)
    elif ch==3:
        b.display()
    elif ch==4:
        print("\nDo you wish to Exit?")
        ch=input("Press Y for YES\nPress N for No: ")
        if(ch=='Y' or ch=='y' or ch=='Yes' or ch=='yes' or ch=='YES'):
            print("Thank You!")
            break
        elif(ch=='N' or ch=='n' or ch=='No' or ch=='no' or ch=='NO'):
            pass
        else:
            print("\nINVALID CHOICE!\nEnter 1 to Deposit.\nEnter 2 to Withdraw.")
            print("Enter 3 to View Account Details.\nEnter 4 to Exit.") 
    else:
        print("\nINVALID CHOICE!\nEnter 1 to Deposit.\nEnter 2 to Withdraw.")
        print("Enter 3 to View Account Details.\nEnter 4 to Exit.")
