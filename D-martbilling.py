while True:
    customer_name =input("enter custumer name:")
    cus_number= int(input("enter customer mobile number:"))
    print("welcome to D-MART")
    grand_total = 0

    while True:
        product = input("name of product:")

        amount = float(input("enter MRP rate: "))
        quantity = float(input("enter quantity:"))
        n=int(input("enter today discount%:"))
        total = (amount * quantity)
        total-= (total*n)/100
        grand_total+=total
        print( "product_name:",product, "quantity:", quantity,  "MRP;",amount, "discoun:",n,"%","TOTAL:",total)
        print("-"*40)
        repeat=input("you want add more item yes/no")
        if repeat=="no" or repeat=="NO":
            break
    print("_"*40)
    print("your grand total is =",grand_total)
    print("_" * 40)
    print("************ thankyou for shopping *****************")

    next = input("do you want add next custumer yes/no")
    if next=="no":
        break


