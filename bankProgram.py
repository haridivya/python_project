#it is a basic banking program it has 4 methods 
'''
1.showBalance
2.Deposite
3.Withdraw
4.exit
'''
("***************")
print("Bank Program")
print("****************")
def currentbalance():
    print(f"Balance is {balance}")
def deposite():
    amount=int(input("Enter the amount to deposite:"))
    if amount<0:
        print("Invaild amount")
    else:
        return amount
def withdraw():
    withdrawamount=int(input("enter the amount to withdraw:"))
    if withdrawamount<balance:
        return withdrawamount
    else:
        print("Insufficient balance")
        return 0
balance=0
n=True
while n:
    print("***********************")
    print("1.Show Balanace","2.Deposite","3.WithDraw","4.Exit",sep='\n')
    userChoice=int(input("Enter Your Choice (1-4):"))
    if userChoice==1:
        currentbalance()
    elif userChoice==2:
        balance+=deposite()
    elif userChoice==3:
        balance-=withdraw()
    elif userChoice==4:
        print("Thank you have a nice day")
        n=False
    else:
        print("Invaild operation")
            
