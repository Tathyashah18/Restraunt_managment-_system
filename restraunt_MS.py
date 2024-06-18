options=["Hot Coffee","Snacke","Cold Coffee","Desert"]
price_d={"Cappuccino":200,"Expresso":200,"Flat white":200,"Vanilla Latte":400,"Sandwich":200,"pizza":200,"burger":200,"bread sticks":400,"Ice Tea":200,"Cold Mocha":200,"Crunchy Frappe":200,"Vegan Shake":400,"CheeseCake":200,"Brownie":200,"Vanilla Scoop":200,"Red Velvet cake":400}
price=0

while True:
    print("\n MENU\n1.Hot Coffee\n2.Snacks\n3.Cold coffee\n4.Desert")
    ch=int(input("Enter choice from above:"))
    if ch==1:
        print("\n Hot Coffee Menu\n1.Cappuccino--200\n2.Expresso--200\n3.Flat white--200\n4.Vanilla Latte\n")
        ch_1=int(input("Enter choice from above:"))
        if ch_1==1:
            price+=price_d["Cappuccino"]
        elif ch_1==2:
            price+=price_d["Expresso"]
        elif ch_1==1:
            price+=price_d["Flat white"]
        elif ch_1==1:
            price+=price_d["Vanilla Latte"]
        else:
            print("\nInvalid Input")
    elif ch==2:
        print("\n Snacks Menu\n1.Sandwich--200\n2.pizza--200\n3.burger--200\n4bread sticks-400\n")
        ch_1=int(input("Enter choice from above:"))
        if ch_1==1:
            price+=price_d["Sandwich"]
        elif ch_1==2:
            price+=price_d["pizza"]
        elif ch_1==1:
            price+=price_d["burger"]
        elif ch_1==1:
            price+=price_d["bread sticks"]
        else:
            print("\nInvalid Input")
    elif ch==3:
        print("\n Cold coffee Menu\n1.Ice Tea--200\n2.Cold Mocha--200\n3.Crunchy Frappe--200\n4.Vegan Shake-400\n")
        ch_1=int(input("Enter choice from above:"))
        if ch_1==1:
            price+=price_d["Ice Tea"]
        elif ch_1==2:
            price+=price_d["Cold Mocha"]
        elif ch_1==1:
            price+=price_d["Crunchy Frappe"]
        elif ch_1==1:
            price+=price_d["Vegan Shake"]
        else:
            print("\nInvalid Input")
    elif ch==4:
        print("\nDesert Menu\n1.CheeseCake--200\n2.Brownie--200\n3.Vanilla Scoop--200\n4.Red Velvet cake-400\n")
        ch_1=int(input("Enter choice from above:"))
        if ch_1==1:
            price+=price_d["CheeseCake"]
        elif ch_1==2:
            price+=price_d["Brownie"]
        elif ch_1==1:
            price+=price_d["Vanilla Scoop"]
        elif ch_1==1:
            price+=price_d["Red Velvet cake"]
        else:
            print("\nInvalid Input")
    else:
        print("\nInvalid input")
    ch_again=input("Do you want to continue the order (Y/N):")
    if ch_again.upper()=="N":
        print(f"\nYour bill is {price:.2f}")
        break
    elif ch_again.upper()=="Y":
        continue
    else:
        print("\nInvalid input")
print("\nThank You")